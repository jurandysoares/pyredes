#!/usr/bin/env python3.0

from socket import *

receptor = socket(AF_INET, SOCK_DGRAM)
receptor.bind(('',2020))
nome = {}

while True:
    dados, endereco = receptor.recvfrom(1024)
    ip = endereco[0]
    if ip not in nome:
        nome[ip] = dados.decode('utf-8')
    else:
        dados = dados.decode('utf-8')
        print ("{0}: {1}".format(nome[ip], dados))

receptor.close()
