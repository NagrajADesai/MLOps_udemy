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

### Steps
1. completed config.py - contain all paths and variables
2. data_handling.py - create function to load dataset and save the model
3. preprocessing.py - create classes for all data preprocessing steps.