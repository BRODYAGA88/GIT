from hashlib import pbkdf2_hmac

"""
Задание 2.
Ваша программа должна запрашивать пароль
Для этого пароля вам нужно получить хеш, используя функцию sha256
Для генерации хеша обязательно нужно использовать криптографическую соль
Обязательно выведите созданный хеш

Далее программа должна запросить пароль повторно
Вам нужно проверить, совпадает ли пароль с исходным
Для проверки необходимо сравнить хеши паролей

ПРИМЕР:
Введите пароль: 123
В базе данных хранится строка: 555a3581d37993843efd4eba1921f1dcaeeafeb855965535d77c55782349444b
Введите пароль еще раз для проверки: 123
Вы ввели правильный пароль
"""


def check():
    login = input("Введите логин: ")
    password = input("Ведите пароль: ")
    hash1 = pbkdf2_hmac(hash_name="sha256", password=password.encode(), salt=login.encode(), iterations=1)
    password = input("Ведите пароль: ")
    hash2 = pbkdf2_hmac(hash_name="sha256", password=password.encode(), salt=login.encode(), iterations=1)
    if hash1 == hash2:
        return "Доступ разрешен!"
    else:
        return "Доступ запрешен!"


print(check())
