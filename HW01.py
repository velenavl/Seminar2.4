# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.141.  10-1 ≤ d ≤10-10
# π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) - (4/15) ...
import math


round_value = int(input("введите число (кол-во знаков после запятой): "))

num = str(math.pi)
dot_index = num.index('.')

round_index = dot_index + round_value

if num[round_index+1] >= '5':
    num = str(float(num)+10**-round_value)

print(float(num[:round_index+1]))

print ('\nили')

num = math.pi
num = num + (num % (10**-round_value)) 
num = num * (10**round_value) 
num = num//1 
num = num / 10**round_value
print(num)


print ('\nпроверка round')
print(round(math.pi,round_value))