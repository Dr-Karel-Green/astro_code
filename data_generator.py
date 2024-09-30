#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 15:03:37 2024

@author: karelgreen
"""
#%%Modules
import numpy as np
from astropy.table import Table, Column
import astropy.units as u
import os
#%%Table for data
dummy_data = Table()
dummy_data.meta['comments'] = ['Generic astropy table with fake values for testing code and running examples']

save = os.getcwd()+'/dummy_data.fits'
#%%

dummy_data['ID'] = np.arange(1,11).astype(str)

dummy_data['z'] = np.round(np.random.rand(10),4)*10
dummy_data['mag'] = np.random.uniform(17.5, 26,size=10)
dummy_data['mag'].description = ['Apparent magnitude in AB. Measured in the K-band (2.2 microns)']

                               
#%% Saving data
dummy_data.write(save, format='fits', overwrite=True)                            

#%% Viewing Table

# #Reading the table comments
# dummy_data.meta

# #Viewing the data in browser
# dummy_data.show_in_browser()  

# #Reading the column description
# dummy_data['mag'].description