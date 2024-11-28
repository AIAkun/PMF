import pickle
import numpy as np
import os
from evaluations import *
from pmf_model import *
import time
from sklearn.metrics import accuracy_score
import importlib,sys
import pandas as pd


dataset='ml-DD'

# load the saved model
with open('PMF_model20241127.pkl', 'rb') as f:
    model = pickle.load(f)

print('PMF Recommendation Model Example')

# choose dataset name and load dataset, 'ml-1m', 'ml-10m'
processed_data_path = os.path.join(os.getcwd(), 'predict_data', dataset)
data = np.loadtxt(os.path.join(processed_data_path, 'data.txt'), dtype=float)
data = data[:,0:2]
print('testing model.......')
preds = model.predict(data=data)
print('----------------------------preds----------------------------------\n',preds)
preds=np.round(preds)
print('----------------------------preds round----------------------------\n',preds)

# save the predictions 
final_data=np.insert(data,2,values=preds,axis=1)
df = pd.DataFrame(final_data, columns=['ChemicalID','DiseaseID','type'])
df.to_excel(os.path.join(processed_data_path, 'predictions.xlsx'), index=False)

print('predictions saved successfully.')
# time.sleep(30)

