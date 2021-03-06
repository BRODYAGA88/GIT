"""
2.	Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)
"""
from collections import defaultdict
from functools import reduce


def count():
    numbers = defaultdict(list)
    for i in range(2):
        number = input(f"Введите {i + 1}-е число в шетснадцатиричной системе: ")
        numbers[number] = list(number)
    summ = sum([int(''.join(i), 16) for i in numbers.values()])
    print(f'Сумма: {hex(summ)[2:].upper()}')

    proiz = reduce(lambda x, y: x * y, [int(''.join(i), 16) for i in numbers.values()])
    print(f'Произведение: {hex(proiz)[2:].upper()}')


count()
