import crop_images
import agumenceImages
import classify_images
import myUtils


# Crop images hyperparameters
IMAGES_DIR_BEGGINING = "./images"
CROPPED_IMAGES_DIR = "./cropImages"
CLASS_NAME = "char"

# Agumence images hyperparameters
IMAGES_PATH_RIGHT_BEFOR_AGUMENCE = myUtils.getImagesFolderForAgumence(CROPPED_IMAGES_DIR,CLASS_NAME)
IMAGES_PATH_AFTER_AGUMENCE = "./agumenceImages"

# Classisfication images hyperparameters
INPUT_SHAPE = (65,50,3)
NUMBER_OF_CLASSES = 118
LEARNING_RATE = 0.001
IMAGES_PATH_BEFOR_CLASSIFICATION = IMAGES_PATH_AFTER_AGUMENCE 
CLASSIFICATION_WEIGHT_PATH = "./classification_weights_0.88.hdf5"

def main():
    crop_images.loadModelAndSaveCropImages(IMAGES_DIR_BEGGINING,CROPPED_IMAGES_DIR)
    #agumenceImages.augumence_images(IMAGES_PATH_RIGHT_BEFOR_AGUMENCE,IMAGES_PATH_AFTER_AGUMENCE)
    #classify_images.evaluateModel(IMAGES_PATH_BEFOR_CLASSIFICATION,INPUT_SHAPE,NUMBER_OF_CLASSES,LEARNING_RATE,CLASSIFICATION_WEIGHT_PATH)
    

if __name__ == "__main__":
    main()