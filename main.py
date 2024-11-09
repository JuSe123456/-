import cv2
import numpy as np
import pyautogui
import os
import math
import time
# 截图
# 坐标：(0,0)->(x=569, y=1069)
# pyautogui.screenshot("jump.png",(0,0,569,1069))
path = r'E:\Niu\OpenCV\jump.png'


ls = []

def mousePoint(event,x,y,flags,params):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),2,(0,0,255),cv2.FILLED)
        ls.append([x,y])
        # print(ls)
        # if len(ls) != 0 :
        #     cv2.line( img , tuple(ls[len(ls) - 2] ) , (x,y) , (0,0,255) , 2)

def countline():
    return round(math.sqrt((ls[0][0] - ls[1][0]) ** 2 + (ls[0][1] - ls[1][1])) , 3)
    
def work(dis):
    pyautogui.moveTo(500,500)
    pyautogui.mouseDown(button='left')
    time.sleep(dis/392)
    print(dis/392)
    pyautogui.mouseUp(button='left')
while True:
    # cv2.imread(img)
    img = cv2.imread(path)
    cv2.imshow('img',img)
    cv2.setMouseCallback('img' , mousePoint)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        pyautogui.screenshot("jump.png",(0,0,569,1069))
        ls = []
        cv2.imshow('img',img)
    if len(ls) == 2:
        work(countline())
        print(countline())
        ls = []


