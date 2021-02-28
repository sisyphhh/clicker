#clicker raid
#клик по координатам
#проверка цвета по координатам 
#время клика
#время останова
#интерфейс qt
import pyautogui as pg
import time
import mouse

print("Choose the position you need by cursor and click on it.\n")


def choose_posintion():
	x,y=pg.position()
	print('x =',x,', y =',y)
	return x,y

def chetchick(timer111):
	while timer111:
		print(timer111)
		timer111-=1
		time.sleep(1)
	print()

def stop_session(flag):
	if flag == 'n':
		return 0
	else:
		return 1


while True:
	if mouse.is_pressed(button='left'):
		print('Gotcha')
		x,y=choose_posintion()
		break

#time.sleep(4)

STARTER=True
while STARTER:
	Number=int(input("Put a Number of 1-clicks ",))#sec
	timer3=int(input("Put a time-intervals between clicks ",))#sec
	print()

	#Номерной блок, зависящий от кол-ва кликов и временными интервалами между ними 
	while Number:# пока текущее время < Времени окончания делаем клики
		print("%d click left"%(Number))
		#time.sleep(timer3)
		pg.click(x, y)
		chetchick(timer3)
		Number-=1

	print('Time is over for this Session')
	print('Do you want to continue y/n?\n')
	ans = input()
	STARTER=stop_session(ans)


#временной блок, зависящий от времени окончания и временными интервалами между кликами
'''
#перевод времени работы программы из секунд в минуты
finish=time.localtime()[3:6]#cortezh consist of ()
print(finish)

while :# пока текущее время < Времени окончания делаем клики
	time.sleep(timer3)
	pg.click(x, y)
	now=time.localtime()[3:6]

print('time is over')

#
#a=time.localtime()
#a
#
#time.strftime('%A',a)
#pg.click(x=100, y=200)
#time.sleep(1)
'''
