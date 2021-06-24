import cv2
import sys
import keyboard
from pymouse import PyMouse
import pyautogui
def target_tracking(tracker):
    # Read video
    video = cv2.VideoCapture(0)
    m = PyMouse()     
    # Exit if video not opened.
    if not video.isOpened():
        print("Could not open video")
        sys.exit()
 
    # Read first frame.
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
    
    # Define an initial bounding box
    bbox = (287, 23, 86, 320)
 
    # Uncomment the line below to select a different bounding box
    bbox = cv2.selectROI(frame, False)
 
    # Initialize tracker with first frame and bounding box
    ok = tracker.init(frame, bbox)
    count = 0
    x = 0
    y = 0
    while True:
        # Read a new frame
        ok, frame = video.read()
        if not ok:
            break
        
        # Start timer
        timer = cv2.getTickCount()
 
        # Update tracker
        ok, bbox = tracker.update(frame)
 
        # Calculate Frames per second (FPS)
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
 
        # Draw bounding box
        if ok:
            # Tracking success
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # Tracking failure
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        cv2.putText(frame, "direction : " , (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        if count == 0:
            x = int(bbox[0])
            y = int(bbox[1])
        if count == 3:
            
            y = int(bbox[1])
            if y >= 90 and y <=157:
                pyautogui.press('up')
                #keyboard.press_and_release('w') 
                #keyboard.press_and_release('up') 
                cv2.putText(frame, "direction : " + "up", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
                
            elif y >= 158 and y <= 224:
                pyautogui.press('left')
                #keyboard.press_and_release('a') 
                #keyboard.press_and_release('left') 
                cv2.putText(frame, "direction : " + "left", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
                
            elif y >= 225 and y <= 292:
                pyautogui.press('right')
                #keyboard.press_and_release('d')
                #keyboard.press_and_release('right') 
                cv2.putText(frame, "direction : " + "right", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            elif y >= 293 and y <= 360:
                pyautogui.press('up')
                #keyboard.press_and_release('up')
                #m_pos = m.position()
                #m.click(m_pos[0],m_pos[1],2)
                #pos = pyautogui.position()
                #pyautogui.mouseDown(button='right')
                cv2.putText(frame, "direction : " + "down", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
                
            count = 0
        if count == -3:
            # tmpx = x - int(bbox[0])
            # tmpy = y - int(bbox[1])
            tmpx1 = 0 + int(bbox[0])
            tmpy1 = 0 + int(bbox[1])
            tmpx2 = 480 - int(bbox[0])
            tmpy2 = 480 - int(bbox[1])
            winx = [0,0]
            winy = [0,0]
            if abs(tmpx1) < abs(tmpx2):
                winx[1] = abs(tmpx1)
            else :
                winx[0] = 1
                winx[1] = abs(tmpx2)
                
            if abs(tmpy1) < abs(tmpy2):
                winy[1]  = abs(tmpy1)
            else :
                winy[0] = 1
                winy[1]  = abs(tmpy2)
            
            
            
#             if winx[1] > winy[1] and winx[0] == 0 :
#                 keyboard.press_and_release('left') 
#                 cv2.putText(frame, "direction : " + "left", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
#             elif winx[1] > winy[1] and winx[0] == 1 :
#                 keyboard.press_and_release('right') 
#                 cv2.putText(frame, "direction : " + "right", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
#             if winy[1] > winx[1] and winy[0] == 0  :
#                 keyboard.press_and_release('up') 
#                 cv2.putText(frame, "direction : " + "up", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
#             elif winy[1] > winx[1] and winy[0] == 1:
#                 keyboard.press_and_release('up') 
#                 cv2.putText(frame, "direction : " + "down", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            # if abs(tmpx) > abs(tmpy) and tmpx > 0 and abs(tmpx) > 5 :
            
                # cv2.putText(frame, "direction : " + "right", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
                
            # if abs(tmpx) > abs(tmpy) and tmpx < 0 and abs(tmpx) > 5:
            
                # cv2.putText(frame, "direction : " + "left", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            # if abs(tmpy) > abs(tmpx) and tmpy > 0 and abs(tmpy) > 10:
            
                # cv2.putText(frame, "direction : " + "up", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            # if abs(tmpy) > abs(tmpx) and tmpy < 0 and abs(tmpy) > 10:
                # cv2.putText(frame, "direction : " + "down", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            count = 0
        count += 1
        # Display tracker type on frame
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
    
        # Display FPS on frame
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        
        cv2.putText(frame, "box : " + str(int(bbox[0]))+","+str(int(bbox[1]))+","+str(int(bbox[2]))+","+str(int(bbox[3])), (100,70), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        
        # Display result
        cv2.imshow("Tracking", frame)
        cv2.resizeWindow("Tracking", 600, 480);
        # Exit if ESC pressed
        k = cv2.waitKey(1) & 0xff
        if k == 27 : 
            break

if __name__ == '__main__' :
 
    # Set up tracker.
    # Instead of MIL, you can also use
 
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
    tracker_type = tracker_types[6]
 
 
    if tracker_type == 'BOOSTING':
        tracker = cv2.legacy.TrackerBoosting_create()
    if tracker_type == 'MIL':
        tracker = cv2.TrackerMIL_create()
    if tracker_type == 'KCF':
        tracker = cv2.legacy.TrackerKCF_create()
    if tracker_type == 'TLD':
        tracker = cv2.legacy.TrackerTLD_create()
    if tracker_type == "CSRT":
        tracker = cv2.legacy.TrackerCSRT_create()
    if tracker_type == 'MEDIANFLOW':
        tracker = cv2.legacy.TrackerMedianFlow_create()
    if tracker_type == "MOSSE":
        tracker = cv2.legacy.TrackerMOSSE_create()
    if tracker_type == 'CSRT':
        tracker = cv2.legacy.TrackerCSRT_create()
        
    target_tracking(tracker)