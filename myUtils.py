# -*- coding: utf-8 -*-
import os
import shutil

def extractUnecessaryImages(srcPath,desPath):
    folderList = os.listdir(srcPath)
    folderPathList = []
    for folder in folderList:
        folderPathList.append(os.path.join(srcPath,folder))
    for folderPath in folderPathList:
        numberImgInFolder = len(os.listdir(folderPath))
        if numberImgInFolder < 10:
            extractAllImg(folderPath,desPath)

def extractAllImg(srcPath,desPath):
    imagesNameList = os.listdir(srcPath)
    imagePathList = []
    for imageName in imagesNameList:
        imagePath = os.path.join(srcPath,imageName)
        shutil.move(imagePath,desPath)

def delFolder(path):
    folderList = os.listdir(path)
    folderPathList = []
    for folder in folderList:
        folderPathList.append(os.path.join(path,folder))
    for folderPath in folderPathList:
        numberImgInFolder = len(os.listdir(folderPath))
        if numberImgInFolder == 0:
            shutil.rmtree(folderPath)

def getImagesPathList(imageDir):
    imagesPathList = []
    imagesNameList = os.listdir(imageDir)
    for imageName in imagesNameList:
        imagePath = os.path.join(imageDir,imageName)
        imagesPathList.append(imagePath)
    return imagesPathList

def deleteDir(path):
    if dirExisted(path):
        shutil.rmtree(path)
        print("Directory existed, success deleting directory.")

def createDir(path):
    if not dirExisted(path):
        os.makedirs(path)
    print("Successfully creaet new directory.")

def dirExisted(path):
    if os.path.exists(path):
        return True
    return False

def deleteDirIfExistedAndMakeNewDir(path):
    deleteDir(path)
    createDir(path)

def getImagesFolderForAgumence(path,className):
    result= os.path.join(path,"crops")
    result = os.path.join(result,className)
    return result


classNameAndIndicesDict = {0: 'いわき', 1: 'つくば', 2: 'とちぎ', 3: 'なにわ', 4: '一宮', 5: '三河', 6: '三重', 7: '下関', 8: '世田谷', 9: '久留米', 10: '京', 11: '京都', 12: '仙台', 13: '伊豆', 14: '会津', 15: '佐世保', 16: '佐賀', 17: '倉敷', 18: '八戸', 19: '八王子', 20: '函館', 21: '前橋', 22: '北九州', 23: '北見', 24: '千葉', 25: '名古屋', 26: '和歌山', 27: '和泉', 28: '品川', 29: '土浦', 30: '堺', 31: '多摩', 32: '大分', 33: '大宮', 34: '大阪', 35: '奄美', 36: '奈良', 37: '姫路', 38: '宇都宮', 39: '室蘭', 40: '宮城', 41: '宮崎', 42: '富士山', 43: '富山', 44: '尾張小牧', 45: '山口', 46: '山形', 47: '山梨', 48: '岐阜', 49: '岡山', 50: '岡崎', 51: '岩手', 52: '島根', 53: '川口', 54: '川崎', 55: '川越', 56: '帯広', 57: '平泉', 58: '広島', 59: '庄内', 60: '徳島', 61: '愛媛', 62: '成田', 63: '所沢', 64: '新潟', 65: '旭川', 66: '春日井', 67: '春日部', 68: '札幌', 69: '杉並', 70: '松本', 71: '柏', 72: '横浜', 73: '水戸', 74: '沖', 75: '沖縄', 76: '沼津', 77: '浜松', 78: '湘南', 79: '滋賀', 80: '熊本', 81: '熊谷', 82: '盛岡', 83: '相模', 84: '石川', 85: '神戸', 86: '福井', 87: '福山', 88: '福岡', 89: '福島', 90: '秋田', 91: '筑豊', 92: '練馬', 93: '群馬', 94: '習志野', 95: '袖ヶ浦', 96: '諏訪', 97: '豊橋', 98: '豊田', 99: '越谷', 100: '足立', 101: '那須', 102: '郡山', 103: '野田', 104: '金沢', 105: '釧路', 106: '鈴鹿', 107: '長岡', 108: '長崎', 109: '長野', 110: '青森', 111: '静岡', 112: '飛騨', 113: '香川', 114: '高崎', 115: '高知', 116: '鳥取', 117: '鹿児島'} 
def createFullDataset(dictionary,path):
    classPathInDir = os.listdir(path)
    classesList = dictionary.values()
    for className in classesList:
        if className not in classPathInDir:
            os.makedirs(os.path.join(path,className))

def countFile(path,name):
    filePath = os.path.join(path,name)
    fileList = os.listdir(filePath)
    return(len(fileList))

def getImagesNameList(path):
    return os.listdir(path)


predictions = ['湘南', '横浜', '石川', '横浜', '横浜', 'Nothing detected', '相模', '相模', '横浜', '横浜', 'なにわ', '横浜', '横浜', '横浜', '伊豆', '横浜', '名古 屋', '名古屋', '横浜', '横浜', '横浜', '横浜', '横浜', '横浜', '横浜', '品川', '相模', '横浜', 'Nothing detected', 'Nothing detected', '横浜', '横浜', '横浜', '横浜', '三河', '横浜', '新潟', '横浜', '横浜', '新潟', '新潟', '新潟', '静岡', '湘南', '横浜', '筑豊', '横浜', '新潟', '横浜', '多摩', '杉並', '横浜', '新潟', '横浜', '新潟', '横浜', '横浜', '横浜', '横浜', '新潟', '横浜', '横浜', '横浜', '横浜', '相模', '横浜', '横浜', '筑豊', '横浜', '横浜', '相模', '横浜', '横浜', '横浜', '新潟', '横浜', '新潟', '横浜', '新潟', '相模', '名古屋', '横浜', '那須', '杉並', '横浜', '横浜', '横浜', '横浜', '湘南', '横浜', '横浜', '横浜', '横浜', '新潟', '横浜', '相模', '名古屋', '相模', '横浜', '相模', '新潟', '相模', '新潟', '横浜', '横浜', '横浜', '湘南', '横浜', '横浜', '横浜', '横浜', '横浜', '相模', '筑豊', '横浜', '新潟', '横浜', '横浜', '横浜', '新潟', '湘南', '横浜', '郡山', '湘南', '横浜', '横浜', '湘南', '横浜', '湘南', '湘南', '横浜', '川崎', '湘南', '旭川', '横浜', '新潟', '横浜', '横浜', '横浜', '新潟', '横浜', '横浜', '新潟', '新潟', '名古屋', '宇都宮', '横浜', '横浜', '新潟', '横浜', '横浜', '相模', '新潟', '湘南', '横浜', '横浜', '新潟', '横浜', '横浜', '静岡', 'Nothing detected', '横浜', '横浜', '横浜', '新潟', '新潟', '横浜', '横浜', '名古屋', '新潟', '新潟', '横浜', '横浜', '横浜', '相模', '湘南', '横浜', '横浜', '横浜', 'Nothing detected', '湘南', '横浜', '横浜', '横浜', '横浜', '那須', '高知', '横浜', '帯広', '横浜', '新潟', '横浜', '横浜', '横浜', '横浜', '新潟', '足立', '横浜', 'Nothing detected', '愛媛', '横浜', '新潟', '足立', '新潟', '湘南', '京', '川崎', '新潟', '横浜', '横浜', 'Nothing detected', '横浜', '横浜', '横浜', '新潟', '筑豊', 'Nothing detected', '横浜', '新潟', '庄内', '横浜', '横浜', '横浜', '横浜', '横浜', '新潟', '湘南', '新潟', '横浜', '横浜', '湘南', '横浜', '横浜', '横浜', '岐阜', '新潟', '横浜', '名古屋', '湘南', '相模', '横浜', '横浜', '湘南', '横浜', '名古屋', '横浜', ' 相模', '横浜', 'Nothing detected', '横浜', '静岡', '横浜', '横浜', '横浜', '新潟', '横浜', '湘南', '横浜', '横浜', '横浜', '新潟', '横浜', '伊豆', ' 横浜', '横浜', '横浜', '新潟', '横浜', '新潟', '新潟', '湘南', '新潟', '湘南', '横浜', '横浜', '新潟', '静岡', '横浜', '相模', '湘南', '相模', '筑豊', '金沢', '高知', '新潟', '筑豊', '横浜', '相模', '横浜', '相模', '横浜', '新潟', '静岡', '名古屋', '湘南', '新潟', '湘南', '横浜', '新潟', '新潟', '新潟', '横浜', '横浜', '相模', '筑豊', '横浜', '横浜', '名古屋', '横浜', '湘南', '相模', '新潟', '新潟', '横浜', '新潟', '横浜', '横浜', '横浜', '湘 南', 'なにわ', '横浜', '横浜', '新潟', '新潟', '湘南', '横浜', '横浜', '新潟', '横浜', '静岡', '名古屋', '横浜', '横浜', '新潟', '筑豊', '横浜', '横 浜', 'Nothing detected', '静岡', '相模', '横浜', '横浜', '湘南', '沼津', '香川', '横浜', '新潟', '新潟', '新潟', '岡崎', '横浜', '新潟', '新潟', '新 潟', '横浜', '湘南', '名古屋', '横浜', '新潟', '新潟', '横浜', '横浜', '横浜', '新潟', '横浜', '横浜', '横浜', '横浜', '新潟', '相模', '新潟', '新潟', '新潟', '横浜', '新潟', '横浜', '横浜', '筑豊', '横浜', '横浜', '新潟', '横浜', '横浜', '横浜', '湘南', '横浜', '湘南', '横浜', '横浜', '横浜', '横浜', '横浜', '横浜', '新潟', '相模', '横浜', '横浜', '新潟', '三河', '多摩', '横浜', '湘南', 'Nothing detected', '湘南', '横浜', '名古屋', '松本', ' 新潟', '横浜', '横浜', '横浜', '湘南', '新潟', '新潟', '石川', '新潟', '横浜', '横浜', '横浜', '湘南', '横浜', '湘南', '新潟', '新潟', '横浜', '湘南', '湘南', '横浜', '横浜', '横浜', '新潟', '新潟', '鹿児島', '横浜', '横浜', '横浜', '杉並', '新潟', '横浜', '新潟', '新潟', '横浜', '新潟', '横浜']

def countClasses(prediction):
    i = 0
    j = 0
    k = 0
    for predict in prediction:
        if predict == '横浜':
            i+=1
        elif predict == '相模':
            j += 1        
        elif predict == '新潟':
            k += 1
    print(i)
    print(j)
    print(k)

