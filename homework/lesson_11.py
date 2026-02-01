
"""
Тема: tuple
"""

# ЗАДАНИЕ 1: Работа с кортежами

# Дано:
# coordinates = (10, 20, 30, 20, 10, 20, 40)

# 1. Выведите первый элемент кортежа
# 2. Выведите последний элемент кортежа
# 3. Выведите срез с 2-го по 4-й элемент (включительно)
# 4. Проверьте, есть ли число 30 в кортеже (используйте оператор in)
# 5. Найдите индекс первого вхождения числа 20
# 6. Подсчитайте, сколько раз встречается число 20
# 7. Подсчитайте, сколько раз встречается число 50 (его нет в кортеже)
# 8. Выведите длину кортежа

coordinates = (10, 20, 30, 20, 10, 20, 40)
print(coordinates[0])
print(coordinates[-1])
print(coordinates[1:4])
print(30 in coordinates)
print(coordinates.index(20))
print(coordinates.count(20))

if 50 in coordinates:
    print(coordinates.count(50))
else:
    print("Число 50 не найдено в кортеже")
print(len(coordinates))

# ЗАДАНИЕ 2: Операции с кортежами

# Дано:
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
numbers = [10, 20, 30, 40, 50]

# 1. Объедините tuple1 и tuple2 в один кортеж
# 2. Создайте кортеж, где элементы tuple1 повторяются 3 раза
# 3. Распакуйте tuple1 в три переменные a, b, c
# 4. Распакуйте numbers (преобразовав в кортеж) так, чтобы:
#    - первый элемент был в переменной first
#    - последний элемент был в переменной last
#    - все средние элементы были в списке middle
# 5. Преобразуйте список numbers в кортеж
# 6. Создайте кортеж из четных чисел от 0 до 10 (используйте генератор)
# 7. Создайте кортеж квадратов чисел от 1 до 5 (используйте генератор)
# 8. Создайте кортеж из одного элемента со значением 42

tuple3 = tuple1 + tuple2
tuple4 = tuple1 * 3
a, b, c = tuple1
print(a)
print(b)
print(c)
numbers_kor = tuple(numbers)
print(numbers_kor)
first, *middle, last = numbers_kor
print(first)
print(middle)
print(last)
numbers2 = list(numbers)
numbers3 = tuple(x for x in range(11) if x % 2 == 0)
numbers4 = tuple(x ** 2 for x in range(1, 6))
numbers5 = (42,)
