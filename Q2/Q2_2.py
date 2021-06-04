#!/usr/bin/env python
# coding: utf-8

# In[90]:


import numpy as np
import math
import pandas as pd
import time


# In[91]:


col=['x1','x2','x3','x4','x5','x6','x7','x8','x9','x10']


# In[92]:


pima=pd.read_csv("Desktop\Q2.csv", header=None,names=col)
pima


# In[93]:


T=[pima.x1.values,pima.x2.values,pima.x3.values,pima.x4.values,
   pima.x5.values,pima.x6.values,pima.x7.values,pima.x8.values,pima.x9.values,pima.x10.values]


# In[94]:


def simple_number(n):
    for i in range(len(T[n])):
        for j in range(i+1,len(T[n])):
            if a[i]==a[j]:
                list2.append(a[i])
    s1=0
    for i in range(len(list1)):
        s1=s1+list1[i]
    s2=0
    for i in range(len(list2)):
        s2=s2+list2[i]
    b=s1-2*s2
    return b


# In[96]:


list4=[]


# In[97]:


for i in range (len(T)):
    for k in range(30):
        list1=T[0]
        list2=[]
        list3=[]
        start=time.time_ns()
        simple_number(i)
        end=time.time_ns()
        #print(end)
        list4.append(float(end-start))


# In[98]:


print(list4)



# In[111]:


import csv
a=open("b3.csv","w")
c=csv.writer(a,delimiter='|')


# In[112]:


c.writerows(map(lambda x: [x], list4))
a.close()


# In[113]:


from pandas import read_csv

dataframe = read_csv('b3.csv', names = ['pi'])
dataframe.hist()

print(dataframe.describe())


# In[ ]:




