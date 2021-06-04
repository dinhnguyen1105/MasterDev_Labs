#!/usr/bin/env python
# coding: utf-8

# In[146]:


import numpy as np
import matplotlib.pyplot as plt
from math import sqrt


# In[147]:


n=50


# In[151]:


def pi_estimate(n):
    x=np.random.random((1,n))
    y=np.random.random((1,n))
    
    
    new_list1  = []
    for nested_list in y:
        print(nested_list)
        for element1 in nested_list:
            print(element1)
            new_list1.append(element1)

    new_list2  = []
    for nested_list in x:
        print(nested_list)
        for element2 in nested_list:
            print(element2)
            new_list2.append(element2)

    k=0

    for i in range(n):
        if(new_list1[i]**2+new_list2[i]**2<=1):
            k=k+1

    pi=4*(k/n)

    return pi


# In[152]:


new_list=[]


# In[153]:


for i in range(100):
    f=pi_estimate(n)
    new_list.append(f)


# In[154]:



print(new_list)





# In[161]:


import csv
a=open("b1.csv","w")
c=csv.writer(a,delimiter='|')


# In[162]:


c.writerows(map(lambda x: [x], new_list))
a.close()


# In[163]:


from pandas import read_csv

dataframe = read_csv('b1.csv', names = ['pi'])
dataframe.hist()

print(dataframe.describe())






