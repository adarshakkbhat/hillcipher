# -*- coding: utf-8 -*-
"""
Created on Wed May  4 22:01:07 2022

@author: Adarsha K K
"""

import numpy as np
import string
low=list(string.ascii_lowercase)
pt=list(input("Enter the plaintext\n").lower())
n=int(input("Enter n\n"))
key=list(input("Enter Key\n").lower())
k=np.array([[0]*n]*n)
for i in range(n):
    for j in range(n):
        k[i][j]=low.index(key[i*n+j])

e=len(pt)%n
if e>0:
  for i in range(n-e):
    pt.append('z')
col=len(pt)//n
pm=np.array([[0]*col]*n)
for i in range(n):
    for j in range(col):
        pm[i][j]=low.index(pt[n*j+i])
rm=np.dot(k,pm)
for i in range(len(rm)):
    for j in range(len(rm[0])):
        rm[i][j]=rm[i][j]%26
ct=[]
for j in range(len(rm[0])):
    for i in range(len(rm)):
        ct.append(low[rm[i][j]])
print(''.join(ct))

ct=rm
d=int(np.linalg.det(k))
inverse=np.linalg.inv(k)
adj=d*inverse

for i in range(26):
    if((d*i)%26==1):
        d=i
        break
inverse=d*adj
for i in range(n):
    for j in range(n):
        if(inverse[i][j]>=0):
            inverse[i][j]=(inverse[i][j])%26
        else:
            inverse[i][j]=(((inverse[i][j])+26)%26)
rpm=np.dot(inverse,ct)

for i in range(len(rpm)):
    for j in range(len(rpm[0])):
          rpm[i][j]=int(round(rpm[i][j])%26)       
dpt=[]
for j in range(len(rpm[0])):
    for i in range(len(rpm)):
        dpt.append(low[int(rpm[i][j])])
print(''.join(dpt))
