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
###
# odeint only accept differential equation of the form dy/dyx = f(x,y)
# any explict ODE can be put into this form by reformulating the system into coupled first order ODEs
# take for example if your system is d^2y/dx^2 = -y + g(x)you derive the varibales
# y1 = y and y2 = dy/dx
# then differentiate the variables
# dy1/dx = dy/dx = y2 and dy2/dx = d^2y/dx^2 = -y + g(t) = -y1 + g(x)
# so in the code you modify the f function so that dy[0]= y[1] and dy[1] = -y[1] + g(x)
###
