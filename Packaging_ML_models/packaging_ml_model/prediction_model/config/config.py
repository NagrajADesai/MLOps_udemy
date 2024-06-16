# store all the path and variables into config.py file

import pathlib
import os
import prediction_model 

# get the root path for prediction_model
PACKAGE_ROOT = pathlib.Path(prediction_model.__file__).resolve().parent

# get dataset path
DATAPATH = os.path.join(PACKAGE_ROOT,'datasets')

TRAIN_FILE = 'train.csv'
TEST_FILE = 'test.csv'

MODEL_NAME = 'Classification.pkl'
# get path of trained_models
SAVE_MODEL_PATH = os.path.join(PACKAGE_ROOT,'trained_models')

# target column
TARGET = 'Loan_Status'

# final features used in the model
FEATURES = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
       'ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History',
       'Property_Area','CoApplicantIncome']

NUM_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

CAT_FEATURES = ['Gender',
 'Married',
 'Dependents',
 'Education',
 'Self_Employed',
 'Credit_History',
 'Property_Area']

FEATURES_TO_ENCODE = ['Gender',
 'Married',
 'Dependents',
 'Education',
 'Self_Employed',
 'Credit_History',
 'Property_Area']

FEATURE_TO_MODIFY = 'ApplicantIncome'
FEATURE_TO_ADD = 'CoApplicantIncome'

# features to drop
DROP_FEATURES = ['CoApplicantIncome']

# taking log of numerical columns
LOG_FEATURES = ['ApplicantIncome', 'LoanAmount', 'Loan_Amount_Term']

