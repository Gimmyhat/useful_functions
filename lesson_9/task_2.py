"""
2. Написать функцию host_range_ping() для перебора ip-адресов из заданного диапазона.
Меняться должен только последний октет каждого адреса.
По результатам проверки должно выводиться соответствующее сообщение.
"""

from ipaddress import ip_address
import socket

from task_1 import host_ping


def host_range_ping():
    while True:
        start_ip = input('Введите первоначальный адрес: ')
        try:
            # можно вводить в формате IPv4, либо текстовый адрес
            start_ip = socket.gethostbyname(start_ip)
            las_oct = int(start_ip.split('.')[3])
            break
        except Exception as e:
            print(e)
    while True:
        end_ip = input('Сколько адресов проверить?: ')
        if not end_ip.isnumeric():
            print('Необходимо ввести число: ')
        else:
            if (las_oct + int(end_ip)) > 254:
                print(f"Можем менять только последний октет, т.е. "
                      f"максимальное число хостов для проверки: {254 - las_oct}")
            else:
                break

    host_list = []
    [host_list.append(str(ip_address(start_ip) + x)) for x in range(int(end_ip))]
    return host_ping(host_list)


if __name__ == "__main__":
    host_range_ping()

'''
РЕЗУЛЬТАТ:

Введите первоначальный адрес: www.ru
Сколько адресов проверить?: 5
31.177.80.70 - Узел доступен
31.177.80.71 - Узел доступен
31.177.80.72 - Узел доступен
31.177.80.73 - Узел недоступен
31.177.80.74 - Узел недоступен

Введите первоначальный адрес: 192.168.1.1
Сколько адресов проверить?: 5
192.168.1.1 - Узел доступен
192.168.1.2 - Узел недоступен
192.168.1.3 - Узел недоступен
192.168.1.4 - Узел недоступен
192.168.1.5 - Узел недоступен
'''
