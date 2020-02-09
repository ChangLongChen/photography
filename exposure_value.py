# -*- coding: utf-8 -*-
"""
Autor: ChangLong Chen
Date: 02092020
Ort: Taiwan
"""
import math
import numpy as np
#
def ev(fn=1.0, t=1.0, iso=100.0):
    '''
    fn (float): F-number
    t (flaot): exposure time
    iso (float): ISO speed, min = 0.8
    '''
    return np.round(np.log2((fn**2/t)*(0.01*iso)),1)
#
def ev2Nit(ev=1.0, k=12.5, iso=100.0):
    '''
    ev (flaot): exposure value
    k (float): calibration factor
    iso (flaot): ISO speed
    '''
    return np.round((k/iso)*2**ev,3)
#
def ev2Lux(ev=1.0, C=250, iso=100.0):
    '''
    ev (flaot): exposure value
    C (float): calibration factor
    iso (flaot): ISO speed
    '''
    return np.round((C/iso)*2**ev,3)
#
def Lux2ev(lux=1.0, C=250, iso=100.0):
    return np.round((np.log2(lux*iso/C)))
#
def Nit2ev(nit=1.0, k=12.5, iso=100.0):
    return np.round((np.log2(nit*iso/k)))   
#
if __name__ == '__main__':

    print('hallo')