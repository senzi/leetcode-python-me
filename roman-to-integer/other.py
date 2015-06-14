__author__ = 'sen'


def romanToInt(s):

    res = 0 + s.count('M') * 1000 \
            + s.count('C') * 100 \
            + s.count('X') * 10 \
            + s.count('I')

    if   'CM'in s: res -= 200
    elif 'CD'in s: res += 300
    elif 'D' in s: res += 500

    if   'XC'in s: res -= 20
    elif 'XL'in s: res += 30
    elif 'L' in s: res += 50

    if   'IX'in s: res -= 2
    elif 'IV'in s: res += 3
    elif 'V' in s: res += 5

    return res


print romanToInt("DCXXI")
