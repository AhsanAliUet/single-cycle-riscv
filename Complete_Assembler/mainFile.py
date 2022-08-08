# -*- coding: utf-8 -*-
"""
Created on Wed May 25 15:39:13 2022

@author: Ahsan Ali
"""

from assem import assembler   #this will read from the file where assembler actually is

def rem_last_2(string):   #removes newline character at the end of string
    s = ''
    if (string[len(string)-1] == '\n'):
        
        for i in range(len(string)-1):
            s = s + string[i]
        return s
    else:
        return string

def add_last_2(string): #adds a new line character at the end of string
    s = '\n'
    return string + s    #concatenation
    


file1 = open('assemblyFile.txt', 'r')  #file from which assembly code will be read which to be converter to equivalent machine code  
file2 = open('machineCodes.txt', 'w')  #file in which machine codes are to be written
file3 = open('machineCodeInBinary.txt', 'w')  #file in which machine codes are to be written

for i in file1:
    assemIns = rem_last_2(i)
    machine_code_generated = assembler(assemIns)
    real_machine_code = add_last_2(machine_code_generated)
    file2.writelines(real_machine_code)
    file3.writelines(real_machine_code)

file1.close()
file2.close()
file3.close()

print("\nMachine Code succesfully written in file machineCodes.txt")
    
#Converting the binary code to hexadecimal also, in the code below
file4 = open('machineCodeInBinary.txt', 'r')  
file5 = open("machineCodeInHex.txt", "w")



for i in file4:
    num = hex(int(i, 2))
    num = num + '\n'
    file5.writelines(num)
    
file4.close()
file5.close()
