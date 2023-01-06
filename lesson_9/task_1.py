# 1. Написать функцию host_ping(), в которой с помощью утилиты ping будет проверяться
# доступность сетевых узлов. Аргументом функции является список, в котором каждый сетевой
# узел должен быть представлен именем хоста или ip-адресом. В функции необходимо
# перебирать ip-адреса и проверять их доступность с выводом соответствующего сообщения
# («Узел доступен», «Узел недоступен»). При этом ip-адрес сетевого узла должен создаваться
# с помощью функции ip_address().


from ipaddress import ip_address
from subprocess import Popen, PIPE


def host_ping(list_ip_addresses, timeout=500, requests=1):
    nodes = ['Доступные узлы', 'Недоступные узлы']
    results = dict(zip(nodes, ['', '']))
    for address in list_ip_addresses:
        try:
            address = ip_address(address)
        except ValueError:
            pass
        proc = Popen(f"ping {address} -w {timeout} -n {requests}", stdout=PIPE)
        proc.wait()

        results[nodes[proc.returncode]] += f"{str(address)}\n"
        print(f'{address} - Узел {("", "не")[proc.returncode]}доступен')

    return results


if __name__ == '__main__':
    ip_addresses = ['yandex.ru', '2.2.2.2', '192.168.1.1', '192.168.0.101']
    print(host_ping(ip_addresses))

'''
РЕЗУЛЬТАТ:

yandex.ru - Узел доступен
2.2.2.2 - Узел недоступен
192.168.1.1 - Узел доступен
192.168.0.101 - Узел недоступен
{'Доступные узлы': 'yandex.ru\n192.168.1.1\n', 'Недоступные узлы': '2.2.2.2\n192.168.0.101\n'}
'''
