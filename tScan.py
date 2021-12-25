import socket

site = input('Digite o site ou o Ip alvo: ')
qtd = (int(input('Quantidade de portas: ')))
portas = []

for x in range(qtd):
    portas.append(int(input('Porta: ')))
for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    codigo = cliente.connect_ex((site, porta))
    if codigo == 0:
        print('\033[92m','[*]','\033[0m',porta, 'OPEN') ## arrumar isso
    else:
        print('\033[91m','[*]','\033[0m',porta, 'CLOSED') ## arrumar isso

input()