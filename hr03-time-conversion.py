#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 15 12:47:36 2022

@author: gregory
"""


import math
import os
import random
import re
import sys

s = '12:05:45PM'

pattern = "^\d{2}:\d{2}:\d{2}PM$"
x = re.search(pattern, s)

txt = re.sub("[AP]M", "", s)

if x:
    split_txt = re.split(":", txt, 1)
    hr = str((int(split_txt[0]) % 12) + 12)
    txt = hr + ":" + split_txt[1]
else:
    txt = re.sub("^12", "00", txt)
    
print(txt)