from os import system as cmd
dirn = int(input('Введите номер ДЗ: '))
cmd(f'mkdir C:\\Users\\ASUS\\Desktop\\AADSIP\\DZ{dirn}')
cmd(f'cd C:\\Users\\ASUS\\Desktop\\AADSIP\\DZ{dirn}')
pcmd = input('Введите команду: ')
if pcmd == 'add':
	for i in range(10):
		cmd(f'echo  > C:\\Users\\ASUS\\Desktop\\AADSIP\\DZ{dirn}\\task_{i}.py')
	cmd(f'del C:\\Users\\ASUS\\Desktop\\AADSIP\\DZ{dirn}\\task_0.py')
else:
	print('Такой команды нет!')