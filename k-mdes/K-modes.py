#!/usr/bin/env python
# coding: utf-8

# In[2]:


import warnings
warnings.filterwarnings(action='ignore') 
import random
import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# check change
def is_changed(old,new,num_cluster,labels):
    state=0
    for i in range(num_cluster):
        for j in range(len(labels)-1):
            # if not equals, return 1.
            if old.iloc[i,j]!=new.iloc[i,j]:
                state=1
            
    return state

# find new clusters 
def find_vector(x,num_cluster,vectors):
    # find new mode vectors
    for i in range(num_cluster):
        a=x[x['flag']==i].mode()
        vectors.iloc[i]=a.iloc[0]
    return vectors
        
# compute the distance
def get_distance(x,data,labels,vector):
    result=0
    for var in labels:
        #if the value is not equal, plus 1.
        if data[var]!=vector[var]:
            result+=1
        #if the value is equal, plus (1-n/total)
        else:
            result+=1-sum(x[var]==vector[var])/len(x)
    return result

# compute distance between mode vectors and clustering
def clustering(x,labels,vectors,list_clusters):
    for i in range(len(x)):
        for j in list_clusters:
            for k in range(len(vectors)):
                x.iloc[i,len(labels)+k]=get_distance(x,x.iloc[i,:],labels,vectors.iloc[k,:])
        for k in range(len(vectors)):
            # assign flag value according to minimun distance
            if x.iloc[i,len(labels)+k]==min(x.iloc[i,len(labels):len(labels)+len(vectors)]):
                x.iloc[i,len(labels)+len(vectors)]=k

    return x


# K- modes clustering
def k_modes(x,num_cluster,labels):
    # setting columns
    list_clu=[]
    for i in range(num_cluster):
        list_clu.append('cluster'+str(i))
        x['cluster'+str(i)]=-1 
    x['flag']=-1
    
    # select vectors randomly
    vectors=x.sample(n=num_cluster)
    
    # make the basket to store old vectors
    old=x.sample(n=num_cluster)
    
    time=0
    while True:
        #compute distance between mode vectors
        x=clustering(x,labels,vectors,list_clu)
    
        #store previous mode vectors
        for i in range(num_cluster):
            old.iloc[i]=vectors.iloc[i]
    

        #find new mode vectors
        vectors=find_vector(x,num_cluster,vectors)
        print("Iteration:",time)
        print("Current mode vectors")
        print(old.iloc[:,0:len(labels)])
        print("New mode vectors")
        print(vectors.iloc[:,0:len(labels)])
        time+=1
        if is_changed(old,vectors,num_cluster,labels)!=1:break
       
    return x

# purity function
def purity(clusters, classes):
    cm = np.array(pd.crosstab(clusters, classes))
    return np.sum(np.amax(cm, axis=1)) / np.sum(cm)



# read a dataset
data =pd.read_csv('mushrooms.csv')


#test
#data, X_test = train_test_split(data, test_size=0.99, random_state=123)


#split the target value
data, classes = data.drop('class',axis=1), data['class'].values

#store names of attributes
label=data.columns

# the number of clusters
k=2

# k-modes clustering
fin=k_modes(data,k,label)

#computing purity
#label encoder to classes
encoder = LabelEncoder()
encoder.fit(classes)
classes=encoder.transform(classes)

#print the result
print("-------------------------------------------")
print("k:",k)
print("purity:",purity(fin['flag'], classes))


# In[ ]:





# In[ ]:





# In[ ]:




