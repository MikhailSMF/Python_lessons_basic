# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.

def my_round(number, ndigits):
    """
    Округление числа без функций
    :param number: int/float
    :param ndigits: int
    :return: int/float
    """
    new_number = f'{str(number)[:int(number)+ndigits+1]}'
    if float(new_number[-1]) >= 6:
        return float(new_number[:-1]) + float(str(0.)+str('0')*(ndigits-2) + str('1'))
    else:
        return new_number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print(my_round(2.1234567, 3))
print(my_round(2.1234567, 4))
print(my_round(2.1234567, 6))

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить

def lucky_ticket(ticket_number):
    if sum(map(int,list(str(ticket_number)[:-3]))) == sum(map(int,list(str(ticket_number)[-3:]))):
        return 'Luck'
    else:
        return 'No luck'


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))