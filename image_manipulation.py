import cv2
import random

img = cv2.imread('assets/forest.jpg')

# Pixel Array
print(img)
print()

# Height, Width, Channels:BGR  
print(img.shape)
print()

""" 2 x 2 Pixel
[
[[0, 0, 0], [255, 255, 255]],
[[0, 0, 0], [255, 255, 255]]
]        
"""

# First row of our img
print(img[0])

# 245th row and 35-100 column of our img
print(img[245][35:100])

# Loop through the first 100 rows and width of the img and randomly change the colors
for i in range(100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randrange(255), random.randrange(255), random.randrange(255)]

tag = img[0:300, 300:900]  
img[400:700, 150:750] = tag      

cv2.imshow('Image', img) 
cv2.waitKey(0)
cv2.destroyAllWindows()