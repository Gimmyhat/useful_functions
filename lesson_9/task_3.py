"""
Написать функцию host_range_ping_tab(), возможности которой основаны на функции из примера 2.
Но в данном случае результат должен быть итоговым по всем ip-адресам, представленным в табличном формате
(использовать модуль tabulate). Таблица должна состоять из двух колонок
"""

from tabulate import tabulate
from task_2 import host_range_ping


def host_range_ping_tab():
    res_dict = host_range_ping()
    print()
    print(tabulate([res_dict], headers='keys', tablefmt="pipe", stralign="center"))


if __name__ == "__main__":
    host_range_ping_tab()

'''
Результат:

Введите первоначальный адрес: www.ru
Сколько адресов проверить?: 5
31.177.80.70 - Узел недоступен
31.177.80.71 - Узел доступен
31.177.80.72 - Узел доступен
31.177.80.73 - Узел недоступен
31.177.80.74 - Узел недоступен

|  Доступные узлы  |  Недоступные узлы  |
|:----------------:|:------------------:|
|   31.177.80.71   |    31.177.80.70    |
|   31.177.80.72   |    31.177.80.73    |
|                  |    31.177.80.74    |
'''