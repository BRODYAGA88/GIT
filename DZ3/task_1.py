import time
"""
Задание 1.

Докажите, что словари обрабатываются быстрее, чем списки.

Реализуйте две функции, в первой нужно заполнить элементами список, во второй-словарь
Сделайте замеры времени выполнения каждой из функций

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор и пусть она считает время
И примените ее к двум своим функциям.
"""
number_list = [i for i in range(100000)]
my_dict = {}
my_list = []
time1 = time.time()
for i in range(len(number_list)):
    my_dict[i] = number_list[i]
num1 = my_dict[63859]
print(time.time() - time1)

time2 = time.time()
for i in number_list:
    my_list.append(i)
num2 = my_list[63859]
print(time.time() - time2)


