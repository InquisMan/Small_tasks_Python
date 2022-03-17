#Вывод последовательности до тех пор, пока не найдётся k


import random

x = []
k = 69
c = 0

for i in range(100):
	while k not in x:	
		x.append(random.randint(10, 70))
		c = c + 1
print (*x)
print (' ')
print ('Шагов до k: ', c)
