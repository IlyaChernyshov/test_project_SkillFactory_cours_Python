
print('--- || СПИСКИ (list)|| ---')
s = [0, 'hello', (1, 'a')] # Наполнение списка

letters = ['a', 'b', 'c', 'd']
letters.append('e') # Добавление элемента в конец APPEND
print(letters)
print(len(letters)) # Длина списка LEN
letters.pop()  # Удаление элемента POP

L = [3.3, 4.4, 5.5, 6.6]
print(map(round, L)) # Функции к каждому элементу списка MAP
print(list(map(round, L)))

string = input("Введите числа через пробел:") # представляет в виде строки
list_of_strings = string.split() # список строковых представлений чисел
list_of_numbers = list(map(int, list_of_strings)) # список чисел
print(sum(list_of_numbers[::3])) # sum() вычисляет сумму элементов списка

print('--- ЗАДАНИЕ 2.5 ---')
a= list(map(float, input('Введите числа через пробел: ').split())) # Преобразование в одной строке
# деление пробелом - преобразование к числам - преобразование в список
a[0],a[-1]=a[-1],a[0] # Обмен местами с помощью присваивания
a.append(sum(a))
print(a)


#                  ----  ///  СЛОВАРИ (dict)||| ----

# словарь заполняется по принципу - ключ:объект (через двоеточие)
person = {'name' : 'Ivan Petrov'}
# в него можно также добавлять новые объекты по ключу
person['age'] = 25
person['email'] = 'ivan_petrov@example.com'
person['phone'] = '8(800)555-35-35'

print(person.keys()) # Получение списка ключей
print(person.values()) # Получение списка значений
person.pop('phone') # Удаление с ключем

d = {'day' : 22, 'month' : 6, 'year' : 2015}
print("||".join(d.keys())) # метод для объединения списка строк в одну
# строку с использованием указанного разделителя - join

print('--- ЗАДАНИЕ 2.5 ---')
title = input("Введите название книги:")
author = input("Введите фамилию автора:")
year = int(input("Введите год издания:"))
book = {'title': title,
        'author': author,
        'year': year}
print(book)


#                  ----  ///  МНОЖЕСТВА (set) ||| ----

a = {'a', 'b', 'c', 'd'} # используя синтаксис { }
L = [1,1,2,3,2]
b = set(L)   # С помощью приведения в множество (set)
# [1,2,3]
b_list = list(b) # Привели обратно в список
# [1,2,3]
c = list(set(L)) # в одну строку
print('--- ЗАДАНИЕ 2.5 ---')
# Вывести кол-во уникальных символов
text=input("Введите текст: ")
unique=list(set(text))
print('Уникальные: ', len(unique))

#      -- ОПЕРАЦИИ С МНОЖЕСТВАМИ --
# set.union()  объединение - множество, состоящее из элементов set и other.
# set.intersection(other) пересечение - множество, состоящее из элементов, которые встречаются и в set, и в other.
# set.difference(other) разновидность - множество элементов set, которые не встречаются в other.
# set.symmetric_difference(other) симетричная разность - множество элементов,
# встречающиеся в одном из множеств, но не в обоих одновременно.

print('--- ЗАДАНИЕ 2.5 ---')
a = input("Введите первую строку: ")
b = input("Введите вторую строку: ")
a_set, b_set = set(a), set(b) # используем множественное присваивание
a_and_b = a_set.symmetric_difference(b_set)
print(a_and_b)

#        ----  ИДЕНТИЧНОСТЬ -----
a = 5
print(id(a))
b = 3+2
print(id(b))
c=id(a)-id(b)
print(c) # 0  (ID одинаков)

shopping_center = ("Галерея", "Санкт-Петербург", "Лиговский пр., 30", ["H&M", "Zara"])
list_id_before = id(shopping_center[-1])

shopping_center[-1].append("Uniqlo")
list_id_after = id(shopping_center[-1])

print(list_id_after is list_id_before)
print(list_id_before == list_id_after)

print(not True)
# можно проверить, находится ли число 1 в промежутке (0,4)
cond1 = 0 < 1
cond2 = 1 < 4
print(cond1 and cond2)
# или, например, содержат ли две строки один и тот же символ
cond3 = 't' in "python"
cond4 = 't' in "django"
print(cond3 and cond4)