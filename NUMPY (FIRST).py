#!/usr/bin/env python
# coding: utf-8

# NUMPY LEARNING (First)

# In[2]:


# Here importing as numpy
import numpy as np


# In[4]:


# Array creation in done
a = np.array([1,2,3])
a


# In[5]:


a = np.array([1,2,3])
print(a)


# In[11]:


import time
import sys
b = range(1000)
print(sys.getsizeof(5), len(b))
print(sys.getsizeof(5)* len(b))


# In[13]:


c = np.arange(1000)
print(c.size*c.itemsize)


# In[15]:


# Here time sys taking for checking the time for both normal python and using numpy
size = 10000
L1 = range(size)
L2 = range(size)
A1 = np.arange(size)
A2 = np.arange(size)


# In[19]:


start = time.time()
result = [(x+y) for x,y in zip(L1, L2)]
print(result)
print("Python List Took : ", (time.time()-start)*1000)


# In[18]:


start = time.time()
result = A1 + A2
print("Numpy Array Took : ",(time.time()-start)*1000)


# In[21]:


# The array creation is done here
a = np.array([[2,3,4],[4,8,9],[8,7,9]])
a


# In[22]:


a.itemsize


# In[23]:


a.shape


# In[25]:


# The dimenssion
a.ndim


# In[26]:


# Here the array are printed as the float number
a = np.array([[2,3,4],[4,8,9],[8,7,9]], dtype = np.float64)
a


# In[27]:


a.itemsize


# In[29]:


# Here the array are printed as the complex number as the i + j
a = np.array([[2,3,4],[4,8,9],[8,7,9]], dtype = np.complex_)
a


# In[30]:


# All zeros array
np.zeros((4,5))


# In[34]:


# All ones array
np.ones((4,5))


# In[35]:


np.arange(10)


# In[36]:


print("Concatenation example : ")
print(np.char.add(["hmm","hi"],["hey","hehe"]))


# In[39]:


print(np.char.multiply("hi", 5))


# In[40]:


print(np.char.center("Hey", 20, fillchar = "."))


# In[42]:


print(np.char.capitalize("saikat munshib"))


# In[43]:


print(np.char.title("i am fine"))


# In[46]:


print(np.char.split("hey where are you?"))


# In[49]:


print(np.char.splitlines("hey where \nare you?"))


# In[50]:


print(np.char.strip(["ball","call","ww","lol"],"l"))


# In[55]:


print(np.char.join([":","-"],["dmy","ymd"]))


# In[57]:


print(np.char.replace("He will a topper","will","is"))


# In[ ]:




