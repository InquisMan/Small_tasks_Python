#Пользователь угадывает число, заданное компьютером. Нужно задать подсказки, чтобы пользователь понимал, ближе он к числу или дальше от него.

import random

i = random.randint(1, 51)
a = int(input('Угадайте число: '))
x = 5

while a != i:
	if a > 50:
		print ('Число вне диапазона')
	elif a == 0:
		print ('Число вне диапазона')
	elif a > i:
		print ('Ваше число больше искомого')
	elif a < i:
		print ('Ваше число меньше искомого')
	if x == 0:
		break
	a = int(input('Угадайте число: '))
	x = x - 1
			
if a != i:
	print ('Количество попыток истекло, вы проиграли!')
elif a == i:
	print ('Вы угадали правильно!: \n', i)
