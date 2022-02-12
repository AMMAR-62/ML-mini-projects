import cv2 as cv
import mediapipe as mp
import time


class HandDetector():
    def __init__(self, mode = False, maxHands = 2):
        self.mode = mode
        self.maxHands = maxHands
        # self.detectionConfidence = detectionConfidence
        # self.trackConfidence = trackConfidence

        
        self.mphands = mp.solutions.hands
        self.hands = self.mphands.Hands(mode, maxHands)
        self.mpDraw = mp.solutions.drawing_utils
        
    def findHands(self, img, draw = True):
        imgRGB = cv.cvtColor(img, cv.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)

        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw: 
                    self.mpDraw.draw_landmarks(img, handLms, self.mphands.HAND_CONNECTIONS)
        return img
    
    def findPosition(self, img, handNo, draw = True):
        lmList=[]
        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myHand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)
                lmList.append([id, cx, cy])
                if draw:
                    cv.circle(img, (cx, cy), 15, (255,255,255), cv.FILLED)
        return lmList
        
        


if __name__ == "__main__":
    pTime = 0
    cTime = 0

    cap = cv.VideoCapture(0, cv.CAP_DSHOW)

    detector = HandDetector()

    while True:
        success, img = cap.read()

        img = detector.findHands(img)

        lmList = detector.findPosition(img, 0)
        if len(lmList)!=0:
            print(lmList[4])

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv.putText(img, str(int(fps)), (10, 70), cv.FONT_HERSHEY_PLAIN, 3, (255,0, 255), 3)
        cv.imshow("image", img)
        k = cv.waitKey(1)
        if k == ord("s"):
            cap.release()
            cv.destroyAllWindows()
            break

