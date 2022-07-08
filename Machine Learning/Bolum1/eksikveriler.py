# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#veri yukleme

veriler= pd.read_csv("eksikveriler.csv")

print(veriler)


#veri on isleme

boy=veriler[["boy"]]#list of list
print(boy)

boykilo=veriler[["boy","kilo"]]
print(boykilo)

#eksik veriler 

#sci-kit learn

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan,strategy="mean")

Yas=veriler.iloc[:,1:4].values

print(Yas)
imputer =imputer.fit(Yas[:,1:4])
Yas[:,1:4]=imputer.transform(Yas[:,1:4])
print(Yas)


 