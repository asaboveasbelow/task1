#!/usr/bin/env python
# coding: utf-8

# In[10]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

print(a)
for i in a:
    
    if i < 5:
        print(i)


# In[22]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []

for i in a:
    if i < 5:
        newList.append(i)
print(newList)


# In[20]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
newList = []
number = int(input('Write you number from 1 to 89: '))
print(number)
for i in a:
      if i < number:
        newList.append(i)
print(newList)   

