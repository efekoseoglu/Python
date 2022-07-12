# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 00:20:17 2021

@author: efe
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#veri yukleme

veriler= pd.read_csv("tenis.csv")

print(veriler)



# encoder: Kategorik -> Numeric

weather=veriler.iloc[:,0:1].values
print(weather)

from sklearn import preprocessing

le=preprocessing.LabelEncoder()

weather[:,0]=le.fit_transform(veriler.iloc[:,0])

print(weather)

ohe=preprocessing.OneHotEncoder()
weather=ohe.fit_transform(weather).toarray()
print(weather)

# encoder: Kategorik -> Numeric

c=veriler.iloc[:,-1:].values
print(c)

from sklearn import preprocessing

le=preprocessing.LabelEncoder()

c[:,-1]=le.fit_transform(veriler.iloc[:,-1])

print(c)

ohe=preprocessing.OneHotEncoder()
c=ohe.fit_transform(c).toarray()
print(c)


#verilerin birleştirilmesi-------------------------------
#numpy dizileri dataframe donusumu

sonuc =pd.DataFrame(data=weather,index=range(14),columns=["sunny","overcast","rainy"])
print(sonuc)

Hum=veriler.iloc[:,2:3]
print(Hum)

sonuc2=pd.DataFrame(data=weather,index=range(14),columns=["temp","hum","wind"])
print(sonuc2)
 
play= veriler.iloc[:,-2:].values
print(play)

sonuc3=pd.DataFrame(data=c[:,:1],index=range(14),columns=["play"])
print(sonuc3)


#dataframe birleştirme işlemi
s=pd.concat([sonuc,sonuc2],axis=1)
print(s)

s2=pd.concat([s,sonuc3], axis=1)
print(s2)

"""
#veri kümesinin eğitim ve test olarak bölünmesi

from sklearn.model_selection import train_test_split
 
x_train, x_test,y_train,y_test=train_test_split(s,sonuc3,test_size=0.33, random_state=0) 


from sklearn.linear_model import LinearRegression
regressor= LinearRegression()
regressor.fit(x_train,y_train)

y_pred =regressor.predict(x_test)

boy = s2.iloc[:,3:4].values
print(boy)

sol = s2.iloc[:,:3]
sag = s2.iloc[:,4:]

veri =pd.concat([sol,sag],axis=1)

x_train, x_test,y_train,y_test=train_test_split(veri,boy,test_size=0.33, random_state=0) 

r2= LinearRegression()
r2.fit(x_train,y_train)

y_pred =regressor.predict(x_test)


import statsmodels.api as sm

X= np.append(arr = np.ones((22,1)).astype(int), values =veri, axis= 1 )

X_l =veri.iloc[:,[0,1,2,3,4,5]].values
X_l =np.array(X_l,dtype=float)
model=sm.OLS(boy,X_l).fit()
print(model.summary())

X_l =veri.iloc[:,[0,1,2,3,5]].values
X_l =np.array(X_l,dtype=float)
model=sm.OLS(boy,X_l).fit()
print(model.summary())

X_l =veri.iloc[:,[0,1,2,3]].values
X_l =np.array(X_l,dtype=float)
model=sm.OLS(boy,X_l).fit()
print(model.summary())
"""