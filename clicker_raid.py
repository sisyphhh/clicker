#clicker raid
#клик по координатам
#проверка цвета по координатам 
#время клика
#время останова
#интерфейс qt
import pyautogui as pg
import time
import mouse


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

def START_session():
	print("Choose the position you need by cursor and right-click on it.\n")
	while True:
		if mouse.is_pressed(button='right'):#left
			print('Gotcha')
			x,y=choose_posintion()
			return x,y
			##break

def STOP_session(flag):
	if flag == '1':
		return True,'Restart'
	elif flag == '2':
		return True,'Continue'
	else:
		return False,'Stop'


#'''
						#########################
						## The body of program ##
						#########################
#'''


x,y=START_session()
#time.sleep(4)

STARTER=True
##	Restart=new(coord + clicks number + time interval);	Continue=new(clicks number + time interval)
START_Type='Continue'
while STARTER:
	#print('here we are 1')
	if START_Type == 'Continue':
		Number=int(input("Put a Number of 1-clicks ",))#sec
		timer3=int(input("Put a time-intervals between clicks ",))#sec	
	elif START_Type == 'Restart':
		x,y=START_session()
		Number=int(input("Put a Number of 1-clicks ",))#sec
		timer3=int(input("Put a time-intervals between clicks ",))#sec
	print()
	#print('here we are 2')
	#ans = input()
	##Номерной блок, зависящий от кол-ва кликов и временными интервалами между ними 
	while Number:# пока текущее время < Времени окончания делаем клики
		print("%d click left"%(Number))
		#time.sleep(timer3)
		pg.click(x, y)
		chetchick(timer3)
		Number-=1

	print('Time is over for this Session\n')
	print('Do you want to Restart/Continue or end Session?\nEnter - 1/2/smth else\n')
	ans = input()
	STARTER, START_Type = STOP_session(ans)
	print(STARTER)


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
