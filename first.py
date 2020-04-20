#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 11:02:08 2017

@author: abhilashsk
"""
#importing pandas, numpy and matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

#Function for Data ingestion stage using read_csv
def readData():
    try:
        dataset=pd.read_csv('./data/Airplane_Crashes_and_Fatalities_Since_1908.csv') #storing the data in a DataFrame
        print("Dataset loaded successfully.")
        return dataset
    except FileNotFoundError:
        print("The file does not exist.")
    
    #print(crashds.head(2))

#Function for Data cleaning stage
def cleanData(dataset):
    del dataset['Summary']  #Summary column is dropped
    
    #removing invalid values
    ds1=dataset.isnull().any()
#    print(ds1)
    if True in ds1.values:  #if there are invalid value drop them
        print("There are invalid values in the dataset. Deleting invalid values...")
        dataset=dataset.dropna()
        print("Invalid values have been dropped.\n")
#        ds1=dataset.isnull().any()
#        print(ds1)
    else:   #if there are no invalid values
        print("There are no invalid values in the dataset.\n")
        
    #changing the format and type of values in Date column
    shape=dataset.shape
    for x in range(shape[0]):
        dataset.iloc[x,0]=datetime.datetime.strptime(dataset.iloc[x,0], "%m/%d/%Y").date()
    
    print("Dataset has been cleaned.")
    #returning dataset
    return dataset

"""
Selecting Columns Section
"""

#Function to return columns of the dataset
def getColumns(dataset,col,rowStart,rowEnd):
    return dataset[col].iloc[rowStart:rowEnd].to_string(index=False)

#Function to return dataset filtered by dates
def filterDs(dataset,frm,to):
    filter_1=dataset['Date']>frm
    filter_2=dataset['Date']>to
    return dataset[filter_1 & filter_2]

"""
Descriptive Statistics Section
"""

#Function to get dataset details
def desDataset(dataset,info):
    if info=="shape":
        return dataset.shape

#Function to describe the columns
def desColumns(dataset,col):
    desc=dataset[col].describe()
    return desc

#Function for displaying data regarding the data set
def defDataset(dataset):
    #print(dataset.head())
    #print(dataset.tail())
    shape=dataset.shape
    columns=dataset.columns
    print("The Indices of the dataset: ",columns,"\nThe shape of dataset: ",shape)
    #dataset.plot(x='Operator',y='Fatalities',figsize=(15,10),kind='bar')


#Function to return column and rows of the dataset
def retData(dataset,cols,rows=0):   #cols will be a list of columns selected
    columns=dataset.columns
    for x in columns:
        print(dataset[x])


#ds=readData()
#ds=cleanData(ds)
##print(ds.head(10))
#desColumns(ds,'Aboard')