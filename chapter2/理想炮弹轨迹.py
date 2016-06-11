# -*- coding: utf-8 -*-
"""
Created on Sat Jun 11 16:12:01 2016

@author: lenovo
"""

import numpy as np
import matplotlib.pyplot as plt
import math

g=9.8
b2m=5e-5
class flight_state:
    def __init__(self, _x=0,_y=0,_vx=0,_vy=0,_t=0):
        self.x=_x
        self.y=_y
        self.vx=_vx
        self.vy=_vy
        self.t=_t
class Cannon:
    def __init__(self,_fs=flight_state(0,0,0,0,0),_dt=0.1):
        self.cannon_flight_state=[]
        self.cannon_flight_state.append(_fs)
        self.dt=_dt
        #print self.cannon_flight_state[-1].x,self.cannon_flight_state[-1].y
    def next_state(self,current_state):
        global g
        next_x=current_state.x+current_state.vx*self.dt        
        next_vx=current_state.vx
        next_y=current_state.y+current_state.vy*self.dt
        next_vy=current_state.vy-g*self.dt
        next_t=current_state.t+self.dt
        return flight_state(next_x,next_y,next_vx,next_vy,next_t)
    def shot(self):
        while not(self.cannon_flight_state[-1].y<0):
            self.cannon_flight_state.append(self.next_state(self.cannon_flight_state[-1]))
        r = - self.cannon_flight_state[-2].y / self.cannon_flight_state[-1].y
        self.cannon_flight_state[-1].x = (self.cannon_flight_state[-2].x + r * self.cannon_flight_state[-1].x) / (r + 1)
        self.cannon_flight_state[-1].y = 0
        #print self.cannon_flight_state[-1].x,self.cannon_flight_state[-1].y
    def show_trace(self):
        global x,y
        x=[]
        y=[]
        for fs in self.cannon_flight_state:
            x.append(fs.x)
            y.append(fs.y)

c1=Cannon(flight_state(0,0,100,100,0),_dt=0.1)
c1.shot()
c1.show_trace()
plt.plot(x,y,'g',label=r'free$\theta=45^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
c1_final=x[-1]

c2=Cannon(flight_state(0,0,100*2**0.5*math.cos(60/57.325),100*2**0.5*math.sin(60/57.325)))
c2.shot()
c2.show_trace()
plt.plot(x,y,'r',label=r'free$\theta=60^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
c2_final=x[-1]

c3=Cannon(flight_state(0,0,100*2**0.5*math.cos(30/57.325),100*2**0.5*math.sin(30/57.325)))
c3.shot()
c3.show_trace()
plt.plot(x,y,'b',label=r'free$\theta=30^\circ$')
legend3=plt.legend(loc='best',prop={'size':11},frameon=False)
c3_final=x[-1]

c4=Cannon(flight_state(0,0,100*2**0.5*math.cos(37.5/57.325),100*2**0.5*math.sin(37.5/57.325)))
c4.shot()
c4.show_trace()
plt.plot(x,y,'y',label=r'free$\theta=37.5^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
c4_final=x[-1]

c5=Cannon(flight_state(0,0,100*2**0.5*math.cos(52.5/57.325),100*2**0.5*math.sin(52.5/57.325)))
c5.shot()
c5.show_trace()
plt.plot(x,y,'c',label=r'free$\theta=52.5^\circ$')
plt.legend(loc='best',prop={'size':11},frameon=False)
c5_final=x[-1]

plt.xlabel('x')
plt.ylabel('y')
plt.title('the trajectory of the cannon shell',fontsize=16)
plt.show()

theta=[55,50,45,40,35]

