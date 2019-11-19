#!/usr/bin/env python
# coding: utf-8

# In[11]:


#lab4_4
import warnings
warnings.filterwarnings(action='ignore') 
import numpy as np

#return value: changed int array
def toNum(sequence):
    num_seq = []
    for i in range(len(sequence)):
        if sequence[i] == 'study':
            num_seq.append(0)
        elif sequence[i] == 'rest':
            num_seq.append(1)
        elif sequence[i] == 'walk':
            num_seq.append(2)
        else:
            num_seq.append(3)
    return num_seq

#input probability
p = np.array(
    [0.06,0.15,0.05,0.2,
    0.05,0.8,0.1,0.05,
    0.05,0.15,0.5,0.3,
    0.2,0.15,0.15,0.5]
).reshape(4, 4)

#transition matrix
print("Transition Matrix")
print(p)
print()

#observation valuse
obser=['rest', 'eat', 'study', 'study', 'walk', 'rest']
print("Observation:",obser)
obser=toNum(obser)


#compute the probability of the sequence of observations
result=1
t=1
for i in obser:
    if t<len(obser):
        result=result*p[i][obser[t]]
        t=t+1

print("Answer:", ' %.9f' % result)


# In[ ]:




