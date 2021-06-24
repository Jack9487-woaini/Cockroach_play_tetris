import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import pyautogui as pyau
# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
path ="keras_model.h5"
path = path.encode(encoding="utf-8")
model = tensorflow.keras.models.load_model(path)

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.



def cv2_to_pil(img): #Since you want to be able to use Pillow (PIL)
    return Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))


cam = cv2.VideoCapture(0) #Define the camera, 0 is which camera, if you have more than 1
ret_val, img = cam.read() #cam.read() returns ret (0/1 if the camera is working) and img, 
#the actual image of the camera in a numpy array

#0 to X milliseconds to stop for a certain amount of time.

 #convert the image to PIL so you can use it that way.
# Replace this with the path to your image


#resize the image to a 224x224 with the same strategy as in TM2:
#resizing the image to be at least 224x224 and then cropping from the center



#turn the image into a numpy array
count = 0

while True:
    # 繼續抓畫面
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    ok, img = cam.read()
    # display the resized image
    pil_img = cv2_to_pil(img)
    image = pil_img
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)
    image_array = np.asarray(image)
# Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array
    #print(data[0])
    # run the inference
    prediction = model.predict(data)
    score = prediction.tolist()
    score =[score[0][0],score[0][1],score[0][2],score[0][3],score[0][4]]
    count += 1
    if score.index(max(score)) == 0 and count >= 5:
        
        #pyau.press('up')
        count = 0
    elif score.index(max(score)) == 1 and count >= 5:
        
        #pyau.press('space')
        count = 0
    elif score.index(max(score)) == 2 and count >= 5:
        count = 0
        #pyau.press('left')
    elif score.index(max(score)) == 3 and count >= 5:
        count = 0
        #pyau.press('right')
    else:
        pass
    cv2.imshow("Camera", img)
    k = cv2.waitKey(1) & 0xff
    if k == 27 : 
        break