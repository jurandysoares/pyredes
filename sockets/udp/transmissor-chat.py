#!/usr/bin/env python3.0
#-*- coding:utf-8 -*-

from socket import *

transmissor = socket(AF_INET, SOCK_DGRAM)
transmissor.setsockopt(SOL_SOCKET,SO_BROADCAST, 1)
receptor = input('Nome ou IP do receptor: ')
porta_destino = int(input('Porta associada ao receptor: '))
apelido = input("Digite seu apelido ou nick: ")
transmissor.sendto(bytearray(apelido, 'utf-8'), (receptor, porta_destino))

mensagem = input('Mensagem: ')
while mensagem:
    transmissor.sendto(bytearray(mensagem, 'utf-8'), (receptor, porta_destino))
    mensagem = input('Mensagem: ')

transmissor.close()
