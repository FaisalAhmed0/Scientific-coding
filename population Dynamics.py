# -*- coding: utf-8 -*-
"""
Created on Mon Oct 30 14:02:32 2017

@author: Faisal

Solution for population dynamics problem assuming infinite resources
dy/dt = kA
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint
def f(p,t,K) :
    '''Description of the ODE'''
    dy = K * p[0]
    return dy
t = np.linspace(0,10,50) #solution space
#Initiate the solver and specify the initial condition
k = 10
P = odeint(f,k,t,args = (.4055,))
#comparison between the numerical and analytical solution
plt.plot(t,P,'ko',t,k*np.exp(.4055*t))
