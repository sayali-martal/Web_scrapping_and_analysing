# -*- coding: utf-8 -*-
"""
Created on Thu Dec  5 15:54:09 2019

@author: Sayali
"""

# Importing libraries
import pandas as pd
import seaborn as sns
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from xgboost import XGBClassifier
from sklearn.metrics import confusion_matrix
import pickle

# Reading dataset
df = pd.read_csv('..\\fundrazr\\data.csv')

# Heatmap
sns.heatmap(df.isnull(), yticklabels=False, cbar=False)

# Preprocessing
df.isnull().sum()
df = df.dropna()

df.drop(['campaignTitle', 'amountRaised', 'currencyType'], axis=1, inplace=True)

df['mediaCount'] = df['mediaCount'].str.extract('([0-9]+)')
df['percent_complete'] = df['percent_complete'].str.extract('([0-9]+)')
df['period'] = df['period'].str.extract('([a-zA-z ]+)')
df['goal'] = df['goal'].str.extract('([0-9.]+[k]?)')

def convert_scale(value):
    if value.endswith("k"):
        return float(value[:-1]) * 10**3
    else:
        return float(value)

df['goal'] = df['goal'].apply(convert_scale)

print(df.dtypes)

# Converting string data type into integer
df["mediaCount"]= df["mediaCount"].astype(int)
df["percent_complete"]= df["percent_complete"].astype(int)

df['days'] = 1
df['days'][df['period'].str.contains('Weeks')] = 7
df['days'][df['period'].str.contains('Years')] = 365

df['periodInDays'] = df['timeLeft']*df['days']

df.drop(['timeLeft', 'days'], axis=1, inplace=True)

df['period'] = df['period'].str.extract('(\w+$)')

df['period'].value_counts()
df['periodInDays'].value_counts()

df['percent_complete'] = np.where(df['percent_complete'] > 100, 100, df['percent_complete'])

print(df['periodInDays'].max())

df['periodInDays'] = np.where((df['period'] == 'left'), (df['periodInDays'].max()+df['periodInDays']), df['periodInDays'])

y = (df['percent_complete'] > 99).astype(int)
df.drop(['percent_complete', 'period'], axis=1, inplace=True)

X = df

# Splitting the dataset into the Training set and Test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)

# Feature Scaling
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Fitting XGBoost to the Training set
classifier = XGBClassifier(base_score = 0.55, gamma = 2)
classifier.fit(X_train, y_train)

y_pred = classifier.predict(X_test)

# Making the Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

# Applying k-Fold Cross Validation
accuracies = cross_val_score(estimator = classifier, X = X_train, y = y_train, cv = 10)
accuracies.mean()
accuracies.std()

# Saving model
filename = 'model.pkl'
pickle.dump(classifier, open(filename, 'wb'))