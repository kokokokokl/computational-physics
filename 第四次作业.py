# -*- coding: utf-8 -*-
"""
Created on Mon Mar 21 15:06:09 2016

@author: lenovo
"""
import numpy as np
N_U = []
t = []
g = 9.8
dt = 0.1
N_U.append(0)
t.append(0)
end_time = 10

for i in range(int(end_time / dt)):
	tmp = N_U[i]+g*dt
	N_U.append(tmp)
	t.append(dt * (i + 1))
	print t[-1], N_U[-1]
