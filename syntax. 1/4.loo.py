#  Циклы (операторы циклов)

# Оператор цикла while
# while True:
#    print("Hi")

# бесконечный цикл с прерыванием 
 #while True:
 #   in_date = input("Введите что-нибудь: ")
  #  if in_date == "pipi":
  #      print("I'm tried")
  #      break
  #  print("Hui")

# Цикл с условием

num = 0

#while num <= 10:
#    print(f"Num: {num}")
    #num = num + 1
 #   num += 2

number = 10

# while number > 0:
   # print(f"Number: {number}")
  #  number -= 2

# цикл с условием и с прерыванием 

pipi = 0
tre = 15

#while pipi < 14:
 #   print(f"Num: {pipi}")
 #   if pipi == tre:
 #       print("Look")
 #       break
  #  pipi += 2

# оператор цикла for

# 1.читает значение элемента итерируеого обьекта по порядку
# 2.присваивает это значение в свою переменную
# 3.выполняет блок кода своего тела

#for item in [1,2,3,4,5,6,7,8]:
 #   print(item)

mom = "Hi!"

#for pop in mom:
 #   print(pop*4)

list_1 = [10, 20, 30, 40, 50]
list_2 = []

#for r in list_1:
#    # r += 2
 #   res = r ** 2
 #   list_2.append(res) 

for r in list_1[::-1]:
    res = r ** 2
    list_2.append(res)

print(r)

