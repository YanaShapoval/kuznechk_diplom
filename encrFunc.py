import sys
import SL_function
import function

# Шифрование пакета данных
def encr(roundkey,edata):
    for i in range(10):
        edata = SL_function.xor_func(roundkey[i], edata)
        edata = SL_function.func_S(edata)
        edata = SL_function.func_L(edata)
    return(edata)

# чтение данных из файла
def fail_func(filename):
    instr = ''
    data =''
    f = open(filename,'r')
    instr = f.read(47)
    for j in range (47):
        if instr[j] != ' ':
            data += instr[j]
    return(data)

#запись шифротекста в файл
def in_file(filename,edata):
    f = open(filename,'a')
    f.write(edata + '\n')
    f.close
    return(0)

# обработка выводимых данных
def add_space(edata):
    outstr = ''
    for i in range(32):
        outstr += edata[i]
        if (i % 2) != 0:
            outstr += ' '
    return(outstr)

# оновная фуекция реализующая шифрование
def main(filename):
    ekey = SL_function.create_key()
    edata = fail_func(filename)
    edata = encr(ekey,edata)
    #in_file(filename,edata)
    edata = add_space(edata)
    in_file(filename,edata)
    return(0)

main(sys.argv[1])
