# -*- coding: utf-8 -*-
"""
Created on Thu Jun 09 14:31:29 2016

@author: lenovo
"""
import matplotlib.pyplot as plt
import numpy as np
x=np.linspace(0.0,20.0,201)
v=[]
t=[]
a=10;b=1
dt=0.1
v.append(0.0)
t.append(0)
end_time=20
for i in range(int(end_time/dt)):
    tmp=v[-1]+dt*(a-b*v[-1])
    v.append(tmp)
    t.append(dt*(i+1))
    print t[-1],v[-1]
line1,=plt.plot(t,v,'ro')
plt.xlabel("time/(s)")
plt.ylabel("velocity/(m/s)")
plt.legend((line1),('numerical line'))
plt.title("The Time-dependence of the Velocity of A Ball Falling with Friction")
plt.show()
