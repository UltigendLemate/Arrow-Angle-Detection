import cv2 
import numpy as np

img = cv2.imread("pic.jpg",cv2.IMREAD_COLOR)
cv2.line(img,(0,10),(800,350),(0,0,0),50)
pts = np.array([[23,45],[566,78],[597,423],[690,700],[800,10]])
cv2.polylines(img,[pts],True,(0,255,0),15)
font= cv2.FONT_HERSHEY_SIMPLEX
str="Hello, I am testing"
cv2.putText(img,str,(10,700),font,0.5,(0,255,0),2,cv2.LINE_AA)

#image showing
cv2.imshow("frame",img)
cv2.waitKey(0)
cv2.destroyAllWindows()