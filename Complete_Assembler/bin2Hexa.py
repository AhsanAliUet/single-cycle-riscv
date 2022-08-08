# -*- coding: utf-8 -*-
"""
Created on Mon Aug  8 17:26:48 2022

@author: Ahsan Ali
"""

#%%
file1 = open("machineCodeInBinary.txt", "r")
file2 = open("machineCodeInHex.txt", "w")

for i in file1:
    num = hex(int(i, 2))
    num = num + '\n'
    file2.writelines(num)
    
