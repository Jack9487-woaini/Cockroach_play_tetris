import cv2
import sys
import pyautogui
#import keyboard 鍵盤備用方案
def target_tracking(tracker):
    # 0 會抓第一台攝影機 ，如果是放影片路徑，就會去抓影片。
    video = cv2.VideoCapture(0)
    m = PyMouse()     
    # 檢查攝影機有沒有啟動
    if not video.isOpened():
        print("Could not open video")
        sys.exit()
 
    # 抓影片的第一幀
    ok, frame = video.read()
    if not ok:
        print('Cannot read video file')
        sys.exit()
 
    # Opencv 會跑出一個視窗，讓你去框出你要的區塊
    bbox = cv2.selectROI(frame, False)
 
    # 初始化 tracker ，bbox 剛框出的區塊，frame 第一幀
    ok = tracker.init(frame, bbox)
    count = 0
    x = 0
    y = 0
    while True:
       # 繼續抓畫面
        ok, frame = video.read()
        if not ok:
            break
        
        # 計算時間
        timer = cv2.getTickCount()
 
       # 讓tracker 去抓現在這一幀的畫面
        ok, bbox = tracker.update(frame)
 
        # 計算 fps
        fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
 
        
        if ok:
            # 追蹤成功
            p1 = (int(bbox[0]), int(bbox[1]))
            p2 = (int(bbox[0] + bbox[2]), int(bbox[1] + bbox[3]))
            cv2.rectangle(frame, p1, p2, (255,0,0), 2, 1)
        else :
            # 追蹤失敗
            cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
        # 現在小寵物在的區塊
        cv2.putText(frame, "direction : " , (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        if count == 0:
            x = int(bbox[0])
            y = int(bbox[1])
        if count == 3:
            
            y = int(bbox[1])
            if y >= 90 and y <=157:
                pyautogui.press('up')
                #keyboard.press_and_release('up')
                cv2.putText(frame, "direction : " + "up", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
                
            elif y >= 158 and y <= 224:
                pyautogui.press('left')
                #keyboard.press_and_release('left')
                cv2.putText(frame, "direction : " + "left", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
                
            elif y >= 225 and y <= 292:
                pyautogui.press('right')
                #keyboard.press_and_release('right')
                cv2.putText(frame, "direction : " + "right", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
            elif y >= 293 and y <= 360:
                pyautogui.press('up')
                #keyboard.press_and_release('up')
                cv2.putText(frame, "direction : " + "down", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
                
            count = 0

        count += 1
        # 現在使用的 traker 類型
        cv2.putText(frame, tracker_type + " Tracker", (100,20), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50),2);
    
        # 現在畫面幀數
        cv2.putText(frame, "FPS : " + str(int(fps)), (100,50), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        # 框框的座標，跟高寬。
        cv2.putText(frame, "box : " + str(int(bbox[0]))+","+str(int(bbox[1]))+","+str(int(bbox[2]))+","+str(int(bbox[3])), (100,70), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
        
        # 跑出攝影機畫面的視窗
        cv2.imshow("Tracking", frame)
        cv2.resizeWindow("Tracking", 600, 480);
        # 按 esc 退出視窗
        k = cv2.waitKey(1) & 0xff
        if k == 27 : 
            break

if __name__ == '__main__' :
 
    # Set up tracker.
    # Instead of MIL, you can also use
 
    tracker_types = ['BOOSTING', 'MIL','KCF', 'TLD', 'MEDIANFLOW', 'MOSSE', 'CSRT']
    tracker_type = tracker_types[6] # 選擇使用的追蹤函數 type
 
 
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
