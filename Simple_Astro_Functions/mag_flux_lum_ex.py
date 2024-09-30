#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 16:10:25 2024
README: Example code that converts magnitudes to flux and then luminosity using
the functions from mag_flux_lum.py
@author: karelgreen
"""

#%%Modules
from astropy.table import Table
import os
import numpy as np
import astropy.units as u
from mag_flux_lum import mag2flux, flux2lum
#%%Data
data = Table.read(os.path.dirname(os.getcwd())+'/dummy_data.fits', format='fits') #replace with file path

z = np.array(data['z'])
mag = np.array(data['mag'])

data['mag'].description #Output of this tells us the wavelength is 2.2 microns

wave = 2.2*(u.micron)

#%% Calculating flux and luminosity
flux = mag2flux(mag, wave)

lum = flux2lum(flux, z)

print(mag[0], '\n', flux[0], '\n', lum[0])