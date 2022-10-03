import os
                                    # Paths to root folders

DATASETS_ROOT_FOLDER = "../../datasets/animals/"
DATASETS_ROOT_FOLDER = os.path.abspath(DATASETS_ROOT_FOLDER) + os.sep
CSV_FOLDER = "../../csv/"
CSV_FOLDER = os.path.abspath(CSV_FOLDER) + os.sep
MODELS_FOLDER = "../../models/v4/"
MODELS_FOLDER = os.path.abspath(MODELS_FOLDER) + os.sep

#################################################################################
                                # Paths of subfolders

DATASET_ORIGINALS = DATASETS_ROOT_FOLDER + "data/"
DATASET_SUB_FINAL = DATASETS_ROOT_FOLDER + "final/"

#################################################################################
                                # Names of FOLDERS

PROJECT_ROOT_FOLDER_NAME = "2. Animal Recognition"

#################################################################################
                                # Names of files

CSV_NAME_FINAL = "final_imgs_and_labels.csv"

TRAIN_CSV = "final_train_list.csv"
TEST_CSV = "final_test_list.csv"
VALIDATION_CSV = "final_validation_list.csv"

#################################################################################
                        # Size of images (when resized)

IMG_WIDTH = 200
IMG_HEIGHT = 200

#################################################################################
                                    # Lists

IMG_EXTENSIONS = ['jpg', 'JPG', 'png', 'PNG']

#################################################################################
                                    # Sample

N_SAMPLES = 16
n_classes = 3