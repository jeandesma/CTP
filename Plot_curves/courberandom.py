#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 10:26:37 2018

@author: jeandesmarchelier
"""

from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D


k = 1
ax = subplot(111)
ax.set_xlim(1,10)
L = linspace(1,100,100)
Z = linspace(0,0,100)
for i in range(1,101):
    for j in range(1,k+2):
        Z[i-1] += ((pow(k-j+2,L[i-1])-pow(k-j+1,L[i-1]))/pow(k+1,L[i-1]))*(((2*j-1)/L[i-1])+1)
k1, = plot(L,Z,'ro', label = 'L = 1')

k = 20
L = linspace(1,100,100)
Z = linspace(0,0,100)
for i in range(1,101):
    for j in range(1,k+2):
        Z[i-1] += ((pow(k-j+2,L[i-1])-pow(k-j+1,L[i-1]))/pow(k+1,L[i-1]))*(((2*j-1)/L[i-1])+1)
k20, = plot(L,Z,'bo', label = 'L = 20')

k = 80

L = linspace(1,100,100)
Z = linspace(0,0,100)
for i in range(1,101):
    for j in range(1,k+2):
        Z[i-1] += ((pow(k-j+2,L[i-1])-pow(k-j+1,L[i-1]))/pow(k+1,L[i-1]))*(((2*j-1)/L[i-1])+1)
k80, = plot(L,Z,'go', label = 'L = 80')

k = 40

L = linspace(1,100,100)
Z = linspace(0,0,100)
for i in range(1,101):
    for j in range(1,k+2):
        Z[i-1] += ((pow(k-j+2,L[i-1])-pow(k-j+1,L[i-1]))/pow(k+1,L[i-1]))*(((2*j-1)/L[i-1])+1)
k40, = plot(L,Z,'mo', label = 'L = 40')


k = 60

L = linspace(1,100,100)
Z = linspace(0,0,100)
for i in range(1,101):
    for j in range(1,k+2):
        Z[i-1] += ((pow(k-j+2,L[i-1])-pow(k-j+1,L[i-1]))/pow(k+1,L[i-1]))*(((2*j-1)/L[i-1])+1)
k60, = plot(L,Z,'yo', label = 'L = 60')
xlabel('l')
ylabel('Competitive ratio')
legend(handles = [k1, k20, k40, k60, k80])
show()

l = 1
K = linspace(1,100,100)
Z = linspace(0,0,100)
for i in range(1,101):
    for j in range(1,int(K[i-1]+2)):
        Z[i-1] += ((pow(K[i-1]-j+2,l)-pow(K[i-1]-j+1,l))/pow(K[i-1]+1,l))*(((2*j-1)/l)+1)
l1, = plot(K,Z,'ro', label = 'L = 1')


l = 2
K = linspace(1,100,100)
Z = linspace(0,0,100)
for i in range(1,101):
    for j in range(1,int(K[i-1]+2)):
        Z[i-1] += ((pow(K[i-1]-j+2,l)-pow(K[i-1]-j+1,l))/pow(K[i-1]+1,l))*(((2*j-1)/l)+1)
l20, = plot(K,Z,'bo', label = 'L = 2')

l = 4
K = linspace(1,100,100)
Z = linspace(0,0,100)
for i in range(1,101):
    for j in range(1,int(K[i-1]+2)):
        Z[i-1] += ((pow(K[i-1]-j+2,l)-pow(K[i-1]-j+1,l))/pow(K[i-1]+1,l))*(((2*j-1)/l)+1)
l40, = plot(K,Z,'mo', label = 'L = 4')

l = 6
K = linspace(1,100,100)
Z = linspace(0,0,100)
for i in range(1,101):
    for j in range(1,int(K[i-1]+2)):
        Z[i-1] += ((pow(K[i-1]-j+2,l)-pow(K[i-1]-j+1,l))/pow(K[i-1]+1,l))*(((2*j-1)/l)+1)
l60, = plot(K,Z,'yo', label = 'L = 6')

l = 8
K = linspace(1,100,100)
Z = linspace(0,0,100)
for i in range(1,101):
    for j in range(1,int(K[i-1]+2)):
        Z[i-1] += ((pow(K[i-1]-j+2,l)-pow(K[i-1]-j+1,l))/pow(K[i-1]+1,l))*(((2*j-1)/l)+1)
l80, = plot(K,Z,'go', label = 'L = 8')
legend(handles = [l1, l20, l40, l60, l80])

ax = subplot(111)
ax.set_xlim(1,20)
ax.set_ylim(0,20)
xlabel('k')
ylabel('Competitive ratio')

show()