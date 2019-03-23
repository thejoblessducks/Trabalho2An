
from __future__ import division
import numpy as np
import math as mt 
import decimal as dm 
import time as tm 
'''-----------------------------------------------------------------------------
                        Auxiliar Functions:
-----------------------------------------------------------------------------'''
error = lambda y,x: y*(10**(-x))

F = lambda x: (10*mt.exp(-0.5*x)*mt.cos(2*x) -4) #F(x)

F_deriv = lambda x: mt.exp(-0.5*x)*(-20*mt.sin(2*x)-5*mt.cos(2*x)) #F'(x)

F_dderiv = lambda x: mt.exp(-0.5*x)*(20*mt.sin(2*x)-37.5*mt.cos(2*x)) #F''(x)

f = lambda x: 0.5*(mt.acos((2*mt.exp(0.5*x))/5))#f(x)=1/2*arcos(2e^0.5x/5)


'''-----------------------------------------------------------------------------
                        Iterative Method:
-----------------------------------------------------------------------------'''

def itMethod(x0,eps):
    x1=f(x0)
    err=abs(x1-x0)
    i=1
    while err > eps:
        x0=x1
        x1=f(x0)
        err=abs(x1-x0)
        i+=1
    print("Iterações: "+str(i)+"\n")
    print("Raíz: "+str(dm.Decimal(x1))+"\n")
    print("Erro: "+str(dm.Decimal(err))+"\n")
    return

'''-----------------------------------------------------------------------------
                        Newton Method:
-----------------------------------------------------------------------------'''
def newtonMethod(x0,a,b,x_der_min,x_dder_max,eps):
    min_fd=F_deriv(x_der_min) #F' min value
    max_fdd=F_dderiv(x_dder_max) #F'' max value
    m=(1/2)*(min_fd/max_fdd) #multiplier
    err=abs(b-a) #x0 error
    x1=0
    i=0; #iterations
    while(err>eps):
        x1=x0-(F(x0)/F_deriv(x0))
        err=m*(err**2)
        x0=x1
        i+=1
    print("Iterações: "+str(i)+"\n")
    print("Raíz: "+str(dm.Decimal(x0))+"\n")
    print("Erro: "+str(dm.Decimal(err))+"\n")
    return
  
  
#Tests-------------------------------------------
print("Newton Method:\n")
newtonMethod(0.54,0.5,0.54,0.5,0.5,error(5,12))

print("Itera Method:\n")
itMethod(0.5,error(5,12))
