# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 00:54:50 2019

@author: 69018
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns 

data = pd.read_csv('tmppgx_njve.csv',encoding = "ISO-8859-1")

data.columns

data['result'].value_counts()

data['result'].unique()

data['result'].nunique()

data['result'].count()

data.head(5)

comments = data['comments'].unique()

comments = pd.DataFrame(comments)

subdata = data[['violation','comments']]

data.columns

len(data.columns)

data.columns

data['licenseno'].unique()

len(data.columns)

data['license\\no'].nunique()

data['businessname'].unique()

data['expdttm'].nunique()

data['result'].unique()

data.columns

data['viollevel'].value_counts().plot.bar()

data['licstatus'].value_counts().plot.bar()

plt.figure(figsize=(10,10))
sns.barplot(x=data.isnull().sum().sort_values(ascending=False),y=data.isnull().sum().sort_values(ascending=False).index)
plt.title("counts of missing value",size=20)

data.isnull().sum()

#how many violation per businesses are within this dataset 
data['businessname'].value_counts()
#found values of number of violations within each busienss 
#there are duplicate names such as mcdonalds and mcdonald's 

data_clean=data.drop_duplicates()
#no duplicates 
data['violstatus'].value_counts()
#fail and pass and state blanks as unknown 
comments

subdata1 = data[['violation','violstatus','comments']]
subdata1.head(5)
data[data['result']=='HE_Filed']['violstatus']
#see all the filed and the violation status 

data[data['result']=='HE_Filed']['violstatus'].value_counts()
#pass 40641 fail 28236 unknown 347
data[data['result']=='HE_Filed']['violstatus'].value_counts().plot.bar()

place=data.groupby(['businessname','address','city'])['violstatus'].value_counts()

c_pass = data[data['violstatus']=='Pass']

c_fail = data[data['violstatus']=='Fail']
