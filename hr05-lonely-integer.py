#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 12:02:22 2022

@author: gregory
"""

arr = [1,2,3,4,3,2,1]

def lonelyInteger(a):
    unique = list(set(a))
    for i in unique:
        if a.count(i) == 1:
            return(i)
    
lonelyInteger(arr)