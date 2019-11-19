#!/usr/bin/env python
# coding: utf-8

# In[49]:


#lab4_3
import warnings
warnings.filterwarnings(action='ignore') 
import numpy as np

#return value: changed int array
def toNum(sequence):
    num_seq = []
    for i in range(len(sequence)):
        if sequence[i] == 'bull':
            num_seq.append(0)
        elif sequence[i] == 'bear':
            num_seq.append(1)
        else:
            num_seq.append(2)
    return num_seq

#input probability
p = np.array(
    [0.9, 0.07, 0.03, 0.15, 0.8, 0.05, 0.35, 0.15, 0.5]
).reshape(3, 3)

#transition matrix
print("Transition Matrix")
print(p)
print()

#observation valuse
obser=['bull', 'bear', 'stagnant', 'bull', 'stagnant', 'bear', 'bear', 'bull']
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





# In[ ]:




