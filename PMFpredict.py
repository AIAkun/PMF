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

predict_data_path=os.path.join(os.getcwd(), 'predict_data', dataset)
data = np.loadtxt(os.path.join(predict_data_path, 'data.txt'), dtype=float)
# print(data[:,0:2])
# continue training the model
# model.fit(X_train, y_train)

# predict using the loaded model

print('testing model.......')
preds = model.predict(data=data)
print('----------------------------preds----------------------------------\n',preds)
preds=np.round(preds)
# print(preds)
print('----------------------------preds round----------------------------\n',preds)
preds_list=preds.tolist()
# 添加预测值到原数据
result=np.insert(data,2,values=preds,axis=1)
# print(result)
df = pd.DataFrame(result)
df.columns=['ChemicalID','DiseaseID','type']
df.to_excel(os.path.join(predict_data_path, 'predict.xlsx'), index=False)

# time.sleep(30)
# test_rmse = RMSE(preds, data[:, 2])
# y_true = data[:, 2].tolist()

# print('test rmse:{:f}'.format(test_rmse))
# print('accuracy_score:',accuracy_score(y_true, preds_list))

# #保存model
# with open('PMF_model.pkl', 'wb') as f:
#     pickle.dump(model, f)


