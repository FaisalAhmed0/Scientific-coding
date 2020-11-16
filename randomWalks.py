# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:02:32 2017

@author: Faisal
"""
# This is the testing branch
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rnd


plt.close('all')
def randomWalk(x):
    xsteps = np.zeros(x)
    ysteps = np.zeros(x)
    xs = (-2*rnd(x,))+1
    ys = (-2*rnd(x,))+1
    xsteps = np.cumsum(xs)
    ysteps = np.cumsum(ys)
    return xsteps,ysteps    
num_steps =1000
x,y = randomWalk(num_steps)
print (len(x))    
plt.plot(x,y,'bo')
plt.axes('equal')
