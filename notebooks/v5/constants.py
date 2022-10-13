import os

#################################################################################
# IMAGE DATASETS
#################################################################################

# Path to root image folders
DATASETS_ROOT_FOLDER = "C:/Users/albam/OneDrive - UNIVERSIDAD DE HUELVA/2. Universidad/Proyects/2. Animal Recognition/datasets/"
# DATASETS_ROOT_FOLDER = "../../datasets/animals"
# DATASETS_ROOT_FOLDER = os.path.abspath(DATASETS_ROOT_FOLDER) + os.sep

#################################################################################
# CSV DATASETS
#################################################################################

# Path to csv-dataset files
CSV_FOLDER = "C:/Users/albam/OneDrive - UNIVERSIDAD DE HUELVA/2. Universidad/Proyects/2. Animal Recognition/csv/"

CSV_FOLDER = os.path.abspath(CSV_FOLDER) + os.sep

# csv-dataset file names
TRAIN_CSV = "final_train_list.csv"
TEST_CSV = "final_test_list.csv"
VALIDATION_CSV = "final_validation_list.csv"

#################################################################################
# MODEL
#################################################################################


########################################
# Model and weights defined together

# Path to the model+weights of the model
MODEL_WEIGHTS_PATH = None

########################################
# Path to folder where to save the model
 #MODEL_SAVE_FOLDER = "C:/Users/albam/OneDrive - UNIVERSIDAD DE HUELVA/2. Universidad/Proyects/2. Animal Recognition/models/v4/"
MODEL_SAVE_FOLDER = "../../models/v5/"
MODEL_SAVE_FOLDER = os.path.abspath(MODEL_SAVE_FOLDER) + os.sep

#################################################################################


#################################################################################
# TRAIN
#################################################################################
SHUFFLE = None


###################################################

# Size of images (when resized)

IMG_WIDTH = 200
IMG_HEIGHT = 200

#################################################################################
# Lists

IMG_EXTENSIONS = ['jpg', 'JPG', 'png', 'PNG']

#################################################################################
# Sample

BATCH_NUMBER = 16

CLASS_NUMBER = 3