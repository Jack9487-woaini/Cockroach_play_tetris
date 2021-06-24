###### tags: `1092LSA`

# 如何讓家裡的~~小寵物~~及主人有遊戲可以玩

![](https://i.imgur.com/905yxjH.png)

- 開會過程:

![](https://i.imgur.com/t2Tlrx4.png)



    
- 工作日誌:
    - 準備過程中，小強越獄了。
        - 最後在書堆裡面找到牠
    - 準備過程中，編譯 OpenCv:
        - 編譯到早上五點，還不能用，沒關係。我抱著破釜成舟的心，打了 sudo pip3 install opencv-contrib-python ，睡了一覺起來，發現終於可以用。 
    - 遊玩過程中，沒有任何一隻小強受到物理性傷害，只有被囚禁。
    - 打字過程中，小強被一群螞蟻，馬上進行救援及清理螞蟻的動作。
    - 打字過程中，救援及清理完畢，避免了一場悲劇的發生，幫自己鼓掌👏，耶🎉。
- 工作分配:
    - 遊戲、硬軟體搭建: 科科
    - 辨識追蹤、霸凌小強: 愛捷克草
## 需準備器材
- webcam x1
- 樹梅派 4 x1
- 小寵物 x1
- 容器(透明較佳) x1
- 主人 x1
## 需準備的工具
### 遊戲
Any Game
> 此 project 以 Tetris 為示範

### OpenCV
我們使用了 OpenCV 擴充套件中的目標追蹤
我們所選用的目標追蹤為 CSRT。
只要框出我們小寵物的位置， OpenCV 就會幫忙追蹤了，超讚的。

### 樹莓派
#### 安裝套件及過程心境
![](https://i.imgur.com/NmuxGfd.png)
![](https://i.imgur.com/Bpmv2I6.png)


- ```sudo apt-get install build-essential cmake git pkg-config libgtk-3-dev libavcodec-dev libavformat-dev libswscale-dev libv4l-dev libxvidcore-dev libx264-dev libjpeg-dev libpng-dev libtiff-dev gfortran openexr libatlas-base-dev python3-dev python3-numpy libtbb2 libtbb-dev ```
- ```sudo pip3 install opencv-contrib-python```記得一定要加 **sudo**，不然會跳出 error。然後我就去編譯 OpenCv ，編譯了一個晚上還不能用，哭阿。
    - 在樹莓派上安裝此套件可能需要將近**五小時**，建議睡前安裝
- ```sudo pip3 install pyautogui``` 模擬鍵盤輸入
- ```sudo pip3 install keyboard``` 模擬鍵盤輸入-備用方案
- ```sudo pip3 install pygame```
- ```sudo apt install libatlas-base-dev```
- ```sudo pip3 install tensorflow-2.3.0-cp37-cp37m-linux_armv7l.whl```
- ```sudo pip3 install keras```
:::info
如果 tensorflow 無法安裝，請[**點擊這裡**](https://github.com/lhelontra/tensorflow-on-arm/releases)，
並下載 tensorflow-2.3.0-cp37-none-linux_armv7l.whl
然後執行 `sudo pip3 install tensorflow-2.3.0-cp37-none-linux_armv7l.whl`
- 若出現 wrapt 的相關 error
    - 請參考[**這篇文章**](https://raspberrypi.stackexchange.com/questions/117231/cannot-uninstall-wrapt-1-10-11)
- 恭喜你應該就會成功了
:::

## 操作說明

### 小寵物部分
:::info
**容器**
![](https://i.imgur.com/YWo8BSt.jpg)

:::

:::info
請搭配 `track_cockroach.py` 跟 `Tetris.py` 使用
:::
- 請開兩個 Terminal，分別執行 `track_cockroach.py` 跟 `Tetris.py`
    - 建議先執行 `track_cockroach.py`
    - 執行後會出現一個視窗請自行框出小寵物的位置
    - 框出小寵物之後，按 `Enter` 即可自動追蹤小寵物
    - 如果失敗請重來一次。
    - 如下圖把小寵物框起來
        ![](https://i.imgur.com/gwh6D2B.jpg)
    - 成功框起來後按enter，會出現新視窗，開始追蹤小寵物。
        ![](https://i.imgur.com/mK0Uyup.jpg)

- 兩個程式開始執行時，請一定要記得選取到遊戲視窗，不然會沒反應喔。

:::info
**Opencv tracker**
我們所使用的函數是 **CSRT** ，它可以在 fps 較低時，保持良好的精準度。
:::
:::info
**容器範圍**
可以依照個人需求
更改條件式中 y 座標的界線
可以先執行 `track_cockroach.py`，框出目標後，視窗的左上方會出現對應的座標值，方便調整。
```python=
if y >= 90 and y <=157:
    pyautogui.keyDown('w')
    #keyboard.press_and_release('w') 
    #keyboard.press_and_release('up') 
    cv2.putText(frame, "direction : " + "up", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

elif y >= 158 and y <= 224:
    pyautogui.keyDown('a')
    #keyboard.press_and_release('a') 
    #keyboard.press_and_release('left') 
    cv2.putText(frame, "direction : " + "left", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);

elif y >= 225 and y <= 292:
    pyautogui.keyDown('d')
    #keyboard.press_and_release('d')
    #keyboard.press_and_release('right') 
    cv2.putText(frame, "direction : " + "right", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
elif y >= 293 and y <= 360:
    #keyboard.press_and_release('up')
    #m_pos = m.position()
    #m.click(m_pos[0],m_pos[1],2)
    pos = pyautogui.position()
    pyautogui.mouseDown(button='right')
    cv2.putText(frame, "direction : " + "down", (100,90), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (50,170,50), 2);
```
由於每位主人的裝小寵物的容器大小不一，所以請自行劃分按鍵區域
此 project 是利用 y 座標把容器切成四個區域
根據小寵物的位置，模擬對應的鍵盤事件。
:::


## 主人部分
使用圖像辨識的模型，來偵測不同的姿勢，藉此遊玩遊戲。

### Teachable Mechine - Google 
訓練圖像辨識的模型，我們謝謝谷哥大大，提供這麼棒的服務。
![](https://i.imgur.com/1shGhbq.png)

- [Teachable Mechine](https://teachablemachine.withgoogle.com/)

![](https://i.imgur.com/1ur4jLx.png)
- 進到網站請點選，開始使用。
- 右下角可以調整語言很貼心。


![](https://i.imgur.com/iVwBmz9.png)
- 請選擇左邊的圖片專案，給他點下去。


![](https://i.imgur.com/vHBHI3s.png)
- 請選擇左邊的標準圖像模型，給他點下去。


![](https://i.imgur.com/Es9mO52.png)
- 這裡可以新增類別，我這裡是創建5個( up 、 down 、 left 、 right 、 nothing )。


![](https://i.imgur.com/0cU0tqc.png)
- 可以上傳圖片。


![](https://i.imgur.com/zGFUpSI.png)
- 也可以使用 webcam 來拍照。 


![](https://i.imgur.com/VaDlvDh.png)
- 中間訓練的部分，可以按進階，調整參數。


![](https://i.imgur.com/KpLR8h1.png)
- 模型訓練中。


![](https://i.imgur.com/d0Bm0qS.png)


![](https://i.imgur.com/7OuPrJu.png)
- 這邊可以直接用 webcam ，開始測試模型訓練準不準確了。
- 要匯出模型，請按匯出模型按鈕。


![](https://i.imgur.com/6PHHPDx.png)
- 請選擇中間的 tensorflow


![](https://i.imgur.com/v4goEGM.png)
- 類型請選 **keras** 後，再按下載模型。
- 之後會開始下載模型的壓縮檔，請把解壓縮後的檔案，放到 track_pose.py 的同一個資料夾底下
- 就可以執行我們的 track_pose.py

## 成品照
![](https://i.imgur.com/5BFScOc.jpg)

## Demo 影片
記得幫我按讚留言，加分享，開啟小鈴鐺，謝謝各位的收看。
- [小強](https://www.youtube.com/watch?v=tNOXoLb93ko)
- [主人]()
##
![](https://i.imgur.com/jtSzEwj.png)


## 未來展望
- 希望可以達成跟寵物一起玩遊戲，排解防疫期間的孤獨感，避免防疫期間所產生的心理問題。
- 還可以讓小寵物進行遊戲實況，讓小寵物賺自己的飼料費。
- 使主人跟小寵物一起遊玩遊戲。
## 參考資料
- [pygame 迷宮](https://github.com/Wonz5130/Maze_AI)
- [pygame Tetris](https://levelup.gitconnected.com/writing-tetris-in-python-2a16bddb5318)
- [opencv tracking 技術 - 1](https://www.gushiciku.cn/dc_tw/109373229)
- [opencv tracking 技術 - 2](https://blog.csdn.net/LuohenYJ/article/details/89029816)
- [opencv tracking 技術 - 3](https://www.pyimagesearch.com/2018/07/30/opencv-object-tracking/)
- [強制刪除 wrapt](https://raspberrypi.stackexchange.com/questions/117231/cannot-uninstall-wrapt-1-10-11)
- [圖像辨識模型](https://teachablemachine.withgoogle.com/)












