import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import time


class boxs:
    def __init__(self,pos,width,height,value):
        self.pos = pos
        self.width = width
        self.height = height
        self.value = value


    def draw(self,img):
        cv.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(0, 51, 0), cv.FILLED)
        cv.rectangle(img,self.pos,(self.pos[0]+self.width,self.pos[1]+self.height),(0,0,128),3)
        cv.putText(img,self.value, (self.pos[0] + 40, self.pos[1] + 60), cv.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)



    def clkbox(self,x,y):
        # x1<x<x1+width
        if self.pos[0]<x<self.pos[0]+self.width and self.pos[1]<y<self.pos[1]+self.height:
            cv.rectangle(img, self.pos, (self.pos[0] + self.width, self.pos[1] + self.height), (255,0,0),
                          cv.FILLED)
            cv.putText(img,self.value, (self.pos[0] + 40, self.pos[1] + 60), cv.FONT_HERSHEY_PLAIN, 2, (255,0,255), 2)
            return True
        else :
            return False

cam = cv.VideoCapture(0)
cam.set(3,1280)
cam.set(4,720)
detecter = HandDetector(detectionCon=0.8,maxHands=1)
box1=boxs((700,200),100,100,"5")

values=[["7","8","9","<"],["4","5","6","/"],["1","2","3","*"],["+","0","-","="]]

equation=''


boxlist=[]
for i in range (4):
    for j in range(4):
        xpos=i*100+850
        ypos=j*100+150
        boxlist.append(boxs((xpos,ypos),100,100,values[j][i]))

while True:
    _,img = cam.read()
    img = cv.flip(img,1)
    hands,img = detecter.findHands(img,flipType=False)
    # box1.draw(img)
    cv.rectangle(img, (850,70), (850+400,70+100), (0,0,0), cv.FILLED)
    cv.rectangle(img, (850,70), (850+400,70+100), (0,0,128), 3)
    cv.rectangle(img, (850, 600), (850 + 400, 70 + 100), (204,153,255), cv.FILLED)
    cv.rectangle(img, (850, 600), (850 + 400, 70 + 100), (0,0,128), 3)
    cv.rectangle(img, (395,0), (760, 45), (0,51,0), cv.FILLED)
    cv.rectangle(img, (395,0), (760, 45), (0, 128, 0), 3)
    cv.putText(img,'$BhaskarReddy007(A.I)', (860,585), cv.FONT_HERSHEY_PLAIN, 2, (0,0,0), 2)

    for boxs in boxlist:
        boxs.draw(img)
    if hands:
        lmList = hands[0]['lmList']
        p1,p2,_=lmList[8]
        p3,p4,_=lmList[12]
        length,_,img = detecter.findDistance((p1,p2),(p3,p4), img)
        # print(length)
        x,y,_=lmList[8]
        if length<50:
            for i,boxs in enumerate(boxlist):
                if boxs.clkbox(x,y):
                    myval=values[int(i%4)][int(i/4)]
                    if myval=='=':
                        equation=str(eval(equation))
                    elif myval=='<':
                        equation=equation[:-1]
                    elif len(equation)>18:
                        equation='syntax error'
                    else:
                        equation+=myval
                    time.sleep(0.2)



    cv.putText(img,equation, (860,120), cv.FONT_HERSHEY_PLAIN, 2, (255,255,255), 2)
    cv.putText(img,"VIRTUAL CALCULATOR", (400, 30), cv.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)
    # cv.putText(img, "__________________", (400, 33), cv.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)




    cv.imshow("BHASKAR_REDDY_007------>Project",img)
    cv.waitKey(1)