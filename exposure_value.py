# -*- coding: utf-8 -*-
"""
Autor: ChangLong Chen
Date: 02092020
Ort: Taiwan
"""
import math
import numpy as np
#
def find_lightting(ev):
    '''
    find the proper lighting condition basedon ev value
    '''
    c = {'subject under quarter moon':-6, 'subject under crescent moon':-5,
         'subject under gibbous moon':-4,'subject under full moon':-3,
         'snowscape under full moon':-2, 'End of blue hour':-1,'Late in blue hour':0,
         'Middle of blue hour':1, 'Distant cityscape at night':2, 'Indoor scene lit only by dim window light':3,
         'Subjects under bright street lamps':4, 'Night home interiors':5, 'Brightly lit home interiors':6,
         'Stage shows':7, 'Interiors with bright florescent lights':8}
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