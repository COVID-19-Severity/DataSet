# -*- coding: utf-8 -*-
"""COVID19-Machine_Learning_Biomarkers.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xqnhsHhivY4ynHsJ9W-MycuvqCYQ6FCc

<hr>

# :: SCRIPT AUTHORS ::
## * Ademir Luiz do Prado
## * Alexandre de Fátima Cobre
<hr>

# MACHINE LEARNING (ML)
Development of a Machine Learning model for the prognosis of COVID-19 in terms of SEVERITY using laboratory biomarkers.
The data are from examinations of patients treated at the Hospital de Clínicas of the Federal University of Paraná
# LEGEND:
### Sex:
##### 1=Female
##### 2=Male
### COVID:
##### * Total: 35,109 Positive Samples
##### * Non-Severe (Mild to Moderate): 7,719 samples
##### * Severe: 27,390 samples
### Classification Severity:
##### * Severe (Serious - Inpatients)
##### * Non-Severe (Mild to Moderate - Outpatients)
### Period of the Samples:
##### * March 2020 to September 2022

# OBJECTIVE:
Develop a Machine Learning model to predict the severity of COVID-19 and identify biomarkers associated with this severity in order to optimize priority in hospital care.
"""

# PHASES:
# 1: Import the DataSet
# 2: Import the Pandas library for handling the DataSet
# 3: Remove unnecessary columns (features) from DataSet
# 4: Install the Pycaret library to aid Auto-Machine Learn
# 5: Import the Pycaret library
# 6: Perform data pre-processing
# 7: Build and compare models
# 8: Train the best model based on predictive performance metrics
# 9: Extract the metrics results from the model
#10: Write conclusions about the best identified model
#11: Save the model to make predictions in real analyzes (Deploy)

# Phase 1: Import the DataSet

from google.colab import files
uploaded = files.upload()

# Phase 2: Import the Pandas library for handling the DataSet
import pandas as pd
DataSet = pd.read_csv("COVID19-DataSetSeverity.csv")
display (DataSet)

# Phase 3: Remove unnecessary columns (features) from DataSet
DataSetSeverity = DataSet.drop("ID", axis = 1)
display (DataSetSeverity)

# Phase 4: Install the Pycaret library to aid Auto-Machine Learn
!pip install pycaret

# Phase 5: Import the Pycaret library
from pycaret import classification

# Phase 6: Perform data pre-processing
classification_setup = classification.setup(data = DataSetSeverity, target = "COVID")

# Phase 7: Build and compare models
models = classification.compare_models()

# Phase 8: Train the best model based on predictive performance metrics
# First: The Light Gradient Boosting Machine (lightgbm) model achieved the best performance. We will create the Light Gradient Boosting Machine model
model_lightgbm = classification.create_model("lightgbm")

# Second: The Extreme Gradient Boosting (xgboost) model second the best performance.
model_xgboost = classification.create_model("xgboost")

# Third: The Random Forest Classifier (rf) model third the best performance.
model_rf = classification.create_model("rf")

# Fourth: The Extra Trees Classifier (et) model fourth the best performance.
model_et = classification.create_model("et")

# Fifth: The Gradient Boosting Classifier (gbc) model fifth the best performance.
model_gbc = classification.create_model("gbc")

# Phase 9: Extract the metrics results from the 5 top models
# lightgbm model metrics
classification.evaluate_model(model_lightgbm)

# xgboost model metrics
classification.evaluate_model(model_xgboost)

# rf model metrics
classification.evaluate_model(model_rf)

# et model metrics
classification.evaluate_model(model_et)

# gbc model metrics
classification.evaluate_model(model_gbc)

# Plotting only the 10 most important biomarkers for lightgbm model
classification.plot_model(model_lightgbm, plot ="feature")

# Phase 10: Write conclusions about the best identified model
# Several Machine Learning models were built to predict the diagnosis of COVID-19 using biomarker data from patients with COVID-19
# The Light Gradient Boosting Machine (lightgbm) model had the best predictive performance
# The 5 most important biomarkers for the prognosis of COVID-19, for the samples under study, were: C-reactive protein, Creatinine, Albumin, Lymphocytes and Erythrocytes
# The next step is to develop the App so that the model can be used in Health Institutions.

# Phase 11: Save the model to make predictions in real analyzes (Deploy)
classification.save_model(model_lightgbm, "BestModel-ML_LightGBM")