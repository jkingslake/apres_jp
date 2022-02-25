#!/usr/bin/env python
# coding: utf-8

# # Flow of the Antarctic Ice sheet
# 

# In[4]:


import fsspec
import xarray as xr
mapper = fsspec.get_mapper('gs://ldeo-glaciology/MEaSUREs')
M = xr.open_zarr(mapper) 


# In[1]:


import xarray.ufuncs as xu
speed = xu.sqrt(MEASURES.VX**2 + MEASURES.VY**2) 


# In[ ]:


speed.isel(x=slice(4000,5500,2), y = slice(4000,5500,2)).plot()

