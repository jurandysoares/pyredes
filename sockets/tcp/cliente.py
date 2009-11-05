#!/usr/bin/env python3

from socket import *

HOSPEDEIRO = input('Servidor (nome ou IP): ')
PORTA = int(input('Porta: '))

clienteSocket = socket(AF_INET, SOCK_STREAM)
clienteSocket.connect((HOSPEDEIRO, PORTA))

mensagem = input('Mensagem: ')
while mensagem != '':
    dados_a_enviar = bytearray(mensagem, 'utf-8')
    print('Enviando dados...')
    clienteSocket.send(dados_a_enviar)
    print('Dados enviados. Aguardando retorno...')
    dados_recebido = clienteSocket.recv(1024)
    print('Retorno recebido')
    dados_recebido = dados_recebido.decode('utf-8')
  
    print ('Recebido:', dados_recebido)
    mensagem = input('Mensagem: ')
    
clienteSocket.close()    
