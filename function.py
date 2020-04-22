import sys
import Libr
import random

# перевод в из 16-ой в 10-ую
def To_teny(x):
    return(int(x,16))

# перевод из 10-ой в 16-ую
def To_sexteen(y):
    if len(hex(y)[2:]) < 2:
        a = '0' + hex(y)[2:]
    else:
        a = hex(y)[2:]
    return (a)

# генерация master - ключа
def key_gen ():
    keymaster = ''
    for i in range(32):
        a = 0
        a = random.randint(0,255)
        a = To_sexteen(a)
        keymaster += str(a)
    return(keymaster)

#разбиение ключа на части

def break_key(keymaster):
    k1 = keymaster[:32]
    k2 = keymaster[32:]
    return k1,k2

# XOR ключа с константами
def xor_key(k1,j):
    currentkey = ""
    for i in range(16):
        l = To_teny(k1[i * 2 :(i + 1) * 2])
        c = To_teny(Libr.C_const[j][i * 2 :(i + 1) * 2])
        m = To_sexteen(l ^ c)
        currentkey += m
    return(currentkey)
