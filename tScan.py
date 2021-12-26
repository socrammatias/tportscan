import socket

site = input('Write the Url or Ip Address: ')
qtd = (int(input('Quantity of ports you want test: ')))
portas = []
ip = (socket.gethostbyname(site))
dominio = (socket.gethostbyaddr(ip))
dominio = dominio.split()[0] ## arrumar isso
for x in range(qtd):
    portas.append(int(input('Port: ')))
for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    codigo = cliente.connect_ex((site, porta))
    if codigo == 0:
        print('\033[92m','[*]','\033[0m',ip, dominio,porta, 'OPEN') 
    else:
        print('\033[91m','[*]','\033[0m',ip, dominio,porta, 'CLOSED') 

input()