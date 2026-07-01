import cv2
import mediapipe as mp
import numpy as np
import HandTrackingModule as hmt
import os

cap = cv2.VideoCapture(0)
cap.set(3,1280)
cap.set(4,900)

overLayList=[]
colorList = sorted(os.listdir("Colors"))

imgCanvas = np.zeros((720,1280,3),np.uint8)
for c in colorList:
    if c.endswith(".jpg"):
        image = cv2.imread(f"Colors/{c}")
        image = cv2.resize(image,(1280,120))
        overLayList.append(image)
header=overLayList[0]


brushThickness=5
eraserThickness=50
color = (255,0,0)

Detector= hmt.HandDetector()
xp,yp=0,0

while True:
    flag,img = cap.read()
    if not flag:
        break
    img=cv2.flip(img,1)
        
    # img = Detector.findHands(img)
    lmList = Detector.findPosition(img)
    if len(lmList) !=0:
        fingers = Detector.fingersUp()
        x,y = lmList[8][1:]
        
        #drawing mode
        if fingers[1] and not fingers[2]:
            if xp==0 and yp==0:
                xp,yp=x,y
            x=(xp+x)//2
            y=(yp+y)//2
            if np.array_equal(header,overLayList[7]):
                cv2.circle(img,(x,y),50,(0,255,0),cv2.FILLED)
                cv2.line(imgCanvas,(x,y),(xp,yp),color,eraserThickness)
            else:
                cv2.circle(img,(x,y),8,(0,255,0),cv2.FILLED)
                cv2.line(imgCanvas,(x,y),(xp,yp),color,brushThickness)
            xp,yp= x,y
            
        #selection mode
        if fingers[1] and fingers[2]:
            xp,yp=0,0
            cv2.rectangle(img,(x,y),tuple(lmList[12][1:]),(200,10,50),cv2.FILLED)
            if y<120:
                if 122<=x<=242:
                    color=(0,0,255)          # Red
                    header=overLayList[0]
            
                elif 270<=x<=390:
                    color=(0,255,0)          # Green
                    header=overLayList[1]
            
                elif 418<=x<=538:
                    color=(255,0,0)          # Blue
                    header=overLayList[2]
            
                elif 566<=x<=686:
                    color=(203,192,255)      # Pink
                    header=overLayList[3]
            
                elif 714<=x<=834:
                    color=(0,255,255)        # Yellow
                    header=overLayList[4]
            
                elif 862<=x<=982:
                    color=(128,0,128)        # Purple
                    header=overLayList[5]
            
                elif 1010<=x<=1130:
                    color=(255,255,255)            # White
                    header=overLayList[6]
            
                elif 1158<=x<=1278:
                    color=(0,0,0)            # Eraser
                    header=overLayList[7]
    img[0:120,0:1280]=header
    imgGray = cv2.cvtColor(imgCanvas,cv2.COLOR_BGR2GRAY)
    _,imgInv = cv2.threshold(imgGray,50,255,cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv,cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img,imgInv)
    img = cv2.bitwise_or(img,imgCanvas)
    cv2.imshow("Virtual Painter",img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()