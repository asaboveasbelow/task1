#!/usr/bin/env python
# coding: utf-8

# In[ ]:


number = int(input('Write you number from 1 to 100: '))

x = range(2, 100)
for elem in x:
    if number % elem == 0 :
        print(number,'have divisors ',elem)
        if elem == number:
            break

