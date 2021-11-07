import random

def bin_search(array, value):

	left = 0
	right = len(array) - 1
	pos = len(array) // 2

	while array[pos] != value and left <= right:

		if value > array[pos]:
			left = pos + 1
		else:
			right = pos - 1

		pos = (left + right) // 2

	return -1 if left > right else pos

a = [random.randint(0, 1000) for _ in range(100)]
a.sort()
print(a)

n = int(input('Введите какой элемент найти: '))
print(bin_search(a, n))


import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

arr_below = []
arr_lager = []

for item in array:

	if item > 0:
		arr_lager.append(item)
	elif item < 0:
		arr_below.append(item)

print(f'{arr_below}\n{arr_lager}')


import random

array = [random.randint(-100, 100) for _ in range(100)]
print(array)

a = int(input('\nВведите число для вставки: '))
b = int(input('\nНа какое место поставить: '))

array.append(None)
i = len(array) - 1

while i > b:
	array[i], array[i - 1] = array[i - 1], array[i]
	i -= 1

array[b] = a
print('\n', array)