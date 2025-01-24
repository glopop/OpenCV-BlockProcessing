import numpy as np
import cv2 # pip install opencv-python
from skimage import io # pip install scikit-image
import matplotlib.pyplot as plt

# loading image as numpy array
img = io.imread('https://t4.ftcdn.net/jpg/07/18/12/87/360_F_718128776_nJReWqPkf5qF4Y5na8ZqGWAbdCJTpczZ.jpg')

# block size, can try with 16 as well fro example, and it displays much more pixelated
block_size = 8

# image dimensions & check they can be divided by the block size
height, width, channels = img.shape
height -= height % block_size
width -= width % block_size

# empty array for the processed image
processed_img = np.zeros_like(img)

# process each block
for y in range(0, height, block_size):
    for x in range(0, width, block_size):
        block = img[y:y+block_size, x:x+block_size]

        # average color for the block
        avg_color = block.mean(axis=(0, 1), dtype=int)

        # give the average color to the block in the processed image
        processed_img[y:y+block_size, x:x+block_size] = avg_color

# saving the proecssed image
cv2.imwrite('img.jpg', cv2.cvtColor(processed_img))

print("imaged saved as image.jpg.")

