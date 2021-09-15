# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 17:00:31 2021

@author: Tanaya Palandurkar
"""

import numpy
import cv2

img = cv2.imread("messi5.jpg")
img2 = cv2.imread("opencv-logo.png")

print(img.shape)
print(img2.shape)

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

print(img.shape)
print(img2.shape)

# dst = cv2.add(img2, img);

dst = cv2.addWeighted(img, 0.1, img2, 0.1, 0)

cv2.imshow("imgae", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()
