#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print('What is your name?')
name = input()
print('How old are you?')
age = int(input())

centuryYear = 100
presentYear = 2019
lifeExpentancy = presentYear + (centuryYear - age)


if age > 0 and age <= 100:

    print(name+', You will be a 100 years old in '+str(lifeExpentancy))
elif age >= 100:  
    print(name+', You already reach golden age in '+str(lifeExpentancy))


# In[ ]:




