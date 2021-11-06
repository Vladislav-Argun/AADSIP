# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,… 
# Количество элементов (n) вводится с клавиатуры.
row = 1
i = 1
result = 1
n = int(input('Введите кол-во: '))
while i != n:
	i += 1
	row *= 0.5
	if i % 2 == 0:
		result = result - row
	else:
		result = result + row
print(result)