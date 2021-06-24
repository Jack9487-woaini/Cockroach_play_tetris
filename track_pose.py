import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import pyautogui as pyau
# import keyboard
np.set_printoptions(suppress=True)

# 載入模型
path ="keras_model.h5"
path = path.encode(encoding="utf-8")
model = tensorflow.keras.models.load_model(path)



def cv2_to_pil(img): # 把 opencv 畫面轉給 pil
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


cam = cv2.VideoCapture(0) # 打開攝影機
ret_val, img = cam.read() # 畫面讀取







#turn the image into a numpy array
count = 0

while True:
    # 繼續抓畫面
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    ok, img = cam.read()
    
    pil_img = cv2_to_pil(img)
    image = pil_img
    size = (224, 224)
    # 調整照片大小
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
    # 標準化圖片
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # 把照片放到 array
    data[0] = normalized_image_array
    #print(data[0])
    
    # 讓模型辨識
    prediction = model.predict(data)
    score = prediction.tolist()
    score =[score[0][0],score[0][1],score[0][2],score[0][3],score[0][4]]
    count += 1
    # 看誰機率最高
    if score.index(max(score)) == 0 and count >= 5:
        #keyboard.press_and_release('up')
        #pyau.press('up')
        count = 0
    elif score.index(max(score)) == 1 and count >= 5:
        #keyboard.press_and_release('space')
        #pyau.press('space')
        count = 0
    elif score.index(max(score)) == 2 and count >= 5:
        count = 0
        #keyboard.press_and_release('left')
        #pyau.press('left')
    elif score.index(max(score)) == 3 and count >= 5:
        count = 0
        #keyboard.press_and_release('right')
        #pyau.press('right')
    else:
        pass
    cv2.imshow("Camera", img)
    k = cv2.waitKey(1) & 0xff
    if k == 27 : 
        break
