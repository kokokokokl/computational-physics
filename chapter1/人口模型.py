import numpy as np
from pylab import *
from math import *
time=5
dt=0.001
t=[]
for i in range(int(time/dt)+1):
    t.append(i*dt)
#numerical solution
def solve_N(a,b):
    N=[]
    t=[]
    N_0=1000#float(input('N0='))
    N.append(N_0)
    t.append(0)
    time=5#float(input('total time='))
    dt=0.001#float(input('time step='))
    for i in range(int(time/dt)):
        N.append(N[i]+dt*(a*N[i]-b*(N[i])**2))#Attn:It is'**',not'^'
        t.append(t[i]+dt)
    return N
N_0=solve_N(10,0.01)


#exact solution
def exact_N(a,b):
    N=[]
    t=[]
    N_0=100#float(input('N0='))
    N.append(N_0)
    t.append(0)
    time=5#float(input('total time='))
    dt=0.001#float(input('time step='))
    for i in range(int(time/dt)):
        N.append(a*N_0*e**(a*t[i])/(a+b*N_0*(e**(a*t[i])-1)))#Attn:It is'**',not'^'
        t.append(t[i]+dt)
    return N
N_exact0=exact_N(10,0.01)


#plot 
plot(t,N_0,'--',color='red')
plot(t,N_exact0,color='red')
legend('b=0 numerical','b=0 exact')
xlabel('t(year)')
ylabel('N')
savefig('problem1.6.png')
show()
