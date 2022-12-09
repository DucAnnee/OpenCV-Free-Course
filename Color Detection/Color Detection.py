import cv2 as cv
import numpy as np
import pandas as pd
 
def call_back_function(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global b, g, r, xpos, ypos, clicked
        clicked = True
        xpos = x
        ypos = y
        b,g,r = img[x,y]
        b = int(b)
        g = int(g)
        r = int(r)

def get_Color_Name(R,G,B):
    minimum = 10000
    for i in range(len(index)):
        d = abs(R- int(index.loc[i,"R"])) + abs(G-int(index.loc[i,"G"]))+ abs(B- int(index.loc[i,"B"]))
        if(d<=minimum):
            minimum = d
            cname = index.loc[i,"color_name"]
    return cname
    

img = cv.imread("Sample.jpg")
index = ["color", "color_name", "hex", "R", "G", "B"]
data = pd.read_csv("C:\Users\DUC AN\Documents\GitHub\OpenCV-Free-Course\Color Detection\colors.csv", names=index, header=None)
cv.imshow(img)
cv.namedWindow("Color Detection Window")
cv.setMouseCallback("Color Detection Window",call_back_function)

while(1):
  cv.imshow("Color Detection Window",img)
  if (clicked):
    cv.rectangle(img,(20,20), (750,60), (b,g,r), -1)
    text = get_Color_Name(r,g,b)+'R='+str(r)+'G='+ str(g)+'B='+ str(b)
    cv.putText(img, text,(50,50),2,0.8, (255,255,255),2,cv.LINE_AA)
    if(r+g+b>=600):
       cv.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv.LINE_AA)
    clicked=False
    if cv.waitKey(20) & 0xFF ==27:
      break
cv.destroyAllWindows()