from __future__ import division
import numpay as np
import math as mt 
import decimal as dm 
import time as tm 
'''-----------------------------------------------------------------------------
                        Auxiliar Functions:
-----------------------------------------------------------------------------'''
error = lambda y,x: y*(10**(-x))

F = lambda x: (10*mt.exp(-0.5*x)*mtcos(2*x) -4)

F_deriv = lambda x: exp(-0.5*x)*(-20*mt.sin(2*x)-5*mt.cos(2*x))

'''-----------------------------------------------------------------------------
                        Iterative Method:
-----------------------------------------------------------------------------'''

def itMethod(x0,a,b,F_der_min,F_dder_max):
    m=(1/2)*(F_dder_max/F_der_min)
    return m

'''-----------------------------------------------------------------------------
                        Newton Method:
-----------------------------------------------------------------------------'''
def newtonMethod(x0,a,b,F_der_min,F_dder_max,eps):
    #Applying Newton's Method for zero calculation to F(x)
    m=(1/2)*(F_dder_max/F_der_min) #Multiplier for error
    err=abs(b-a) #x0 error
    x1
    i=0;
    while(err>eps):
        x1=x0-(F(x0)/F_deriv(x0))
        err=m*(err**2)
        x0=x1
        i+=1
    print("Iterações: "+str(i)+"\n")
    print("Raíz: "+str(dm.Decimal(x0))+"\n")
    print("Erro: "+str(dm.Decimal(err))+"\n")
    return
  
def iteraMethod(x0,eps,n_max):
    x1=F(x0)
    err=abs()
