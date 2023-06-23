from yolo import Yolo
from images import Images


def main():
    classes = []
    output_folder = 'output'
    with open("coco.names", "r") as file:
        classes = [line.strip() for line in file.readlines()]

    y = Yolo(classes=classes)
    i = Images('images', output_folder)
    imgs = i.get_images()

    for img in imgs:
        output_name = output_folder + '/' + \
            i.get_random_image_name(10) + '-' + img.split('/')[-1]
        print(output_name)
        y.detect(img, output_name)


if __name__ == "__main__":
    main()
