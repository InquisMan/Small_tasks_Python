#По номеру месяца определить, какое время года.


x = int(input('Введите номер месяца: '))

if x == 12 or x == 1 or x == 2:
	print (' ')
	print ('зима')
elif x == 3 or x == 4 or x == 5:
	print (' ')
	print ('весна')
elif x == 6 or x == 7 or x == 8:
	print (' ')
	print ('лето')
elif x == 9 or x == 10 or x == 11:
	print (' ')
	print ('осень')
