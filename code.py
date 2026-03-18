#!/usr/bin/env python
# coding: utf-8

# In[ ]:


pip install lightkurve --upgrade


# In[2]:


from lightkurve import read
import matplotlib.pyplot as plt
import numpy as np

lc = read("ktwo246199087-c12_llc.fits")
# lc.plot()


# In[3]:


# Remove bad quality
lc = lc[lc.quality == 0]

# Normalize
lc = lc.normalize()

lc.scatter()
plt.show()


# In[4]:


lc = lc[(lc.flux > 0.95) & (lc.flux < 1.05)]
lc.scatter()
plt.show()


# In[8]:


dip = lc[(lc.time.value > 2932) & (lc.time.value < 2934)]
dip.scatter()
plt.show()

depth = 1 - dip.flux.min()
print("Transit depth:", depth)


# In[ ]:




