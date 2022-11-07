# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
#  Пример:
# k=2 => 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

from os import path
from random import randint

def string_gen (list_factor): 
    k = len(list_factor)-1
    string_write = str(list_factor[0])
    for i in range (1,k+1): 
        string_write = str(list_factor[i]) + 'x^' + str(i) + ' + ' + string_write
    return string_write

def polynomial_gen (file_name = "file.txt"): 
    k = int(input("введите число (натуральная степень): "))
    file = open(file_name, 'w')
    list_factor = [randint(0,100) for i in range (k+1)]

    string_write = string_gen(list_factor)
    
    file.write(string_write)
    file.close()


    print (f"в файл '{path.abspath(file_name)}' записано - {string_write}")


if __name__ == '__main__':
    polynomial_gen ()