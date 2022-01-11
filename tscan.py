#!/usr/bin/env python3
import socket

site = input('Write the url or ip address: ')
qtd = (int(input('Quantity of ports you want test: ')))
portas = []
ip = (socket.gethostbyname(site))
domain = (socket.gethostbyaddr(ip))
domain = domain[0] 
for x in range(qtd):
    portas.append(int(input('Port: ')))
for porta in portas:
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.settimeout(0.5)
    codigo = cliente.connect_ex((site, porta))
    if codigo == 0:
        print('[*]',ip, ',',domain,',',porta, 'OPEN') 
    else:
        print('[*]',ip, ',',domain,',',porta, 'CLOSED') 

input('Press anything to close.')