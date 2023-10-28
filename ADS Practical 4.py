#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:33:15 2023

@author: diya
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#matplotlib inline

# reading the data from CSV files
VOD =  pd.read_csv("/Users/diya/Downloads/VOD_ann.csv")
TSCO =  pd.read_csv("/Users/diya/Downloads/TSCO_ann.csv")
BCS =  pd.read_csv("/Users/diya/Downloads/BCS_ann.csv")
BP =  pd.read_csv("/Users/diya/Downloads/BP_ann.csv")

print(VOD)
# creating subplots
plt.figure()

plt.subplot(2, 2, 1)
plt.hist(BCS["ann_return"], label="Barclays", density=True) 
plt.legend() # needs to be done for every subplot

plt.subplot(2, 2, 2)
plt.hist(BP["ann_return"], label="BP", density=True)
plt.legend()

plt.subplot(2, 2, 3)
plt.hist(TSCO["ann_return"], label="Tesco" , density=True)
plt.legend()

plt.subplot(2, 2, 4)
plt.hist(VOD["ann_return"], label="Vodafone" , density=True)
plt.legend()

plt.savefig("four_histo.png")
plt.show()

plt.figure()
# IMPORTANT range and bins setting need to be identical
# to get meaningful histogram
plt.hist(BP["ann_return"], label="BP", density=True, alpha=0.7) 
plt.hist(TSCO["ann_return"], label="Vodaphone" , density=True, alpha=0.7)
plt.legend()
plt.xlabel("ann. returns")
plt.savefig("one_histo.png")
plt.show()


 # list with names
stocks = ["Barclays", "BP", "Tesco", "Vodaphone"]
# create a list with the returns for all four stocks
# remember return is forbidden
ret = [BCS["ann_return"], BP["ann_return"], TSCO["ann_return"],VOD["ann_return"]]

plt.figure()
plt.boxplot(ret, labels=stocks)
plt.ylabel("ann. returns")
plt.savefig("box.png")
plt.show()


names = ["Barclays", "BP", "Tesco", "Vodaphone"] # market cap in £1000
cap = np.array([33367, 68785, 20979, 29741])
# pie chart for the four companies
plt.figure()
plt.pie(cap, labels=names)
plt.show()



ftse = 1814000
norm = cap / ftse # works for numpy array, not for lists
plt.figure()
# normalise will be required in future versions
plt.pie(norm, labels=names, normalize=False)
plt.show()


plt.figure()
plt.bar(names, cap)
plt.ylabel("market cap [£1000]")
plt.show()