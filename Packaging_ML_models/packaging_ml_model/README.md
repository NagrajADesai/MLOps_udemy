# Packaging_ml_model

- Experiments - contain experiments required for the project
- packaging_ml_model - contain complete model pipeline 
- tests - check the test cases

## Directory structure

```
├── MANIFEST.in
├── prediction_model
│   ├── config
│   │   ├── config.py
│   │   └── __init__.py
│   ├── datasets
│   │   ├── __init__.py
│   │   ├── test.csv
│   │   └── train.csv
│   ├── __init__.py
│   ├── pipeline.py
│   ├── predict.py
│   ├── processing
│   │   ├── data_handling.py
│   │   ├── __init__.py
│   │   └── preprocessing.py
│   ├── trained_models
│   │   ├── classification.pkl
│   │   └── __init__.py
│   ├── training_pipeline.py
│   └── VERSION
├── README.md
├── requirements.txt
├── setup.py
└── tests
    ├── pytest.ini
    └── test_prediction.py
```

## Virtual Envionment
Install virtualenv  
```python -m pip install virtualenv```

Check version   
```virtualenv --version```

Create virtual environment  
```virtualenv ml_package```

Activate virtual environment(Windows)   
```ml_package\Scripts\activate```

Deactivate virtual environment  
```deactivate```


### Steps
1. completed config.py - contain all paths and variables
2. data_handling.py - create function to load dataset and save the model
3. preprocessing.py - create classes for all data preprocessing steps.
4. pipeline.py - create complete data preprocessing pipeline
5. training_pipleline.py - create function to train the model
6. predict.py - create function to predict the result
7. add custome python path -    
```set PYTHONPATH=%PYTHONPATH%;D:\MLOps_udemy\Packaging_ML_models\packaging_ml_model```

    - run the training_pipeline file:
```python training_pipeline.py```
8. requirements.txt

```pip install -r requirements.txt```



