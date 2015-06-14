__author__ = 'sen'

def isHappy(n):
    buff = []
    goal = [100,10,1]
    while(True):
        strn = str(n)
        n = 0
        for i in range(0,len(strn)):
            n = n + int(strn[i])**2
        if n in goal :
            print buff
            return True
        elif n in buff :
            print buff
            return False
        else :
            buff.append(n)

print isHappy(132)
