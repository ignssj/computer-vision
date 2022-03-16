import numpy as np
import cv2

def draw_circle (event,x,y,flags,params):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),3)
cv2.namedWindow(winname='task')
cv2.setMouseCallback('task',draw_circle)

img = cv2.imread('/home/wanakin/DATA/bricks.jpg')
while True:
    cv2.imshow('task',img)
    if cv2.waitKey(20) & 0xFF == 27:
        break
cv2.destroyAllWindows()
