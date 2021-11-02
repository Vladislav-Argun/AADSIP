'''
Автор скрипта: Vladislav-Argun
Ссылка на Git: https://github.com/Vladislav-Argun/AADSIP.git
'''

# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6. 
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.
a = 5 & 6
b = 5 | 6
c = 5 ^ 6

print(a, b, c)

# 2. По введенным пользователем координатам двух точек вывести 
# уравнение прямой вида y = kx + b, проходящей через эти точки.
x1 = int(input('Введите координаты 1-ой точки по оси x: '))
x2 = int(input('\nВведите координаты 1-ой точки по оси y: '))
y1 = int(input('\nВведите координаты 2-ой точки по оси x: '))
y2 = int(input('\nВведите координаты 2-ой точки по оси y: '))

a = y1 - y2
b = x1 - x2
c = x1 * y2 - x2 * y1

if a == 0 & b == 0:
	print('\nТочки совпадают!')
elif a == 0:
	print(f'{b}y + {c} = 0')
elif b == 0: 
	print(f'{a}x + {c} = 0')
else:
	print(f'{a}x + {b}y + c = 0')

# 3. Написать программу, которая генерирует в указанных пользователем границах:
# a. случайное целое число,
# b. случайное вещественное число,
# c. случайный символ.
# Для каждого из трех случаев пользователь задает свои границы диапазона. 
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. 
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

import random

cmd = input('Выберите один из вариантов:\na) случайное целое число\nb) случайное вещественное число\nc) случайный символ\nВведите название пункта: ')
cmd = cmd.lower()
if cmd == 'a':
	a1 = int(input('Введите целое число 1: '))
	a2 = int(input('Введите целое число 2: '))

	a = random.randint(a1, a2)

	print(f'Результат: {a}')
elif cmd == 'b':
	b = random.uniform(b1, b2)
	print(f'Результат: {b}')
elif cmd == 'c':
	c = chr(random.randint(ord(ch1), ord(ch2)))
	print(f'Результат: {c}')


# 4. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят, 
# и сколько между ними находится букв.
char_1 = input('Ведите первую прописную букву латинского алфавита: ')
char_2 = input('Ведите вторую прописную букву латинского алфавита: ')

position_1 = ord(char_1) - 96
position_2 = ord(char_2) - 96
distance = abs(position_1 - position_2) - 1
print(f'Буква "{char_1}" {position_1}-я в алфавите\n'
      f'Буква "{char_2}" {position_2}-я в алфавите\n'
      f'Между буквами {distance} букв')
'''
https://www.asciitable.com/
Если вы проверите сами, порядковый номер a равен 97 
(ссылка, которую я разместил выше, покажет полный набор символов ASCII.) 
Каждая буква нижнего регистра находится в диапазоне 97-122 (26 символов.) 
Итак, если вы просто вычтете 96 из порядкового номера любой строчной буквы, 
вы получите ее положение в алфавите.
'''

# 5. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
num = int(input('Введите номер буквы в латинском алфавите: '))
print(chr(num + 96))

# 6. По длинам трех отрезков, введенных пользователем,
# определить возможность существования треугольника, составленного из этих отрезков. 
# Если такой треугольник существует, то определить, 
# является ли он разносторонним, равнобедренным или равносторонним.
print('Введите длины трех отрезков:')
a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))

if a + b >= c and a + c >= b and b + c >= a:
    if a == b or b == c or c == a:
        if a == b and a == c:
            print('Треугольник равносторонний')
        else:
            print('Треугольник равнобедренный')
    else:
        print('Треугольник разносторонний')
else:
    print('Это не треугольник')

# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.
year = int(input('Введите год: '))
if year % 4 == 0:
	print(f'{year}г. является високосным.')

# 8. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).
n1 = int(input('Введите число 1: '))
n2 = int(input('Введите число 2: '))
n3 = int(input('Введите число 3: '))

result = n1 + n2 + n3 - max(n1, n2, n3) - min(n1, n2, n3)

print(f'{result} - среднее число')