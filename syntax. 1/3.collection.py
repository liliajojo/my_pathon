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

print(f"x: {x}; z: {z}")
















