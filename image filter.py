from typing import get_args
import cv2
import numpy as np

#thresholding
img = cv2.imread('bookpage.jpg')
retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
grayscaled = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)
th = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 115, 1)
th1 = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


#image show
# cv2.imshow('original',img)
cv2.imshow('mean',th)
cv2.imshow('gaussian',th1)
# cv2.imshow('gray',threshold2)
# cv2.imshow('graysc',grayscaled)
# cv2.imshow('threshold',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()