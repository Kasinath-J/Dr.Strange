import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

def drawline(a,b,c,d):
    cv2.line(img,(a,b),(c,d),(51,92,255),5)


while True:
    sucess, img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            cx4, cy4 = 0,0
            h, w, c = img.shape
            for id,lm in enumerate(handLms.landmark):
                #print(id,lm)
                if id==4 :
                    cx4, cy4 = int(lm.x * w), int(lm.y * h)
                if id==9 :
                    cx,cy = int(lm.x*w), int(lm.y*h)
            if cx4 and cx and cy4 and cy:
                rad = abs(int(((cx4-cx)*2 + (cy4-cy)*2)*0.5))

                cv2.circle(img,(cx,cy),int(0.9*rad),(26,209,255),3)
                cv2.rectangle(img,(cx-rad-10,cy-rad-10),(cx+rad+10,cy+rad+10),(51,92,255),4)

                cv2.circle(img, (cx, cy), int(1.5 * rad), (26, 209, 255), 1)
                cv2.circle(img, (cx, cy), int(1.7 * rad), (26, 209, 255), 1)
                cv2.circle(img, (cx, cy), int(1.75 * rad), (26, 209, 255), 1)
                cv2.circle(img, (cx, cy), int(1.85 * rad), (26, 209, 255), 1)

                rad = rad+40
                drawline(cx, cy - rad, cx + rad, cy)
                drawline(cx + rad, cy, cx, cy + rad)
                drawline(cx, cy + rad, cx - rad, cy)
                drawline(cx - rad, cy, cx, cy - rad)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    # cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow("outImg", img)
    cv2.waitKey(1)