import os
import tensorflow as tf
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, average_precision_score


############ DATASET INFORMATION
# CLASSES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
CLASSES = ["Bear", "Chicken", "Turtle"]

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
'''TRAIN_CSV = "mnist_train.csv"
TEST_CSV = "mnist_test.csv"
VALIDATION_CSV = "mnist_val.csv"'''

TRAIN_CSV = "data_train.csv"
TEST_CSV = "data_test.csv"
VALIDATION_CSV = "data_val.csv"


#################################################################################
# MODEL
#################################################################################


########################################
# Model and weights defined together

# Path to the model+weights of the model
MODEL_PATH = "../../models/v5"
# MODEL_PATH = "/home/manuel/Escritorio/Alba/Animal_Recognition_Neural_Network-master/models/v5/test_model"

########################################
# Path to folder where to save the model
 #MODEL_SAVE_FOLDER = "C:/Users/albam/OneDrive - UNIVERSIDAD DE HUELVA/2. Universidad/Proyects/2. Animal Recognition/models/v4/"
MODEL_SAVE_FOLDER = "../../models/v5/"
MODEL_SAVE_FOLDER = os.path.abspath(MODEL_SAVE_FOLDER) + os.sep




#################################################################################
# TRAIN
#################################################################################

SHUFFLE = True

BATCH_NUMBER = 64

# The number of epochs is repeated during the training_loops_Dataset_renewal
TRAINING_LOOPS_DATASETS_RENEWAL = 3     # Period of dataset renewal
EPOCHS = 9                              # Total / Max number of epochs that are going to be runned
# So training for 9 epochs, and every 3 epochs dataset will be renewed (3 different datasets)

FROM_LOGITS = True
MODEL_PATH = None
MODEL_NAME = "test_model"

LOSS = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=FROM_LOGITS)

METRICAS = ["Accuracy"]     #, "Precision", "Recall", "F1"]

METRICS = [accuracy_score, recall_score, precision_score, f1_score]


###################################################
# Size/shape of images (when resized)

IMG_WIDTH = 128
IMG_HEIGHT = 128
N_CHANNELS = 3


#################################################################################
# Lists

IMG_EXTENSIONS = ['jpg', 'JPG', 'png', 'PNG']

