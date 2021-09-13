# -*- coding: utf-8 -*-
"""
Created on Fri Sep  3 19:03:20 2021

@author: Tanaya Palandurkar
"""

import cv2
import numpy as np

img1 = np.zeros((500,500,3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = np.zeros((500,500,3), np.uint8)
img2 = cv2.rectangle(img2, (0, 0), (250, 500), (255, 255, 255), -1)

bitAND = cv2.bitwise_and(img1, img2)
cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow("img3", bitAND)

cv2.waitKey(0)
cv2.destroyAllWindows