import albumentations as A
import cv2
from PIL import Image
import os
import numpy as np
import shutil

augMethod = [
    A.RandomBrightnessContrast(brightness_limit=(-0.3,0.05)),
    A.augmentations.geometric.transforms.Affine (scale=None, translate_percent=(-0.1,0.1), translate_px=None, rotate=None, shear=None, interpolation=1, mask_interpolation=0, cval=0, cval_mask=0, mode=1, fit_output=False, keep_ratio=False, p = 1),
    A.Rotate(limit=(-10,10 ),p = 0.8),
    A.Resize(50,65,always_apply=True, p=1),
]


def getPaddingSize(img):
    imgWidth,imgHeight = img.size
    paddingHeight = int(imgHeight*0.4)
    paddingWidth = int(imgWidth*0.25)
    paddingSize = [paddingWidth,paddingHeight]
    return paddingSize


def addPadding(img):
    paddingSize = getPaddingSize(img)
    paddingWidth = paddingSize[0]
    paddingHeight = paddingSize[1]

    paddingRight = paddingWidth
    paddingLeft = paddingWidth
    paddingTop = paddingHeight
    paddingBottom = paddingHeight

    imgWidth,imgHeight = img.size
    newImgHeight = imgHeight + paddingTop + paddingBottom
    newImgWidth = imgWidth + paddingLeft + paddingRight
    paddingColor = computeBackgroundColor(img)

    imageAfterPadding = Image.new(img.mode, (newImgWidth,newImgHeight), paddingColor)
    imageAfterPadding.paste(img,(paddingLeft,paddingTop))
    return imageAfterPadding


def computeBackgroundColor(img):
    imgWidth,imgHeight = img.size
    mostSeenColor = max(img.getcolors(imgWidth*imgHeight))
    backgroundColor = mostSeenColor[1]
    return backgroundColor



def getImageAreaFromNumpy(img):
    imgWidth = img.shape[1]
    imgHeight = img.shape[0]
    imgArea = imgWidth * imgHeight
    return imgArea



def createCustomAugMethod(img,augumencMethod):
    imgArea = getImageAreaFromNumpy(img)

    if imgArea <= 14000:
        customAugMethod = [ A.Blur(blur_limit=(6,10),p = 1),
                            A.MotionBlur(blur_limit=3, p = 0.3)] 
    elif imgArea <= 16000:
        customAugMethod = [ A.Blur(blur_limit=(5,7),p = 1),
                            A.MotionBlur(blur_limit=3, p = 0.3)]
    elif imgArea <= 19000:
        customAugMethod = [ A.Blur(blur_limit=(14,20),p = 1),
                            A.MotionBlur(blur_limit=3,p = 0.3)]   
    else:
        customAugMethod = [ A.Blur(blur_limit=(18,23),p = 1),
                            A.MotionBlur(blur_limit=3, p = 0.5)]
    # customAugMethod = [A.Defocus(radius=(2,3),alias_blur=(0.15,0.25),p = 1),
    #                     A.MotionBlur(blur_limit=3, p =1)]


    augumencMethod =  customAugMethod + augumencMethod
    customAug = A.Compose(augumencMethod)
    return customAug



def augmence_a_class(class_name,source,des):
    class_path = os.path.join(source,class_name)
    names = os.listdir(class_path)
    j = 0
    for image_name in names:
      image = Image.open(os.path.join(class_path,image_name))
      image = image.convert('RGB')
      #image = image.resize((65,50))
      #add padding to image
      image = addPadding(image)
      #store all agument image in a list
      image = np.array(image)
      customAug = createCustomAugMethod(image,augMethod)
      for i in range(50):
        augumentation = customAug(image = image)
        augument_image = augumentation["image"]
        im = Image.fromarray(augument_image)
        im.save(f"{des}/{class_name}/{image_name.split('.')[0]}-aug-{i}.jpeg")
        j+=1
    print(j)



def resizeTestImages(imgFolderPath,des):
    imagesName = os.listdir(imgFolderPath)
    aug = A.Compose([A.Resize(50,65,always_apply=True, p=1),])
    for imgName in imagesName:
        imgPath = os.path.join(imgFolderPath,imgName)
        image = Image.open(imgPath)
        image = np.array(image)
        augmece = aug(image = image)
        augmeceImg = augmece["image"]
        im = Image.fromarray(augmeceImg)
        im.save(f"{des}/{imgName}")
        

def makeValidFolder(src,des):
    if os.path.exists(des):
        shutil.rmtree(des)
    os.mkdir(des)

    classNames = os.listdir(src)
    for className in classNames:
        os.mkdir(f"{des}/{className}")


def augumenceAll(src,des):
    classNames = os.listdir(src)
    for className in classNames:
        classPath = os.path.join(src,className)
        augmence_a_class(className,src,des)
        


def main():
    #augmence_a_class("湘南","./car_lience_crop","./testImgFolder")
    #resizeTestImages("./cropImages","./testImgAfterResize")
    "横浜""湘南"
    makeValidFolder("./car_lience_crop","./testImgFolder")
    augumenceAll("./car_lience_crop","./testImgFolder")
    #augmence_a_class("横浜","./car_lience_crop","./wrong_image01")



if __name__ == "__main__":
    main()





