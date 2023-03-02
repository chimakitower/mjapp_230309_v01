import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from function import *

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib

six_path = '/Users/chimaki_tower/Downloads/MJAPP_flask/src/six_id_230302.csv'
score_path = '/Users/chimaki_tower/Downloads/MJAPP_flask/src/score_binary_230302.csv'


df_six = pd.read_csv(six_path)
df_score = pd.read_csv(score_path)

np_six = df_six.to_numpy()
np_score = df_score.to_numpy()

np_six_onehot = get_onehot(np_six)
np_six_onehot = flatten(np_six_onehot)

x_train, x_test, t_train, t_test = train_test_split(np_six_onehot, np_score, test_size=0.3, random_state=0)
model = LogisticRegression(C=1.0)

model.fit(x_train, t_train)
pred = model.predict(x_test)

print(classification_report(t_test, pred))

joblib.dump(model, 'src/mjapp.pkl', compress=True)