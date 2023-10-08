drone_list = ["DJi Mavic 2 Pro", "DJI Mavic 2 Zoom", "DJI Mavic 2 Enterprise Advanced", "AUTEL Evo II Pro",
			  "DJI Mini 2", "Autel Evo Nano", "Autel Evo Lite Plus", "Parrot Anafi", "Dji Inspire 2",
			  "DJI Mavic 3", "DJI Mavic Air2s", "Ryze Tello", "Eachine Trashcan"]

drone_weight_list = [903, 900, 920, 980, 249, 249, 600, 540, 1500, 1000, 570, 130, 110]

#в drone по очереди попадает каждый дрон из списка drone_list
#for drone in drone_list:
	#print(drone)

#TODO1
#выведите все дроны производителя, название которогоDjведет пользователь через input, и подсчитайте их количество. 
#учтите, что:
#1) DJI и Dji - это один и тот же производитель! такие случаи тоже должны обрабатываться
#2) при выводе исправьте название производителя, если допущена ошибка. как правильно писать производителей: DJI, Autel

def TODO1():
	count = 0
	name = input("Enter the name of the manufacturer: ").lower().strip()
	for drone in drone_list:
		drone=drone.strip().split()
		if drone[0].lower() ==name:
			if drone[0].lower() =='dji':
				drone[0] = drone[0].upper()
			else: drone[0]== drone[0].capitalize()
			print(" ".join(drone))
			count+=1
	print("Number of drones: ", count)

#TODO2
#1) подсчитайте количество моделей дронов каждого производителя из списка drone_list. производители: DJI, Autel, Parrot, Ryze, Eachine
#2) подсчитайте количество моделей дронов второй версии (содержащих в названии "2" или "II") - ответ 7

def TODO2():
	c = {"DJI":0,"Autel":0,"Parrot":0,"Ryze":0,"Eachine":0}
	count=0
	for drone in drone_list:
		drone=drone.strip().split()
		if drone[0].lower()=="dji":
			c["DJI"]+=1
		else:
			drone[0]=drone[0].capitalize()
			c[drone[0]] += 1
		if "2" in drone or "II" in drone:
			count+=1
	print(c)
	print("Models with 2:", count)


#TODO3
#выведите все дроны из списка, которые нужно регистрировать, и подсчитайте их количество.
#напоминание: регистрировать нужно все дроны массой более 150 г
#сделайте то же самое для всех дронов, которые не нужно регистрировать
#для этого вам нужно параллельно обрабатывать два списка: drone_list и drone_weight_list:
#как работает zip, мы разберем на лекции про списки. пока что просто пользуйтесь (в drone будет модель, в weight - ее вес)

def TODO3():
	for drone, weight in zip(drone_list,  drone_weight_list):
		if weight >=150:
			print("Need to register: ","".join(drone))
		else: print("Not need to register: ", "".join(drone))

#TODO4
#для каждого дрона из списка выведите, нужно ли согласовывать полет при следующих условиях:
#высота 155 м, полет вне населенного пункта, вне закрытых зон, в прямой видимости
#помните, что для дронов тяжелее 150 г согласовывать полет над населенным пунктом - обязательно!

def TODO4():
	height = 100
	local = True
	close= False
	visible = True

	for drone, weight in zip(drone_list,  drone_weight_list):
		if weight < 150 or (not local and height < 155 and not close and visible):
			print(drone,"Does not require flight approval")
		else:
			print(drone, "Requires flight approval")
		
#TODO5
#модифицируйте решение задания TODO1:
#теперь для введенного пользователем производителя вы должны вывести строку, содержащую перечисление моделей и БЕЗ названия производителя.
#например, пользователь ввел "Autel". ваша программа должна вывести вот такой результат: "Evo II Pro, Evo Nano, Evo Lite Plus". для этого вам понадобится несколько функций работы со строками. решить эту задачу можно несколькими разными способами
#производители те же: DJI, Autel, Parrot, Ryze, Eachine

def TODO5():
	name = input("Enter the name of the manufacturer: ").lower().strip()
	for drone in drone_list:
		drone=drone.strip().split()
		if drone[0].lower() == name:
			print(" ".join(drone[1:]))

