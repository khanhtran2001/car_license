from cv2 import normalize
import torch 
from PIL import Image
import numpy as np
import torch
import albumentations as A
import tensorflow as tf
import tensorflow.keras
from tensorflow.keras.layers import Dense, Activation, Dropout, Flatten 
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras import layers
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras.applications.mobilenet import MobileNet
import myUtils


INPUTSHAPE = (65,50,3)
NUMBEROFCLASSES = 118
LEARNINGRATE = 0.001

IMAGEPATH = "./images/1fe8e009-4594-4be3-b018-a7661161ae00_plate.png"
FOLDERPATH =  "D:/Downloads/Test_dataset/Test_29032022/相模"
WEIGHTPATH = "./weights/classification_weights_0.88.hdf5"

classNameAndIndicesDict = {0: 'いわき', 1: 'つくば', 2: 'とちぎ', 3: 'なにわ', 4: '一宮', 5: '三河', 6: '三重', 7: '下関', 8: '世田谷', 9: '久留米', 10: '京', 11: '京都', 12: '仙台', 13: '伊豆', 14: '会津', 15: '佐世保', 16: '佐賀', 17: '倉敷', 18: '八戸', 19: '八王子', 20: '函館', 21: '前橋', 22: '北九州', 23: '北見', 24: '千葉', 25: '名古屋', 26: '和歌山', 27: '和泉', 28: '品川', 29: '土浦', 30: '堺', 31: '多摩', 32: '大分', 33: '大宮', 34: '大阪', 35: '奄美', 36: '奈良', 37: '姫路', 38: '宇都宮', 39: '室蘭', 40: '宮城', 41: '宮崎', 42: '富士山', 43: '富山', 44: '尾張小牧', 45: '山口', 46: '山形', 47: '山梨', 48: '岐阜', 49: '岡山', 50: '岡崎', 51: '岩手', 52: '島根', 53: '川口', 54: '川崎', 55: '川越', 56: '帯広', 57: '平泉', 58: '広島', 59: '庄内', 60: '徳島', 61: '愛媛', 62: '成田', 63: '所沢', 64: '新潟', 65: '旭川', 66: '春日井', 67: '春日部', 68: '札幌', 69: '杉並', 70: '松本', 71: '柏', 72: '横浜', 73: '水戸', 74: '沖', 75: '沖縄', 76: '沼津', 77: '浜松', 78: '湘南', 79: '滋賀', 80: '熊本', 81: '熊谷', 82: '盛岡', 83: '相模', 84: '石川', 85: '神戸', 86: '福井', 87: '福山', 88: '福岡', 89: '福島', 90: '秋田', 91: '筑豊', 92: '練馬', 93: '群馬', 94: '習志野', 95: '袖ヶ浦', 96: '諏訪', 97: '豊橋', 98: '豊田', 99: '越谷', 100: '足立', 101: '那須', 102: '郡山', 103: '野田', 104: '金沢', 105: '釧路', 106: '鈴鹿', 107: '長岡', 108: '長崎', 109: '長野', 110: '青森', 111: '静岡', 112: '飛騨', 113: '香川', 114: '高崎', 115: '高知', 116: '鳥取', 117: '鹿児島'} 
augMethod = A.Compose([
    # A.ToGray(p = 1),
    # A.RandomBrightnessContrast(brightness_limit=(-0.35,0.1))
])



def cropOneImageToNumpy(imageDir):
    #load model
    model = torch.hub.load("ultralytics/yolov5", 'custom', path="./weights/yolov5_license_plate.pt")
    print("Successfully load model")
    img = Image.open(imageDir).convert('L')
    cropImageAsArray = model(img).crop(save = False)[0]['im']
    return cropImageAsArray


def agumenImage(image):
    image = Image.fromarray(image)
    image_width,image_height = image.size
    box_crop = (image_width*0.1, image_height*0.05, image_width * 0.85, image_height*0.85)
    image = image.crop(box_crop)
    return image 


def normalizeImg(image):
    img = image.resize((50,65))
    img = np.array(img)
    img = img.astype('float64')
    # normalize to the range 0-1    
    img /= 255.0
    img = np.expand_dims(img, axis=0)
    return img

def loadAndCompileModel(inputShape,numberOfClass,learningRate,weightPath):
    input_layer=layers.Input(inputShape)
    model_mobileNet = MobileNet(input_tensor = input_layer, include_top=True, classes=numberOfClass, weights=None)
    optimizerFunction = tf.keras.optimizers.RMSprop(learning_rate=learningRate)
    model_mobileNet.compile(loss='categorical_crossentropy', optimizer=optimizerFunction,metrics=['accuracy'])
    model_mobileNet.load_weights(weightPath) 
    print("Create classification model completed.")
    return model_mobileNet

def predictImage(image,model):
    classes = model.predict(image, batch_size=1)
    predictedClassIndices=np.argmax(classes,axis=1)[0]
    prediction = classNameAndIndicesDict[predictedClassIndices]
    return prediction


def classifyImage(image,inputShape,numberOfClass,learningRate,weightPath):
    model = loadAndCompileModel(inputShape,numberOfClass,learningRate,weightPath)
    prediction = predictImage(image,model)
    return prediction

def predictOneImage(IMAGE_PATH,INPUT_SHAPE,NUMBER_OF_CLASSES,LEARNING_RATE,WEIGHT_PATH):
    try:
        cropImageAsArray = cropOneImageToNumpy(IMAGE_PATH)
        augumenImg = agumenImage(cropImageAsArray)
        augumenImg.save("./test.jpg")
        normalizeImage = normalizeImg(augumenImg)
        prediction = classifyImage(normalizeImage,INPUT_SHAPE,NUMBER_OF_CLASSES,LEARNING_RATE,WEIGHT_PATH)
    except:
        return "Nothing detected"
    return prediction
    

if __name__ == "__main__":
    prediction = predictOneImage(IMAGEPATH,INPUTSHAPE,NUMBEROFCLASSES,LEARNINGRATE,WEIGHTPATH)
    print(prediction)
