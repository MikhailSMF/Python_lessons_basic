# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def fibonacci(n, m):
    a = 1
    b = 1
    lst = [a, b]
    while len(lst) < m:
        lst.append(a + b)
        a, b = b, a + b
    #print(lst)
    return lst[n-1:m]

print(fibonacci(3, 5))

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    for i in range(len(origin_list) - 1):
        for j in range(len(origin_list) - i - 1):
            if origin_list[j] > origin_list[j + 1]:
                buff = origin_list[j]
                origin_list[j] = origin_list[j + 1]
                origin_list[j + 1] = buff
    return print(origin_list)


sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.

