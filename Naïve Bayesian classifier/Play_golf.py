#!/usr/bin/env python
# coding: utf-8

# In[2]:


#lab4_2
import warnings
warnings.filterwarnings(action='ignore') 
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
import numpy as np
import pandas as pd

def MultiLabelEncoder(columnlist,dataframe):
    for i in columnlist:
        labelencoder_X=LabelEncoder()
        dataframe[i]=labelencoder_X.fit_transform(dataframe[i])
        
def proba(dataframe,x,y,label):
    total=0
    count=0
    for i in range(len(dataframe)):
        if dataframe['university'][i].item() ==y:
            total=total+1
            if dataframe[label][i].item() ==x:
                count=count+1
    return count/total   
              
def count(dataframe,y):
    total=0
    for i in range(len(dataframe)):
        if dataframe['university'][i].item() ==y:
            total=total+1
    return total/len(dataframe)

# Load the data
x = pd.read_csv('go_university.csv')

# Preprocess the data
# Label encoding
columnlist=x.columns
MultiLabelEncoder(columnlist,x)

print(x)
#compute enter probability
enter=proba(x,1,0,'dad')*proba(x,1,0,'mom')*proba(x,1,0,'child')*count(x,0)
print("Probability of Enter:",enter)

#compute none probablity
none=proba(x,1,1,'dad')*proba(x,1,1,'mom')*proba(x,1,1,'child')*count(x,1)
print("Probability of None:",none)

if enter>=none:
    print("Predicted: Enter")
else:
    print("Predicted: None")


# In[ ]:




