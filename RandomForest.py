# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 13:33:28 2020

@author: HP P DTS
"""

import pandas as pd
csv=pd.read_csv('iris.csv')
import matplotlib.pyplot as plt
print(csv.columns)
#'sepal_length', 'sepal_width', 'petal_length', 'petal_width',
#'species'
df1=csv[['sepal_length', 'sepal_width']][:50]
df2=csv[['sepal_length', 'sepal_width']][50:100]
df3=csv[['sepal_length', 'sepal_width']][100:150]
plt.plot(df1['sepal_length'], df1['sepal_width'],'ro',label='Setosa')
plt.plot(df2['sepal_length'], df2['sepal_width'],'bo',label='Versicolor')
plt.plot(df3['sepal_length'], df3['sepal_width'],'go',label='Virginica')
plt.legend()

df4=csv[['petal_length', 'petal_width']][:50]
df5=csv[['petal_length', 'petal_width']][50:100]
df6=csv[['petal_length', 'petal_width']][100:150]

plt.plot(df4['petal_length'], df4['petal_width'],'ro',label='Setosa')
plt.plot(df5['petal_length'], df5['petal_width'],'bo',label='Versicolor')
plt.plot(df6['petal_length'], df6['petal_width'],'go',label='Virginica')
plt.legend()

# Preprocessing
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
csv['species_new']=le.fit_transform(csv['species'])

X=csv.drop(['species_new','species'],axis=1)
y=csv['species_new']


# TrainTestSplit
from sklearn.model_selection import train_test_split
X_train,x_test,y_train,y_test=train_test_split(X,y,test_size=0.2)

# Model RandomForestClassifier call
from sklearn.ensemble import RandomForestClassifier
rfc=RandomForestClassifier(7)
rfc.fit(X_train,y_train)
rfc.score(x_test,y_test)
y_pred=rfc.predict(x_test)
from sklearn.metrics import confusion_matrix
cm=confusion_matrix(y_test,y_pred)
import seaborn as sns
plt.figure(figsize=(8,5))
sns.heatmap(cm,annot=True,center=True)
plt.show()
from sklearn.metrics import accuracy_score
score=accuracy_score(y_test,y_pred)
print(score)
from sklearn.metrics import classification_report
cr=classification_report(y_test,y_pred)
print(cr)