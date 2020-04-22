import Libr
import function

# функция нелинейного преобразования
def func_S(Xk1):
    sres = ""
    for i in range(16):
        x = Libr.DeskEncr[function.To_teny(Xk1[i * 2:(i + 1) * 2])]
        x = function.To_sexteen(x)
        sres += x
    #print(sres)
    return(sres)

# функция линейного преобразования
def func_L(currentkey):
    key = ""
    for j in range (16):
        a = function.To_teny(currentkey[0:2])
        val = a & Libr.line_conver[0]
        for i in range (1,16):
            a = function.To_teny(currentkey[i * 2: (i + 1) * 2])
            val = val ^ (a & Libr.line_conver[i])
        #    print('val',i,val)
        #    print('valSX',i,function.To_sexteen(val))
        key += function.To_sexteen(val)
        if len(key) < 32:
            key = '0' * (32 - len(key)) + key
        elif len(key) > 32:
            key = key [len(key) - 32:]
        currentkey = key
    return(key)

# XOR
def xor_func (x,y):
    res = ""
    for i in range (16):
        a = function.To_teny(x[i * 2: (i + 1) * 2])
        b = function.To_teny(y[i * 2: (i + 1) * 2])
        res = res + function.To_sexteen(a ^ b)
    return(res)

# ключ на выходе из ячейки
def stic_key(r, currentkey):
    return(r + currentkey)

# тело программы
def create_key():
    key = function.key_gen()
    roundkey = []
    for i in range (5):
        k1,k2 = function.break_key(key)
        k1 = function.xor_key(k1,i)
        k1 = func_S(k1)
        k1 = func_L(k1)
        k1 = xor_func(k1,k2)
        key = stic_key(k2,k1)
        roundkey.append(k1)
        roundkey.append(k2)
    #print(roundkey)
    return(roundkey)
create_key()
