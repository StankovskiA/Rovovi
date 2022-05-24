from itertools import count
import cv2 as cv
from matplotlib import image
import numpy as np

class ImagePartitionReader:

    def __init__(self, image_file) -> None:
        self.map_image = cv.imread('images/main_image.png')

    def get_sub_images(self, sub_image_size):
        sub_images = []

        for i in range(0, self.map_image.shape[1], sub_image_size):
            for j in range(0, self.map_image.shape[0], sub_image_size):
                sub_image = self.map_image[i:i+sub_image_size,j:j+sub_image_size]
                sub_images.append(sub_image)

        return sub_images




if __name__ == '__main__':

    image_partition_reader = ImagePartitionReader('images/main_image.png')
    images = image_partition_reader.get_sub_images(sub_image_size=300)
    counter = 0

    
    for image in images:
        cv.imshow('test', image)
        cv.waitKey(300)
        cv.imwrite(f'./out/img_{counter}.jpg', image)
        counter += 1    