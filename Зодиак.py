#Знак зодиака по дате рождения.


x = int(input('Введите день вашего рождения: '))
y = int(input('Введите номер месяца вашего рождения: '))

if (21 <= x <= 31 and y == 3) or (1 <= x <= 20 and y == 4):
	print (' ')
	print ('Ваш знак зодиака овен')
elif (21 <= x <= 30 and y == 4) or (1 <= x <= 20 and y == 5):
	print (' ')
	print ('Ваш знак зодиака телец')
elif (21 <= x <= 30 and y == 5) or (1 <= x <= 20 and y == 6):
	print (' ')
	print ('Ваш знак зодиака близнецы')
elif (21 <= x <= 30 and y == 6) or (1 <= x <= 22 and y == 7):
	print (' ')
	print ('Ваш знак зодиака рак')
elif (23 <= x <= 31 and y == 7) or (1 <= x <= 22 and y == 8):
	print (' ')
	print ('Ваш знак зодиака лев')
elif (23 <= x <= 31 and y == 8) or (1 <= x <= 23 and y == 9):
	print (' ')
	print ('Ваш знак зодиака дева')
elif (24 <= x <= 30 and y == 9) or (1 <= x <= 23 and y == 10):
	print (' ')
	print ('Ваш знак зодиака весы')
elif (24 <= x <= 31 and y == 10) or (1 <= x <= 21 and y == 11):
	print (' ')
	print ('Ваш знак зодиака скорпион')
elif (22 <= x <= 30 and y == 11) or (1 <= x <= 21 and y == 12):
	print (' ')
	print ('Ваш знак зодиака стрелец')
elif (22 <= x <= 31 and y == 12) or (1 <= x <= 19 and y == 1):
	print (' ')
	print ('Ваш знак зодиака козерог')
elif (22 <= x <= 31 and y == 1) or (1 <= x <= 18 and y == 2):
	print (' ')
	print ('Ваш знак зодиака водолей')
elif (19 <= x <= 28 and y == 2) or (1 <= x <= 20 and y == 3):
	print (' ')
	print ('Ваш знак зодиака рыбы')
