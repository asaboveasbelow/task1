#!/usr/bin/env python
# coding: utf-8

# In[4]:


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
newList =[]

for x in b:
    if x in a and x not in newList:
        newList.append(x)
            
print(newList)


# In[ ]:




