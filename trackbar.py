import cv2
import numpy as np
img=np.zeros((300,512,3), np.uint8)
cv2.namedWindow('image')

def glider(x):
    print(x)


cv2.createTrackbar('B','image', 0, 255, glider)
cv2.createTrackbar('G', 'image', 0, 255, glider)
cv2.createTrackbar('R', 'image', 0, 255, glider)
switch = '0 : OFF\n 1 : ON'
cv2.createTrackbar(switch, 'image', 0, 1, glider)




while(1):
    cv2.imshow('image', img)
    k=cv2.waitKey(1) & 0xFF
    if k==27:
        break
    b=cv2.getTrackbarPos('B','image')
    g=cv2.getTrackbarPos('G','image')
    r=cv2.getTrackbarPos('R','image')
    s=cv2.getTrackbarPos(switch,'image')
    if s == 0:
        img[:]=[0]
    else:
        img[:]= [b ,g ,r]

cv2.destroyAllWindows()

