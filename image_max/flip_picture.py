import tensorflow as tf
from scipy import ndimage
import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib import image as img
from skimage import transform
from PIL import Image
from skimage.io import imread, imshow

# 随机旋转图片
def random_rotate_image(image_file, num):
    image = imread(image_file)
    rot = transform.rotate(image, angle=num, mode='constant',cval=1)

    img.imsave('./name_15.png', rot,cmap='gray')

def resize_pic(image_file):
    image = imread(image_file)
    dst = transform.resize(image, (20, 20),mode='constant',cval=1,clip=False)
    img.imsave('./name_20.png', dst,cmap='gray')

def random_database():
    '''随机选择几个文件进行旋转或者缩放'''


if __name__ == '__main__':
    # 处理图片，进行20次随机处理，并将处理后的图片保存到输入图片相同的路径下
    # test(cv2.imread("F:/data/test_picture/ding.png"), 30)
    resize_pic('F:/data/test_picture/ding.png')

    # image = cv2.imread('F:/data/test_picture/ding.png')
    # angle = 45
    # imag = rotate_bound(image, angle)
    # cv2.imshow('ww', imag)
    # cv2.waitKey()



