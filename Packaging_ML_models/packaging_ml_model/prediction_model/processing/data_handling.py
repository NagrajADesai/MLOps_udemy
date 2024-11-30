# create function to load dataset and save the model
import os
import sys
from pathlib import Path
import joblib
import pandas as pd
from prediction_model.config import config

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent.parent
sys.path.append(str(PACKAGE_ROOT))

# create a function to read the dataset
def load_dataset(file_name):
    filepath = os.path.join(config.DATAPATH,file_name)
    _data = pd.read_csv(filepath)
    return _data 

# serialization of model
def save_pipeline(pipeline_to_save):
    save_path = os.path.join(config.SAVE_MODEL_PATH, config.MODEL_NAME)
    joblib.dump(pipeline_to_save,save_path)
    print(f"Model has been saved under the name {config.MODEL_NAME}")

# deserialization of model
def load_pipeline(pipeline_to_load):
    save_path = os.path.join(config.SAVE_MODEL_PATH, pipeline_to_load)
    model_loaded = joblib.load(save_path)
    print("Model has been loaded")
    return model_loaded
    