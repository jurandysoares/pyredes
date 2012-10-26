# -*- coding: utf-8 -*-

print('''  Tutor de TCP/IP:
    * cálculo da quantidade de endereços IP na sub-rede
    * cálculo do endereço de rede
    * cálculo do endereço de broadcast
    * cálculo do menor número IP atribuível a interface
    * cálculo do maior número IP atribuível a interface
    ''')

print('Entre com os dados do endereço IP versão 4')
end_ip  = input('Endereço: ')
bits_netID = int(input('Quantidades de bits para máscara de sub-rede: '))
print('Calculando a quantidade de bits utilizada para identificar hosts...')
bits_hostID = 32 - bits_netID
print(bits_hostID)
print('Calculando a quantidade de endereços da sub-rede...')
qtde_ips = 2**bits_hostID
print(qtde_ips)

if bits_netID >= 24:
    print('Obtendo o último valor decimal do último octeto...')    
    final_ip = int(end_ip.split('.')[-1])
    print(final_ip)
    final_rede = (final_ip//qtde_ips) * qtde_ips
    final_broadcast = (final_rede+qtde_ips) - 1
    final_menor_ip = final_rede+1
    final_maior_ip = final_broadcast-1
    
    print('Formatando a saída...')
    prefixo_ip = end_ip[:end_ip.rindex('.')+1]
    rede = prefixo_ip + str(final_rede)
    broadcast = prefixo_ip + str(final_broadcast)
    menor_ip = prefixo_ip + str(final_menor_ip)
    maior_ip = prefixo_ip + str(final_maior_ip)
    
    print('Exibindo os resultados obtidos...')
    print('Endereço de Rede:', rede)
    print('Endereço de Broadcast:', broadcast)
    print('Menor endereço IP atribuível:', menor_ip)
    print('Maior endereço IP atribuível:', maior_ip)
    print('Quantidade de endereços IPs atribuíveis:', qtde_ips-2)
else:
    print('Sinto muito, você terá que fazer os cálculos binários :(')
    

    
    
