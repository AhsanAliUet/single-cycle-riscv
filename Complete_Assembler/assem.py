# -*- coding: utf-8 -*-
"""
Created on Wed May 25 16:29:13 2022

@author: Ahsan Ali
"""

def lst2str(lst):
    st = ''
    for i in lst:
        st = st + i
    return st

def reg2num(s):
    temp = []
    for i in s:
        if i == 'x':
            continue
        temp.append(i)
    tempNum = lst2str(temp)
    return int(tempNum)

# def dec2bin(n, noOfBits):  #will return a string of a noOfBits-bit binary binary

#     #n is int type    
#     lst = []
#     a = bin(n).replace("0b", "")
#     for i in a:
#         lst.append(i)
        
#     #if len(a) < 5:    #appending zeros at start to make it a noOfBits-bits number
#     for i in range(noOfBits-len(a)):
#         lst.insert(0, '0')
#     # else:
#     #     for i in range(noOfBits-len(a)):
#     #         lst.insert(0, '0')        
#     s = lst2str(lst)
#     return s

def dec2bin(n, bits):  #converts in binary, also takes negative numbers
    s = bin(n & int("1"*bits, 2))[2:]
    return ("{0:0>%s}" % (bits)).format(s)

def hex2bin(num, noOfBits):     #will return a string of a noOfBits-bit binary binary
    
    #num is string type
    int_value = int(num, base=16)
    binValue = str(bin(int_value))[2:].zfill(noOfBits)
    lst = []
    for i in binValue:
        lst.append(i)
        
    return  lst2str(lst)
    
    return  lst2str(lst)
def bitExtractor(imm, froom, too):
    L = len(imm) - 1
    out = imm[L-too:L-froom+1]  #+1 for python
    return out
    
def bitNum(imm, n):  #extracts a specific bit wrt verilog
    l = len(imm) - 1
    return imm[l-n]

#following are done
#R, B, L, S, I, 
s = 'addi x0 x1 1'    #take instruction without commas

def assembler(s):
    lst = s.split(' ')
    print(lst)
    
    
    #Load type
    if (lst[0] == 'lw' or lst[0] == 'lb' or lst[0] == 'lh' or lst[0] == 'lbu' or lst[0] == 'lhu'):
        opcode = '0000011'
        if (lst[0] == 'lb'):
            func3 = '000'
        elif (lst[0] == 'lh'):
            func3 = '001'
        elif (lst[0] == 'lw'):
            func3 = '010'
        elif (lst[0] == 'lbu'):
            func3 = '100'
        elif (lst[0] == 'lhu'):
            func3 = '101'
            
        rd = dec2bin(reg2num(lst[1]), 5)
        imm = dec2bin(int(lst[2]), 12)
        rs1 = dec2bin(reg2num(lst[3]), 5)
        
        machineCode = imm + rs1 + func3 + rd + opcode
        return machineCode
    #S-type
    # sw x2 0 x3 = sw x2, 0(x3)     (content of x3 + 0) = Adress where to write in data memory, contents of x2 = what to write in that address
    elif (lst[0] == 'sw' or lst[0] == 'sh' or lst[0] == 'sb'):
        opcode = '0100011'
        if (lst[0] == 'sb'):
            func3 = '000'
        elif (lst[0] == 'sh'):
            func3 = '001'
        elif (lst[0] == 'sw'):
            func3 = '010'
    
        rs1 = dec2bin(reg2num(lst[3]), 5)
        
        rs2 = dec2bin(reg2num(lst[1]), 5)
        imm = dec2bin(int(lst[2]), 12)
        
        machineCode = bitExtractor(imm, 5, 11) + rs2 + rs1 + func3 + bitExtractor(imm, 0, 4) + opcode
        return machineCode
    #R-type
    elif (lst[0] == 'add' or lst[0] == 'sub' or lst[0] == 'sll' or lst[0] == 'slt' or lst[0] == 'sltu' or lst[0] == 'xor' or lst[0] == 'srl' or lst[0] == 'sra' or lst[0] == 'or' or lst[0] == 'and'):
        opcode = '0110011'
        if (lst[0] == 'add'):
            func3 = '000'
            func7 = '0000000'
        elif (lst[0] == 'sub'):
            func3 = '000'
            func7 = '0100000'
        elif (lst[0] == 'sll'):
            func3 = '001'
            func7 = '0000000'
        elif (lst[0] == 'slt'):
            func3 = '010'
            func7 = '0000000'
        elif (lst[0] == 'sltu'):
            func3 = '011'
            func7 = '0000000'
        elif (lst[0] == 'xor'):
            func3 = '100'
            func7 = '0000000'
        elif (lst[0] == 'srl'):
            func3 = '101'
            func7 = '0000000'
        elif (lst[0] == 'sra'):
            func3 = '101'
            func7 = '0000000'
        elif (lst[0] == 'or'):
            func3 = '110'
            func7 = '0000000'
        elif (lst[0] == 'and'):
            func3 = '111'
            func7 = '0000000'
            
        rd = dec2bin(reg2num(lst[1]), 5)
        rs1 = dec2bin(reg2num(lst[2]), 5)
        rs2 = dec2bin(reg2num(lst[3]), 5)
    
        machineCode = func7 + rs2 + rs1 + func3 + rd + opcode
        return machineCode    

    #B-type
    elif (lst[0] == 'beq' or lst[0] == 'bne' or lst[0] == 'blt' or lst[0] == 'bge' or lst[0] == 'bltu' or lst[0] == 'bgeu'):
        opcode = '1100011'
        if (lst[0] == 'beq'):
            func3 = '000'
        elif (lst[0] == 'bne'):
            func3 = '001'
        elif (lst[0] == 'blt'):
            func3 = '100'
        elif (lst[0] == 'bge'):
            func3 = '101'
        elif (lst[0] == 'bltu'):
            func3 = '110'
        elif (lst[0] == 'bgeu'):
            func3 = '111'
            
        rs1 = dec2bin(reg2num(lst[1]), 5)
        rs2 = dec2bin(reg2num(lst[2]), 5)
        imm = hex2bin(lst[3], 12)
        #imm = imm + '0'  #extra LSB which is always 0, read book page # 407
    
        
        machineCode = bitNum(imm, 12) + bitExtractor(imm, 5, 10) + rs2 + rs1 + func3 + bitExtractor(imm, 1, 4) + bitNum(imm, 11) + opcode
        return machineCode
     
    #I-type
    elif (lst[0] == 'addi' or lst[0] == 'slti' or lst[0] == 'sltiu' or lst[0] == 'xori' or lst[0] == 'ori' or lst[0] == 'andi' or lst[0] == 'slli' or lst[0] == 'srli' or lst[0] == 'srai'):
        opcode = '0010011'
        if (lst[0] == 'addi'):
            func3 = '000'
            rd = dec2bin(reg2num(lst[1]), 5)
            rs1 = dec2bin(reg2num(lst[2]), 5)
            imm = dec2bin(int(lst[3]), 12)
            machineCode = imm + rs1 + func3 + rd + opcode
            return machineCode
        
        elif (lst[0] == 'slti'):
            func3 = '010'
            rd = dec2bin(reg2num(lst[1]), 5)
            rs1 = dec2bin(reg2num(lst[2]), 5)
            imm = dec2bin(int(lst[3]), 12)
            machineCode = imm + rs1 + func3 + rd + opcode
            return machineCode
        
        elif (lst[0] == 'sltiu'):
            func3 = '011'
            rd = dec2bin(reg2num(lst[1]), 5)
            rs1 = dec2bin(reg2num(lst[2]), 5)
            imm = dec2bin(int(lst[3]), 12)
            machineCode = imm + rs1 + func3 + rd + opcode
        
        elif (lst[0] == 'xori'):
            func3 = '100'
            
            rd = dec2bin(reg2num(lst[1]), 5)
            rs1 = dec2bin(reg2num(lst[2]), 5)
            imm = dec2bin(int(lst[3]), 12)
            machineCode = imm + rs1 + func3 + rd + opcode
            return machineCode
        
        elif (lst[0] == 'ori'):
            func3 = '110'
            rd = dec2bin(reg2num(lst[1]), 5)
            rs1 = dec2bin(reg2num(lst[2]), 5)
            imm = dec2bin(int(lst[3]), 12)
            machineCode = imm + rs1 + func3 + rd + opcode
            return machineCode
        
        elif (lst[0] == 'andi'):
            func3 = '111'
            rd = dec2bin(reg2num(lst[1]), 5)
            rs1 = dec2bin(reg2num(lst[2]), 5)
            imm = dec2bin(int(lst[3]), 12)
            machineCode = imm + rs1 + func3 + rd + opcode
            return machineCode
        
        elif (lst[0] == 'slli'):
            func3 = '001'
            func7 = '0000000'
            rd = dec2bin(reg2num(lst[1]), 5)
            rs1 = dec2bin(reg2num(lst[2]), 5)
            shamt = dec2bin(int(lst[3]), 5)  #shift amount
            machineCode = func7 + shamt + rs1 + func3 + rd + opcode
            return machineCode
            
        elif (lst[0] == 'srli'):
            func3 = '101'
            func7 = '0000000'
            rd = dec2bin(reg2num(lst[1]), 5)
            rs1 = dec2bin(reg2num(lst[2]), 5)
            shamt = dec2bin(int(lst[3]), 5)  #shift amount
            machineCode = func7 + shamt + rs1 + func3 + rd + opcode
            return machineCode
            
        elif (lst[0] == 'srai'):
            func3 = '101'
            func7 = '0100000'
            rd = dec2bin(reg2num(lst[1]), 5)
            rs1 = dec2bin(reg2num(lst[2]), 5)
            shamt = dec2bin(int(lst[3]), 5)  #shift amount
            machineCode = func7 + shamt + rs1 + func3 + rd + opcode
            return machineCode
    
    #J-type
    elif (lst[0] == 'jal'):   #jal x10 2
        opcode = '1101111'
        
        rd = dec2bin(reg2num(lst[1]), 5)
        offset = dec2bin(int(lst[2]), 20)
        
        machineCode = bitNum(offset, 20) + bitExtractor(offset, 1, 10) + bitNum(offset, 11) + bitExtractor(offset, 12, 19) + rd + opcode
        return machineCode
    
    #J-type
    elif (lst[0] == 'jalr'):
        opcode = '1100111'
        func3 = '000'
        rd = dec2bin(reg2num(lst[1]), 5)
        rs1 = dec2bin(reg2num(lst[2]), 5) 
        offset = dec2bin(int(lst[3]), 12)
        machineCode = offset + rs1 + func3 + rd + opcode
        return machineCode
    
    #LUI-type
    elif (lst[0] == 'lui'):
        opcode = '0110111'
        rd = lst[1]
        imm = hex2bin(lst[2], 32)
        
        machineCode = bitExtractor(imm, 12, 31) + rd + opcode
        return machineCode
    
    #LUI-type
    elif (lst[0] == 'auipc'):
        opcode = '0010111'
        rd = lst[1]
        imm = hex2bin(lst[2], 32)
        
        machineCode = bitExtractor(imm, 12, 31) + rd + opcode
        return machineCode
    
    


