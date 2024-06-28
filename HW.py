# Переменные
name = "Jordan" #переменная str
age = 22 #перемнная int
height = 1.82 #переменная float
print(name, age, height) #Jordan, 22, 1.82

#Типы данных
print(type(name)) #str
print(type(age)) #int
print(type(height)) #float
print(age == 22) #boolean(true)

#Математические операторы
print(3 + 2) #Сложение(5)
print(3 - 2) #Вычитание(1)
print(3 * 2) #Умножение(6)
print(3 / 2) #Деление(1.5)
print(3**2) #Возведение в степень(9)
print(3 // 2) #Деление без остатка(1)
print(3 % 2) #Остаток от деления(1)

#Условные операторы + input + методы списка + цикл while + форматирование строк
# a = []
# while True:
#     b = input("Что хотите сделать? ")
#     if b.lower() == "добавить":
#         c = input("Введите имя, которое хотите добавить: ")
#         if c in a:
#             print("Это имя уже есть в списке!")
#         else:
#             a.append(c)
#             print(f'Имя {c} успешно добавлен в список!')
#     elif b.lower() == "удалить":
#         d = input("Введите имя, которое хотите удалить: ")
#         if d in a:
#             a.remove(d)
#             print(f'Имя успешно удалено!')
#         else:
#             print(f'Это имя не существует в списке!')
#     elif b.lower() == "отмена":
#         break


#list slicing + индексы
q = ["Jordan", 25, 4.5, "Alex", 47, "Pavel"]
print(q[0:4:2]) #от "Jordan" до 47(не включительно) с шагом 2
# 'Jordan', 4.5

#Кортежи
#тоже самое что и списки, но не поддаются к изменениям
#создаются с помощью круглых скобок
# t = ("Jordan")
# print(t.append("Alex")) #ошибка

#list comprehension + цикл for + range
d = [h for h in range(0, 101)] #лист, который включает в себя цифры и числа от 0 до 101(не включительно)
o = [m for m in d if m % 2 == 0] #сортировка четных цифр и чисел
print(o)

#Словарь
  #Методы создания
f = {}
f["genre"] = "pop"
print(f)
i = dict(genre = "classic")
print(i)
  #Заменя значения
i["genre"] = "folk"
print(i)

#Сеты
#сет оставляет только уникаальные элементы
u = {1, 2, 3, 3, 4} #1, 2, 3, 4
print(u)

#Функции
def x():
    print(2 + 8) #Код функции
x() #Вызов функции
  #анонимная функция
p = lambda y: y+5
print(p(10)) # 15

# *args *kwargs
# с помощью *args можно задать любое кол-во аргументов
def d(*args):
    return args
print(d(1, 2, 3, "abc"))
# с помощью *kwargs можно задать любое кол-во аргументов (ключ:значение)
def g(**kwargs):
    return kwargs
print(g(Jordan = 22, Alex = 23))

#Классы + наследование классов
class Car:
    def __init__(self, a): #self способ обращения к атрибутам
        pass

class ABC(Car): #наследование методa класса "Car"
    def __init__(self, a):
        super.__init__(a)



