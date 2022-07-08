# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#veri yukleme

veriler= pd.read_csv("veriler.csv")

print(veriler)


#veri on isleme

boy=veriler[["boy"]]#list of list
print(boy)

boykilo=veriler[["boy","kilo"]]
print(boykilo)

x=10


 