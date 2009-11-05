#!/usr/bin/env python3.0

from socket import *

receptor = socket(AF_INET, SOCK_DGRAM)
receptor.bind(('',2000))

while True :
    dados, endereco = receptor.recvfrom(1024)
    print ()
    if not dados :
        break
    else:
        dados = dados.decode('utf-8')
        print (dados)

receptor.close()
