#!/usr/bin/env python3
# arquivo: servidor-poderoso.py

from socket import *

HOSPEDEIRO = input('IP para escutar (pressione <ENTER> para todas as interfaces): ')
PORTA = int(input('Porta a escutar (acima de 1024): '))
socketServidor = socket(AF_INET, SOCK_STREAM)
socketServidor.bind((HOSPEDEIRO, PORTA))
socketServidor.listen(1)
print('Esperando por uma conexão...')
conexao, endereco = socketServidor.accept()

while True:
    print ('Conexao vinda de {end_ip} pela porta {num_porta}'.format(
        end_ip=endereco[0], num_porta=endereco[1]))

    dados = conexao.recv(1024)
    while dados:    
        dados = dados.decode('utf-8')
        print('Recebi', dados)
        # Convertendo dados para letra maiúscula
        dados = dados.upper()
        conexao.send(bytearray(dados, 'utf-8'))
        dados = conexao.recv(1024)
    # end-while
    
    conexao.close()
    conexao, endereco = socketServidor.accept()
# end-while
