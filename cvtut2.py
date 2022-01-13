import cv2 

vid = cv2.VideoCapture(0)
while True:
    ret,frame = vid.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('frame2',gray)


    if cv2.waitKey(1) == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
