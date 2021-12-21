import cv2 as cv
import mediapipe as mp
import numpy as np
import time

class PoseDetector():
    def __init__(self):
        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose()
    
    def showPose(self, frame, draw=True, width=1000, height=700):
            self.width = width
            self.height = height
            self.dim = (self.width, self.height)
            
            frame = cv.resize(frame, self.dim)
            frameRGB = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            
            results = self.pose.process(frameRGB)

            self.poseList = []

            if results.pose_landmarks:
                
                # if(draw):
                    
                for id, lm in enumerate(results.pose_landmarks.landmark):
                    cx, cy = int(lm.x*width), int(lm.y*height)
                    if draw:
                        self.mpDraw.draw_landmarks(frame, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)
                        cv.circle(frame, (cx, cy), 10, (255, 255, 255), cv.FILLED)
                    self.poseList.append([id, cx, cy])
            return frame

    

def main(video_file, pos = 5):

    video = cv.VideoCapture(video_file)
    
    if not video.isOpened():
        print("can't read the video, please check the location")
        exit(0)

    pTime = 0
    pDetector = PoseDetector()
    
    while (True):
        
        ret , frame = video.read()
        
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        if ret:
            cv.putText(frame, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 3)
            frame = pDetector.showPose(frame, False)
            print(pDetector.poseList[pos])
            cv.imshow(str(video_file), frame)
            if cv.waitKey(25) & 0xFF == ord('q'):
                break
        else:
            break

    video.release()
    cv.destroyAllWindows()
    

if __name__ == '__main__':
    main("Pose Estimation/static/4.mp4" , 10)