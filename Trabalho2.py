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

'''-----------------------------------------------------------------------------
                        Iterative Method:
-----------------------------------------------------------------------------'''

def itMethod(x0,a,b,F_der_min,F_dder_max):
    m=(1/2)*(F_dder_max/F_der_min)
    return m

'''-----------------------------------------------------------------------------
                        Newton Method:
-----------------------------------------------------------------------------'''
def newtonMethod(x0,a,b,x_der_min,x_dder_max,eps):
    min_fd=F_deriv(x_der_min) #min first F derivative value
    max_fdd=F_dderiv(x_dder_max) #max secondF derivative value
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
  
#Tests------------------------------------------------------------------------
newtonMethod(0.54,0.5,0.54,0.5,0.5,error(5,4))
