#!/usr/bin/env python3
#-*- coding:utf-8 -*-

#
# servidor_filamento.py
# This file is part of PYREDES
#
# Copyright (C) 2014 - Jurandy Soares
#
# PYREDES is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# PYREDES is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PYREDES; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, 
# Boston, MA  02110-1301  USA
#

import socket
import threading
import socketserver

class Servidor(socketserver.BaseRequestHandler):
        
    # método principal, que vai manipular a conexão
    def handle(self):
        filamento_atual = threading.current_thread()
        print(filamento_atual.getName())
        
        bytesrecebidos = self.request.recv(1024)
        dados = bytesrecebidos.decode('utf-8')        
        while dados.strip():          
            print('Dados processados por {}: {}'.format(filamento_atual.getName(), dados))
            # comd,*varg = dados.split()
            resposta = dados.upper()
            bytesresposta = bytearray(resposta, 'utf-8')
            self.request.send(bytesresposta)
            bytesrecebidos = self.request.recv(1024)
            dados = bytesrecebidos.decode('utf-8')
            print(len(dados))            


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass
    
def main():
    
    # O servidor escutará na porta 4403, em homenagem à turma
    HOST, PORT = "", 4455 

    servidor = ThreadedTCPServer((HOST, PORT), Servidor)

    thread_servidor = threading.Thread(target=servidor.serve_forever)
    thread_servidor.setDaemon(True)
    thread_servidor.start()
    input('Pressione <ENTER> para encerrar o servidor\n')
    servidor.shutdown()    

if __name__ == "__main__":
    main()
    
