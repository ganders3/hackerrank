#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 17 11:47:46 2022

@author: gregory
"""

s = ['aba', 'baba', 'aba', 'xzxb']
q = ['aba', 'xzxb', 'ab']

def matchingStrings(strings, queries):
    arr = [strings.count(i) for i in queries]
    return(arr)
        
matchingStrings(s, q)