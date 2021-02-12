# Список (list)

# Создание пустого списка 
list_my = []
list_my_2 = list()

# добавление обьекта 
list_my.append(100)
list_my.append(35)
list_my.append("Hi da")

# обращение к элементам списка
list_my[0] = 10
list_my[-2] = "OOOO"

# чтение значений
el_value = list_my[0]

# удаление элемента 
# del list_my[-2]


# list_my.remove(3)

# a = list_my.pop(0)

# создание заполненного списка

list_my_2 = [2, 6, 8, 'ssaas', "kuk", 3.14, [493943], True]

# "длина" списка -  кол-во элементов
# print(len(list_my_2))

# создание списка из строки

s = "Hi, kuk. how are u?"
popFrom = list(s)

# print(popFrom)


# методы списка

# представление
x = [1, 3, 5, 7, 9, 11]

y = x 

# y[2] = 20

# копия
z = x.copy()

z[2] = 30

# print(f"x: {x}; z: {z}")

# срез списка

my = [1, 2, 3, 4, 5, 6, 7]

# прямой срез
slice_1 = my[1:4]

slice_1 = my[2:]

slice_1 = my[::2]

slice_1 = my[1:6:2]

# обратный срез
slice_2 = my[-1::-1]

slice_2 = my[-3:-6:-1]

# print(slice_2)

# Кортеж (tuple)

# неизменяемая (inmuteble) коллекция

my_tuple = (20, 40, 60, 90, 30, 20, 70)

el = my_tuple[-1]

# нельзя делать срез кортежей
el = my_tuple[-1:-2:-1]

# нельзя удалять значения  
# нельзя менять значения
# нельзя добавлять элемент

# print(el)


# Словарь (dictionary)

# Создание словаря

my_dict = {1 : 193, 2:286, 3:500}
my_dict_2 = {'aaoooaoao':20, "mama":'pipi', 'toto':[3, 4 , 6, 8], 20:200}

# чтение данных 
item = my_dict_2[20]
item = my_dict_2['aaoooaoao']

# пример примения словаря в качкстве альтернативы условным операторам
con = 'gay_2'
g = {'gay_1':283, 'gay_2': 293}

# Изменение значения
my_dict_2['mama'] = 'popo'

# удаление элемента
del my_dict_2['aaoooaoao']

# добавление нового элемента
my_dict_2["newGay"] = 999

# проблема со стением значений 
# val = my_dict_2["ku_2"]

# решение проблемы
# val = my_dict_2.get("newGay")
val = my_dict_2.get("ku", 0)

# print(val) 


#  Обновление данных 

d_l = {'d':250, "pipi": 10, 'sss':40, 'r': 70}

d_k = {'r':100, 'd':35}
d_k_2 = {'r':444, "q":666}

# d_l.update(g_k)
d_l.update(d_k_2)

print(d_l)