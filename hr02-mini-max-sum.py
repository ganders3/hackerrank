#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 12:32:36 2022

@author: gregory
"""

import math

arr = [1,2,3,4,5]

n = len(arr)
sumAll = sum(arr)
minSum = math.inf
maxSum = -math.inf

for i in arr:
    val = sumAll - i
    if val > maxSum:
        maxSum = val
    if val < minSum:
        minSum = val

print(minSum, maxSum)