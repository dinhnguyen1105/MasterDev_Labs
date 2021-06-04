#!/usr/bin/env python
# coding: utf-8

# In[93]:


import numpy as np
import math
import pandas as pd
import time


# In[94]:


col=['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']


# In[95]:


pima=pd.read_csv("Desktop\Q2.csv", header=None,names=col)
pima


# In[96]:


T=[sorted(pima.x1.values),sorted(pima.x2.values),sorted(pima.x3.values),sorted(pima.x4.values),
   sorted(pima.x5.values),sorted(pima.x6.values),sorted(pima.x7.values),sorted(pima.x8.values),
   sorted(pima.x9.values),sorted(pima.x10.values)]


# In[97]:


def simple_number(a):
    j=0
    while True:
        if (j+1)<= (len(a)-1):
            if a[j]==a[j+1]:
                j=j+2
            else:
                b=a[j]
                break

        else:
            b=a[j]
            break
    return b


# In[98]:


for i in range(len(T)):
    for k in range(30):
        start=time.time_ns()
        simple_number(T[i])
        end=time.time_ns()
        list1.append(float(end-start))


# In[99]:


print(list1)



# In[106]:


import csv
a=open("b2.csv","w")
c=csv.writer(a,delimiter='|')


# In[107]:


c.writerows(map(lambda x: [x], list1))
a.close()


# In[108]:


from pandas import read_csv

dataframe = read_csv('b2.csv', names = ['pi'])
dataframe.hist()

print(dataframe.describe())


# In[ ]:




