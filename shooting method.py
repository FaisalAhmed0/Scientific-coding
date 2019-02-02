import numpy as np, matplotlib.pyplot as plt
import scipy.integrate as si
# Solution of ODE of the form 
# d^2y/dx^2 + lambda*y = 0
# with the boundary condition y(0)=0 and y(L) = 0
# it is an eignvalue problem
# solved using a shooting (binary search) approach 
def f(y,t,eign) :# Differntail eq. with BV problems P.212
    dy = [0,0]
    dy[0] = y[1]
    dy[1] = -eign*y[0]
    return dy    
t = np.linspace(0,1,100)    
init = [0,.0001]
y = si.odeint(f,init,t,args = (10,))
accuracy = 10**-8
lmbda = 1
dl = .1
while abs(y[-1,0]) > accuracy:
    y = si.odeint(f,init,t,args = (lmbda,))
    if y[-1,0] > 0 :
        lmbda+=dl
    else:
        lmbda=-dl
        dl  = dl/2
print (lmbda)        
plt.plot(t,y[:,0])