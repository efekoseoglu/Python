# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 23:47:45 2021

@author: efe
"""


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#veri yukleme
veriler= pd.read_csv("maaslar.csv")


x= veriler.iloc[:,1:2]
y =veriler.iloc[:,2:]
X=x.values
Y=y.values


#linear regression
from sklearn.linear_model import LinearRegression
lin_reg =LinearRegression()
lin_reg.fit(X,Y)

plt.scatter(X,Y,color ="red")
plt.plot(x,lin_reg.predict(X),color="blue")
plt.show()

#polynomial regression

from sklearn.preprocessing import PolynomialFeatures
poly_reg =PolynomialFeatures(degree =2)
x_poly =poly_reg.fit_transform(X)
print(x_poly)

lin_reg2 =LinearRegression()
lin_reg2.fit(x_poly,y)
plt.scatter(X,Y)
plt.plot(X,lin_reg2.predict(poly_reg.fit_transform(X)),color ="blue")
plt.show()



