#parametric plotter with animation 
import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random as rnd
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.colors as col
import matplotlib.cm as cms
from scipy.optimize import fsolve
from scipy.integrate import ode
from matplotlib import animation
num_steps = 100 #steps size for the animator 
plt.close('all')
fig = plt.figure()
interval = 3 #specify the axes limits
ax = plt.axes(xlim=(-interval,interval),ylim = (-interval,interval))

(myline,) = ax.plot([],[],lw=2) # ploter line 
(mypoint,) = ax.plot([],[],'ko',ms=5) # ploter pointer

def get_step(n,x,y,this_line,this_point):
    this_line.set_data(x[:n+1],y[:n+1])
    this_point.set_data(x[n],y[n])
    
def init():
    myline.set_data([],[])
    return myline
def animate(i):
    t = np.linspace(0,2*np.pi,(100*interval)/(interval+2))
    y = np.sin(t) #y(t)
    x = np.cos(t)#x(t)
    myline.set_data(x[:i+1],y[:i+1])
    mypoint.set_data(x[i],y[i])
    return myline
anim = animation.FuncAnimation(fig,animate,init_func=init,frames = 2000,interval = 1)
