# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 01:37:51 2021

@author: efe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#veri yukleme

veriler= pd.read_csv("tenis.csv")

# encoder: Kategorik -> Numeric
"""
play=veriler.iloc[:,-1:].values
print(play)
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
play[:,0]=le.fit_transform(play[:,0])
print(play)


windy=veriler.iloc[:,-2:-1].values
print(windy)
from sklearn import preprocessing
le=preprocessing.LabelEncoder()
windy[:,0]=le.fit_transform(windy[:,0])
print(windy)
"""

from sklearn import preprocessing
from sklearn.preprocessing import LabelEncoder
veriler2=veriler.apply(LabelEncoder().fit_transform)#tek tek label encoder yapmak yerine tüm sütunlar için bu komutu uyguladık

c=veriler2.iloc[:,:1]

from sklearn.preprocessing import OneHotEncoder
ohe=preprocessing.OneHotEncoder()
c=ohe.fit_transform(c).toarray()
print(c)



#verilerin birleştirilmesi-------------------------------
#numpy dizileri dataframe donusumu

havadurumu=pd.DataFrame(data=c,index=range(14), columns=["o","r","s"])

sonveriler=pd.concat([havadurumu,veriler.iloc[:,1:3]],axis=1)
sonveriler=pd.concat([veriler2.iloc[:,-2:],sonveriler],axis=1)




#veri kümesinin eğitim ve test olarak bölünmesi

from sklearn.model_selection import train_test_split
 
x_train, x_test,y_train,y_test=train_test_split(sonveriler.iloc[:,:-1],sonveriler.iloc[:,-1:],test_size=0.33, random_state=0) 


from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_train,y_train)

y_pred =regressor.predict(x_test)


#backward elimination
import statsmodels.api as sm

X= np.append(arr = np.ones((14,1)).astype(int), values =sonveriler.iloc[:,:-1], axis= 1 )

X_l =sonveriler.iloc[:,[0,1,2,3,4,5]].values
X_l =np.array(X_l,dtype=float)
model=sm.OLS(sonveriler.iloc[:,-1:] ,X_l).fit()
print(model.summary())

sonveriler=sonveriler.iloc[:,1:]

import statsmodels.api as sm

X= np.append(arr = np.ones((14,1)).astype(int), values =sonveriler.iloc[:,:-1], axis= 1 )

X_l =sonveriler.iloc[:,[0,1,2,3,4]].values
X_l =np.array(X_l,dtype=float)
model=sm.OLS(sonveriler.iloc[:,-1:] ,X_l).fit()
print(model.summary())


x_train=x_train.iloc[:,1:]
x_test=x_test.iloc[:,1:]

regressor.fit(x_train,y_train)

y_pred=regressor.predict(x_test)






