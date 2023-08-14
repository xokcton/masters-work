from yolo import Yolo
from images import Images

import os


def main():
    cfg_path = os.path.join('.', 'model', 'cfg', 'yolov3-spp.cfg')
    weights_path = os.path.join('.', 'model', 'weights', 'yolov3-spp.weights')
    coco_names = os.path.join('.', 'model', 'coco.names')
    output_folder = 'output'
    classes = []

    with open(coco_names, "r") as file:
        classes = [line.strip() for line in file.readlines()]

    y = Yolo(classes=classes, cfg_path=cfg_path, weights_path=weights_path)
    i = Images('images', output_folder)
    imgs = i.get_images()

    for img in imgs:
        output_name = output_folder + '/' + \
            i.get_random_image_name(10) + '-' + img.split('/')[-1]
        print(output_name)
        y.detect(img, output_name)


if __name__ == "__main__":
    main()
