#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 22 18:52:30 2024
README: A set of functions that can convert from magnitude to flux and 
luminosity in any combination
@author: karelgreen
"""

#%% Modules
import numpy as np
from astropy.cosmology import FlatLambdaCDM
cosmo = FlatLambdaCDM(H0=70, Om0=0.3, Tcmb0=2.725)
from math import pi
import astropy.units as u
from astropy.constants import c

#%% Functions

def mag2flux(mag, wavelength, zero_point=-48.6):
    """Converts an AB magntiude into a flux in erg s^-1 cm^-2. Requires the wavelength (or frequency)
    of the band the magnitude was measured in.
    
    mag = magntiude in AB units
    wavelength = wavelength of light, any reasonable unit
    zero_point = Use -48.6 for cgs (erg s-1 cm-2 hz-1), use +8.9 for janskys
    """
    try:
        wavelength = wavelength.to(u.m)
    except AttributeError:
        wavelength = wavelength*(u.m)
        
    flux_den = 10**((mag - zero_point)/-2.5)
    flux = flux_den*(c/wavelength)
    flux = flux.value 
    flux = flux*(u.erg/((u.s**1)*(u.cm**2)))
    return flux

def flux2mag(flux, wavelength, zero_point=-48.6):
    """Converts a flux in erg s^-1 cm^-2 into an AB magntiude. Requires the wavelength (or frequency)
    of the band the flux was measured in.
    
    flux = flux in any reasonable unit
    wavelength = wavelength of light, any reasonable unit
    zero_point = Use -48.6 for cgs (erg s-1 cm-2 hz-1), use +8.9 for janskys
    """
    try:
        wavelength = wavelength.to(u.m)
    except AttributeError:
        wavelength = wavelength*(u.m)
    
    try:
        flux = flux.to(u.erg/((u.s**1)*(u.cm**2)))
    except AttributeError:
        flux = flux*(u.erg/((u.s**1)*(u.cm**2)))
        
    fluxden = flux/(c.value/wavelength)
    mag = (-2.5*(np.log10(fluxden))) + zero_point
    mag = mag.value
    return mag

def flux2lum(flux, z):
    """Converts a flux to a luminosity.
    
    flux = flux in cgs units (erg s-1 cm-2)
    Z = Redshift"""
    distance = cosmo.luminosity_distance(z)
    distance = distance.to(u.cm)
    try:
        flux.to(u.erg/((u.s**1)*(u.cm**2)))
    except AttributeError:
        flux = flux*(u.erg/((u.s**1)*(u.cm**2)))
    
    luminosity = 4*pi*(distance**2)*flux
    return luminosity

def lum2flux(lum, z):
    """Converts a luminosity to a flux.
    
    lum = luminosity in erg s-1
    Z = Redshift"""
    distance = cosmo.luminosity_distance(z)
    distance = distance.to(u.cm)
    try:
        lum = lum.to(u.erg/(u.s**1))
    except AttributeError:
        lum = lum*(u.erg/(u.s**1))
    flux = lum/4*pi*(distance**2)
    return flux

