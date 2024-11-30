import pytest
import numpy as np
from pathlib import Path 
import os
import sys 

PACKAGE_ROOT = Path(os.path.abspath(os.path.dirname(__file__))).parent 
sys.path.append(str(PACKAGE_ROOT))

from prediction_model.config import config
from prediction_model.processing.data_handling import load_dataset
from prediction_model.predict import generate_predictions
from prediction_model.processing.data_handling import load_pipeline


# output from predict script not null
# output from predict script is str data type
# the output is Y for an example data

# Fixtures --> functions before test function --> ensure single_prediction
classification_pipeline = load_pipeline(config.MODEL_NAME)

@pytest.fixture
def single_prediction():
    test_data = load_dataset(config.TEST_FILE)
    pred = classification_pipeline.predict(test_data[config.FEATURES])
    return pred 

def test_single_pred_not_none(single_prediction): # output is not none
    assert single_prediction is not None 

def test_single_pred_str_type(single_prediction): # data type is integer
    print(f"Single prediction[0]: {single_prediction[0]}, type: {type(single_prediction[0])}")
    assert isinstance(single_prediction[0], np.int64)