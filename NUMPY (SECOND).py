#!/usr/bin/env python
# coding: utf-8

# # ARRAY MANIPULATION

# # CHANGING SHAPE

# In[3]:


import numpy as np
a = np.arange(9)
print("The Original Array")
print(a)
print()
b = a.reshape(3,3)
print("The Modified Array")
print(b)


# In[4]:


print(b.flatten())


# In[6]:


a = np.arange(12).reshape(4,3)
print("The Original Matrix")
print(a)
print("The Transpose Matrix")
print(np.transpose(a))


# In[10]:


np.rollaxis(a,1,2)


# In[12]:


np.swapaxes(a,2,2)


# # NUMPY ARITHMETIC OPERATIONS

# In[14]:


a = np.arange(9).reshape(3,3)
a


# In[15]:


b = np.array([10,10,10])
b


# In[16]:


np.add(a,b)


# In[17]:


np.subtract(a,b)


# In[18]:


np.multiply(a,b)


# In[19]:


np.divide(a,b)


# # SLICING

# In[21]:


a = np.arange(20)
a


# In[22]:


a[4:]


# In[23]:


a[:4]


# In[24]:


s= slice(2,9,3)
a[s]


# # ITERATING OVER ARRAY

# In[29]:


a = np.arange(0,45,5)
a = a.reshape(3,3)
a


# In[30]:


for x in np.nditer(a):
    print(x)


# # ITERATION ORDER (C - STYLE AND F - STYLE)

# In[31]:


print(a)
for x in np.nditer(a, order = "C"):
    print(x)
    
for x in np.nditer(a, order = "F"):
    print(x)


# # JOINING ARRAYS

# In[36]:


a = np.array([[1,2],[3,4]])
print("FIRST ARRAY")
print(a)
b = np.array([[5,6],[7,8]])
print("SECOND ARRAY")
print(b)

print('Joining the two arrays along axis 0 :')
print(np.concatenate((a,b)))
print('\n')


# # RESIZING AN ARRAY

# In[38]:


a = np.array([[1,2,3],[4,5,6]])
print(a)
print(a.shape)
print('\n')
b = np.resize(a, (3,2))
print(b)
print(b.shape)


# # HISTOGRAM

# In[40]:


from matplotlib import pyplot as plt
a = np.array([20,87,84,25,54,15,78,58,54,125,41])
plt.hist(a, bins = [0,20,40,60,80,100])
plt.title("HISTOGRAM")
plt.show()


# In[41]:


plt.hist(a, bins = [0,20,40,60,80,100])
plt.title("HISTOGRAM")
plt.show()


# # OTHER USEFUL FUNCTIONS IN NUMPY

# In[42]:


a = np.linspace(1,3,10)
print(a)


# In[43]:


a = np.array([(1,2,3),(3,4,5)])
print(a.sum(axis = 0))


# In[44]:


import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,3*np.pi,0.1)
y = np.sin(x)
plt.plot(x,y)
plt.show()


# In[ ]:




