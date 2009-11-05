#!/usr/bin/env python3

from socket import *
from os import fork

HOSPEDEIRO = input('IP para escutar (pressione <ENTER> para todas as interfaces): ')
HOSPEDEIRO = ''
PORTA = int(input('Porta a escutar (acima de 1024): '))
socketServidor = socket(AF_INET, SOCK_STREAM)
socketServidor.bind((HOSPEDEIRO, PORTA))
socketServidor.listen(30)
print('Esperando por uma conexão...')

while True:
     conexao, endereco = socketServidor.accept()
     
     num_processo = fork()

     if (num_processo == 0):
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
         break
     # end-if
# end-while
