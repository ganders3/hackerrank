#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 12:21:22 2022

@author: gregory
"""

arr = [1,1,0,-1,-1]

nPos = 0
nNeg = 0
nZer = 0

for i in arr:
    if i > 0:
        nPos += 1
    elif i < 0:
        nNeg += 1
    else:
        nZer += 1

n = len(arr)
rPos = nPos/n
rNeg = nNeg/n
rZer = nZer/n

print("%.6f" % rPos)
print("%.6f" % rNeg)
print("%.6f" % rZer)