from math import factorial as fact

def factorial(numStr):
    try:
        n = int(numStr)
        r = str(fact(n))
    except:
        r = 'Error!'
    return r

def decToBin(numStr):
    try:
        n = int(numStr)
        r = bin(n)[2:]
    except:
        r = 'Error!'
    return r

def binToDec(numStr):
    try:
        n = int(numStr, 2)
        r = str(n)
    except:
        r = 'Error!'
    return r

def decToRoman(numStr):
    try:
        n = int(numStr)
    except:
        return 'Error!'
    
    if n>= 4000:
        return 'Error!'
    
    romans = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'),
         (100, 'C'),  (90, 'XC'),  (50, 'L'),  (40, 'XL'),
          (10, 'X'),   (9, 'IX'),   (5, 'V'),   (4, 'IV'),
           (1, 'I')
    ]

    result = ''
    for value, letters in romans:
        while n >= value:
            result += letters
            n -= value
    
    return result

def romanToDec(numStr):
    if numStr.isnumeric() == True:
        return "This is number!"

    romans = [
        (1, 'I'), (4, 'IV'), (5, 'V'), (9, 'IX'),
        (10, 'X'), (40, 'XL'), (50, 'L'), (90, 'XC'),
        (100, 'C'), (400, 'CD'), (500, 'D'), (900, 'CM'),
        (1000, 'M')
    ]

    rom_list = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    for i in range(len(numStr)):
        if numStr[i] not in rom_list:
            return "Unexpected!"

    idx = len(numStr)
    result = 0
    check_num = 1

    while True:
        roman_char = numStr[idx-1]
        idx -= 1
        for i in romans:
            if roman_char == i[1]:
                roman_num = i[0]
                break
        if check_num > roman_num:
            result -= roman_num
        else:
            result += roman_num
        if idx == 0:
            break
        check_num = roman_num

    return str(result)