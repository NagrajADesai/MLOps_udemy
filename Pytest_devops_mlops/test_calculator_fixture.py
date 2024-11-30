import pytest
from calculator import add, subtract


@pytest.fixture
def calculator_setup():
    print("Setting up the environment for calculator")

def test_add(calculator_setup):
    assert add(3,4) == 7

def test_subtract(calculator_setup):
    assert subtract(3,4) == -1


# from Packaging_ML_models.packaging_ml_model.prediction_model.config import config
# from Packaging_ML_models.packaging_ml_model.prediction_model.processing.data_handling import load_dataset
# from Packaging_ML_models.packaging_ml_model.prediction_model.predict import generate_predictions


# @pytest.fixture
# def single_prediction():
#     test_dataset = load_dataset(config.TEST_FILE)
#     single_row = test_dataset[:1]
#     result = generate_predictions(single_row)
#     return result

# def test_single_pred_not_none(single_prediction): #output is not none
#     assert single_prediction is not None

# def test_single_pred_str_type(single_prediction): #data type is string
#     assert isinstance(single_prediction.get('prediction')[0],str)

# def test_single_pred_validate(single_prediction): # check the output is Y
#     assert single_prediction.get('prediction')[0] == "Y"