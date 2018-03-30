#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:26:37 2018

@author: jeandesmarchelier
"""

from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D



 
    

l = 20
K=linspace(0,l,20)
ax = subplot(111)
ax.set_xlim(1,30)
Z = l*(2*K + 1) - floor((l-1)/(K+1))*(K+1)*K-((l-1)%(K+1))*((l-1)%(K+1)+1)
l20, = plot(K,Z,'ro',label = 'L = 20')
xlabel('k')
ylabel('Total Distance')
l = 30
K=linspace(0,l,30)
Z = l*(2*K + 1) - floor((l-1)/(K+1))*(K+1)*K-((l-1)%(K+1))*((l-1)%(K+1)+1)
l30, = plot(K,Z,'go', label = 'L = 30')
xlabel('k')
ylabel('Total Distance')
legend(handles = [l20, l30])
show()
    

k = 20
L=linspace(k,100,40)
ax = subplot(111)
ax.set_xlim(21,100)
Z = L*(2*k + 1) - floor((L-1)/(k+1))*(k+1)*k-((L-1)%(k+1))*((L-1)%(k+1)+1)
k20, = plot(L,Z,'ro',label = 'K = 20')
k = 30
L=linspace(k,100,35)
Z = L*(2*k + 1) - floor((L-1)/(k+1))*(k+1)*k-((L-1)%(k+1))*((L-1)%(k+1)+1)
k30, = plot(L,Z,'go', label = 'K = 30')
xlabel('l')
ylabel('Total Distance')
legend(handles = [k20, k30])
show()