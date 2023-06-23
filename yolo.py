import cv2
import numpy as np


class Yolo:
    def __init__(self, classes):
        self.classes = classes
        self.yolo = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")

    def detect(self, input_image, output_image):
        layer_names = self.yolo.getLayerNames()
        output_layers = [layer_names[i - 1]
                         for i in self.yolo.getUnconnectedOutLayers()]

        redColor = (0, 0, 255)
        greenColor = (0, 255, 0)

        # Loading Images
        name = input_image
        img = cv2.imread(name)
        height, width, channels = img.shape

        # Detecting objects
        blob = cv2.dnn.blobFromImage(
            img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)

        self.yolo.setInput(blob)
        outputs = self.yolo.forward(output_layers)

        class_ids = []
        confidences = []
        boxes = []
        for output in outputs:
            for detection in output:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)

                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)

                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                cv2.rectangle(img, (x, y), (x + w, y + h), greenColor, 3)
                cv2.putText(img, label, (x, y + 10),
                            cv2.FONT_HERSHEY_PLAIN, 8, redColor, 8)

        cv2.imwrite(output_image, img)
