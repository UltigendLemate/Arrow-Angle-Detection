import cv2
import numpy
import matplotlib.pyplot as plt

#image declaration
img= cv2.imread("pic.jpg",cv2.IMREAD_GRAYSCALE)

#IMAGE SHOW BY OPENCV
# cv2.imshow('test',img)
# cv2.waitK ey(0)
# cv2.destroyAllWindows()
# print("h")

#IMAGE SHOW BY MATPLOTLIB
plt.imshow(img,cmap="gray",interpolation="bicubic")
plt.show()