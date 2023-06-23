import os
import random
import string


class Images:
    def __init__(self, input_folder, output_folder):
        self.input_folder = input_folder
        self.output_folder = output_folder

        if not os.path.exists(self.output_folder):
            os.makedirs(self.output_folder)

    def get_images(self):
        return [(self.input_folder + '/' + image)
                for image in os.listdir(self.input_folder)]

    def get_random_image_name(self, length):
        letters = string.ascii_lowercase
        return ''.join(random.choice(letters) for i in range(length))
