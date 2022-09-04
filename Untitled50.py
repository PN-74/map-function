#!/usr/bin/env python
# coding: utf-8

# In[4]:


nums = (1, 2, 3, 4, 5, 6, 7)
print("original list: ", nums)
result = map(lambda x: x + x + x, nums)
print("\ntriple of list numbers: ")
print(list(result))


# In[ ]:




