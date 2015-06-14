__author__ = 'sen'

test = "MMCDLXVII"

def romanToInt(s):
    res = 0
    temp_I,temp_X,temp_C,temp_M = 0,0,0,0

    if(s.find("CM")!=-1):
        res = res + 900
        temp_C = temp_C+1
        temp_M = temp_M+1
    if(s.find("XC")!=-1):
        res = res + 90
        temp_X = temp_X+1
        temp_C = temp_C+1
    if(s.find("IX")!=-1):
        res = res + 9
        temp_I = temp_I+1
        temp_X = temp_X+1
    if(s.find("CD")!=-1):
        res = res + 400
        temp_C = temp_C+1
    elif(s.find("D")!=-1):
        res = res + 500
    if(s.find("XL")!=-1):
        res = res + 40
        temp_X = temp_X+1
    elif(s.find("L")!=-1):
        res = res + 50
    if(s.find("IV")!=-1):
        res = res + 4
        temp_I = temp_I+1
    elif(s.find("V")!=-1):
        res = res + 5

    res = res + (s.count('M')-temp_M)*1000
    res = res + (s.count('C')-temp_C)*100
    res = res + (s.count('X')-temp_X)*10
    res = res + (s.count('I')-temp_I)*1

    return res

print romanToInt(test)