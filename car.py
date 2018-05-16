# -*- coding: utf-8 -*-
"""
Created on Wed May 16 20:18:30 2018

@author: NP
"""
import pandas as pd
import numpy as np

data = pd.read_csv('car.data.txt',names = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety','class'])

col = ['buying', 'maint', 'doors', 'persons', 'lug_boot', 'safety']
X = data[col]
y = data['class']
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=1)

X_train['class'] = y_train

for atr in col:
    l = list(X_train[atr].unique())
    
    