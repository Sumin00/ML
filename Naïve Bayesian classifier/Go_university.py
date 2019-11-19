#!/usr/bin/env python
# coding: utf-8

# In[1]:


#lab4_1
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
        if dataframe['play Golf'][i].item() ==y:
            total=total+1
            if dataframe[label][i].item() ==x:
                count=count+1
    return count/total
               
def count(dataframe,y):
    total=0
    for i in range(len(dataframe)):
        if dataframe['play Golf'][i].item() ==y:
            total=total+1
    return total/len(dataframe)

# Load the data
x = pd.read_csv('play_golf.csv')

# Preprocess the data
# Label encoding
columnlist=x.columns
MultiLabelEncoder(columnlist,x)
print(x)

#compute no probability
no=proba(x,2,0,'Outlook')*proba(x,0,0,'Temp')*proba(x,0,0,'Humidity')*proba(x,0,0,'Wind')*count(x,0)
print("Probability of No:",no)

#compute yes probablity
yes=proba(x,2,1,'Outlook')*proba(x,0,1,'Temp')*proba(x,0,1,'Humidity')*proba(x,0,1,'Wind')*count(x,1)
print("Probability of Yes:",yes)

if yes>=no:
    print("Predicted: Yes")
else:
    print("Predicted: No")


# In[ ]:





# In[ ]:




