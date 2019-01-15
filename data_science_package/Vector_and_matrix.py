#!/usr/bin/env python
# coding: utf-8

# In[1]:


def make_matrix(row, column, shape):
    return [[shape(i,j)
            for j in range(column)]
           for i in range(row)]


# In[7]:


def diagonal(i,j):
    return 1 if i == j else 0


# In[8]:


make_matrix(5,5,diagonal)


# In[2]:


def get_row(A,i):
    return A[i]


# In[3]:


def get_column(A,j):
    return [A_i[j]
           for A_i in A]


# In[ ]:




