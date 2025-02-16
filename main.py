import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector=mp.solutions.hands.Hands()
drawing_utils=mp.solutions.drawing_utils
screen_width,screen_height =pyautogui.size()
index_y=0
p1=1
p2=5
while(True):
    _,frame= cap.read()
    frame=cv2.flip(frame,1)
    frame_hight,frame_width,_=frame.shape
    rgb_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output=hand_detector.process(rgb_frame)
    hands=output.multi_hand_landmarks
    if (hands):
        for hand in hands:
            drawing_utils.draw_landmarks(frame,hand)
            landmaks=hand.landmark
            for id,landmak in enumerate(landmaks):
                x=int (landmak.x*frame_width)
                y=int (landmak.y*frame_hight)
                
                if id==8:#move
                    cv2.circle(img=frame,center=(x,y),radius=15,color=(0,225,225),thickness=2)
                    index_x=screen_width/frame_width*x
                    index_y=screen_height/frame_hight*y
                    pyautogui.moveTo(index_x,index_y)

                if id==4:#click
                    cv2.circle(img=frame,center=(x,y),radius=15,color=(0,225,225),thickness=2)
                    thumb_x=screen_width/frame_width*x
                    thumb_y=screen_height/frame_hight*y
                    #rint('outside',abs(index_y-thumb_y))
                    if abs(index_y-thumb_y)<20:
                        pyautogui.click()
                        pyautogui.sleep(1)

                if id==12:#scroll down
                    cv2.circle(img=frame,center=(x,y),radius=15,color=(0,225,225),thickness=2)
                    #cv2.circle(img=frame,center=(x,y),radius=15,color=(0,225,225))
                    ring_x=screen_width/frame_width*x
                    ring_y=screen_height/frame_hight*y
                    print('outside 1',abs(index_y-ring_y))
                    if abs(index_y-ring_y)>200:
                        pyautogui.scroll(-200)
                
                if id==16:#scrool up
                    cv2.circle(img=frame,center=(x,y),radius=15,color=(0,225,225))
                    small_x=screen_width/frame_width*x
                    small_y=screen_height/frame_hight*y
                    #print('outside 1',abs(thumb_x-small_y))
                    if abs(thumb_y-small_y)<30:
                       pyautogui.scroll(200)
                 

    cv2.imshow("virtual mouse",frame)
    cv2.waitKey(1)