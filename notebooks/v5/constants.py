import os

############ DATASET INFORMATION
CLASSES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]

CLASS_NUMBER = len(CLASSES)

# Nos aseguramos que son string
CLASSES =[str(item) for item in CLASSES]


CLASS_DICTIONARY = {}
for idx, clas in enumerate(CLASSES):
    CLASS_DICTIONARY[clas] = idx



#################################################################################
# DATASETS
#################################################################################


########################################
# Image Dataset

# Path to root image folders
DATASETS_ROOT_FOLDER = "../../datasets/"
# DATASETS_ROOT_FOLDER = os.path.abspath(DATASETS_ROOT_FOLDER) + os.sep

########################################
# CSV dataset

# Path to csv-dataset files
CSV_FOLDER = "../../csv/"
#CSV_FOLDER = os.path.abspath(CSV_FOLDER) + os.sep

# csv-dataset file names
TRAIN_CSV = "mnist_train.csv"
TEST_CSV = "mnist_test.csv"
VALIDATION_CSV = "mnist_val.csv"


#################################################################################
# MODEL
#################################################################################


########################################
# Model and weights defined together

# Path to the model+weights of the model
MODEL_PATH = "../../models/v5"
MODEL_PATH = "/home/manuel/Escritorio/Alba/Animal_Recognition_Neural_Network-master/models/v5/test_model"

########################################
# Path to folder where to save the model
 #MODEL_SAVE_FOLDER = "C:/Users/albam/OneDrive - UNIVERSIDAD DE HUELVA/2. Universidad/Proyects/2. Animal Recognition/models/v4/"
MODEL_SAVE_FOLDER = "../../models/v5/"
MODEL_SAVE_FOLDER = os.path.abspath(MODEL_SAVE_FOLDER) + os.sep




#################################################################################
# TRAIN
#################################################################################

SHUFFLE = None

BATCH_NUMBER = 32

# The number of epochs is repeated during the training_loops_Dataset_renewal
TRAINING_LOOPS_DATASETS_RENEWAL = 3
EPOCHS = 3



###################################################
# Size/shape of images (when resized)

IMG_WIDTH = 28
IMG_HEIGHT = 28
N_CHANNELS = 1


#################################################################################
# Lists

IMG_EXTENSIONS = ['jpg', 'JPG', 'png', 'PNG']

