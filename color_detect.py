import pandas as pd
import cv2
import numpy as np
clicked=False
g=b=r=xpos=ypos=0

def draw_function(event,x,y,flags,param):
    if event==cv2.EVENT_LBUTTONDBLCLK:
        global g,b,r,xpos,ypos,clicked
        print('hiiiiiiii')
        clicked=True
        xpos=x
        ypox=y
        b,g,r=img[y,x]
        b=int(b)
        g-int(g)
        r=int(r)
        colorname=get_color_name(b,g,r)
        c=(int(b),int(g),int(r))
        cv2.rectangle(img, (20, 20), (750, 60), c, -1)
        text = get_color_name(b, g, r) + ' B-' + str(b) + ' G-' + str(g) + ' R-' + str(r)
        cv2.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv2.LINE_AA)
        if (r + g + b >= 600):
            cv2.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv2.LINE_AA)
        cv2.imshow('image', img)




img=cv2.imread('input_cat1.jpg')
cv2.imshow('image',img)
#cv2.namedWindow('image')
cv2.setMouseCallback('image',draw_function)


index=["color","color_name","hex","R","G","B"]
csv=pd.read_csv('colo.csv',names=index,header=None)


def get_color_name(b,g,r):
    minimum=10000
    for i in range(len(csv)):
        d=abs(r-int(csv.loc[i,'R']))+abs(g-int(csv.loc[i,'G']))+abs(b-int(csv.loc[i,'B']))
        if d<=minimum:
            minimum=d
            cname=csv.loc[i,'color_name']
    return cname



if clicked:
        cv2.rectangle(img,(20,20),(750,60),(b,g,r),-1)
        text=get_color_name(b,g,r)+'B-'+b+' G-'+g+' R-'+r
        cv2.putText(img,text,(50,50),2,0.8,(255,255,255),2,cv2.LINE_AA)
        if(r+g+b>=600):
            cv2.putText(img, text,(50,50),2,0.8,(0,0,0),2,cv2.LINE_AA)
        clicked=False
        if cv2.waitKey(1) & 0xFF ==27:
            cv2.destroyAllWindows()

cv2.waitKey(0)
cv2.destroyAllWindows()