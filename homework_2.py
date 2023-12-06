# =====================================
# ЗАДАНИЕ 1: Работа с файлами
# =====================================
# TODO 1-1
#  Прочитайте данные из файла pilot_path.json (лекция 9)

# ВАШ КОД:

import json 

with open("pilot_path.json") as json_file:          #def read_json
    json_data=json.load(json_file)
print(json_data, "\n")

# =====================================
# ЗАДАНИЕ 2: Расчет статистик
# =====================================
# TODO 2-1) Подсчитайте, сколько миссий налетал каждый пилот. Выведите результат в порядке убывания миссий
# ИНФОРМАЦИЯ:
# структура данных в файле: {"имя_пилота": "список_миссий":[миссия1, ...]]
# структура одной миссии: {"drone":"модель_дрона", "mission":[список точек миссии]}
# у пилотов неодинаковое количество миссий (и миссии могут быть разной длины). у каждой миссии - произвольная модель дрона
# РЕЗУЛЬТАТ:
# Пилоты в порядке возрастания количества миссий: {'pilot1': 1, 'pilot4': 2, 'pilot9': 3, 'pilot5': 3, 'pilot7': 4, 'pilot6': 5, 'pilot2': 5, 'pilot3': 6, 'pilot8': 6}

# ВАШ КОД:
missions_count_by_pilots = {}
for pilot in json_data.keys():                      #def missions_by_pilots
    missions = json_data[pilot]["missions"]         #def missions_by_pilot
    missions_count_by_pilots[pilot] = len(missions)
pilots_missions_count=dict(sorted(missions_count_by_pilots.items(), key=lambda item: item[1]))
print(pilots_missions_count, "\n")

# TODO 2-2) Получите и выведите список всех моделей дронов, которые были в файле pilot_path.json
# Подсказка: внутри print используйте str.join(), чтобы соединить элементы списка (множества)

# ПРИМЕР РЕЗУЛЬТАТА:
# Полеты совершались на дронах следующих моделей: DJI Mavic 2 Pro, DJI Mavic 3, DJI Inspire 2, DJI Mavic 2 Zoom, DJI Mavic 2 Enterprise Advanced       
            
# ВАШ КОД:

models = []
drones_missions_dict={}
for pilot in json_data.keys():                     
    missions=json_data[pilot]["missions"]            #def missions_by_pilot
    for mission in missions:                         #def missions_by_drones
        drone = mission["drone"]
        if not drone in drones_missions_dict.keys():
            drones_missions_dict[drone]=[]
        drones_missions_dict[drone].append(mission["mission"])
drones_missions=drones_missions_dict 
for drone in drones_missions.keys():                #def types
    if not drone in models:
        models.append(drone)
print(f'Полеты совершались на дронах следующих моделей: {", ".join(models)}', "\n")

# TODO 2-3) Получите список миссий для каждой модели дронов, которые были в файле pilot_path.json,
# и выведите на экран модель дрона и количество миссий, которые он отлетал

# ПРИМЕР РЕЗУЛЬТАТА:
# Дрон DJI Inspire 2 отлетал 6 миссий
# Дрон DJI Mavic 2 Pro отлетал 6 миссий
# Дрон DJI Mavic 2 Enterprise Advanced отлетал 10 миссий
# Дрон DJI Mavic 3 отлетал 4 миссий
# Дрон DJI Mavic 2 Zoom отлетал 9 миссий

# ВАШ КОД:

answer = {}
for drone in drones_missions.keys():
    answer[drone] = len(drones_missions[drone])
drones_missions_count=answer
for drone in drones_missions_count.keys():             #def count_missions
    print(f"Дрон {drone} отлетал {drones_missions_count[drone]} миссий", "\n")

# TODO 3) Оформите задания из TODO 1 и 2 в виде функций
# ВАШ КОД:

def read_json(filename):

    with open(filename) as json_file:
        data = json.load(json_file)
    
    return data

def missions_by_pilot(pilot, data):
    return data[pilot]["missions"]

def missions_by_pilots(data):
    missions_count_by_pilots = {}
    for pilot in data.keys():
        missions = missions_by_pilot(pilot, data)
        missions_count_by_pilots[pilot] = len(missions)

    return dict(sorted(missions_count_by_pilots.items(), key=lambda item: item[1], reverse=True))

def missions_by_drones(data):
    drones_missions_dict = {}
    for pilot in data.keys():
        missions = missions_by_pilot(pilot, data)
        for mission in missions:
            drone = mission["drone"]
            if not drone in drones_missions_dict.keys():
                drones_missions_dict[drone] = []    
            drones_missions_dict[drone].append(mission["mission"])
    return drones_missions_dict 

def types(data):
    models = []
    drones_missions = missions_by_drones(data)
    for drone in drones_missions.keys():
        if not drone in models:
            models.append(drone)
    return models           

def count_missions(data):

    drones_missions = missions_by_drones(data)
    result = {}

    for drone in drones_missions.keys():
        result[drone] = len(drones_missions[drone])

    return result    

print("Через функции:", "\n")
#1-1
filename = "pilot_path.json"
json_data = read_json(filename)
print(json_data, "\n")
#2-1
pilots_missions_count = missions_by_pilots(json_data)
print(pilots_missions_count, "\n")
#2-2
models = types(json_data)
print(f'Полеты совершались на дронах следующих моделей: {", ".join(models)}', "\n")
#2-3
drones_missions_count = count_missions(json_data)
for drone in drones_missions_count.keys():
    print(f"Дрон {drone} отлетал {drones_missions_count[drone]} миссий", "\n")