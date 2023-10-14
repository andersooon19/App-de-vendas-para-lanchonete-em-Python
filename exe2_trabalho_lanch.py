print('Bem Vindo a Lanchonete do Anderson Alves Santana') # Informações para os clientes escolherem os seus pedidos.
print('------------------|Cardápio|-----------------')
print('')
print('| Código |        Descrição        |  Valor |')
print('|  100   |     Cachorro Quente     |  9,00  |')
print('|  101   |  Cachorro Quente Duplo  |  11,00 |')
print('|  102   |           X-Egg         |  12,00 |')
print('|  103   |         X-Salada        |  12,00 |')
print('|  104   |          X-Bacon        |  14,00 |')
print('|  105   |          X-Tudo         |  17,00 |')
print('|  200   |     Refrigerante Lata   |  5,00  |')
print('|  201   |        Chá Gelado       |  4,00  |')
print('---------------------------------------------')
acumu = 0 # Váriavel acumuladora.

while True: # Enquanto for verdade.
    codigo = (input('Entre com o código desejado: '))

    if codigo != '100' and codigo != '101' and codigo != '102' and codigo != '103' and codigo != '104' and codigo != '105' and codigo != '200' and codigo != '201': # Condição.
        print('Opção Inválida')
        continue # Se o usuário digitar algo inválido volta para o inicio o while.

    if codigo == '100':
        print('Você pediu um Cachorro-Quente no valor de 9,00')
        acumu += 9 # Pegue o valor que tinha no acumu e some com 9.

    elif codigo == '101':
        print('Você pediu um Cachorro-Quente Duplo no valor de 11,00')
        acumu += 11 # Pegue o valor que tinha no acumu e some com 11.

    elif codigo == '102':
        print('Você pediu um X-Egg no valor de 12,00')
        acumu += 12 # Pegue o valor que tinha no acumu e some com 12.

    elif codigo == '103':
        print('Você pediu um X-Salada no valor de 12,00')
        acumu += 12 # Pegue o valor que tinha no acumu e some com 12.

    elif codigo == '104':
        print('Você pediu um X-Bacon no valor de 14,00')
        acumu += 14 # Pegue o valor que tinha no acumu e some com 14.

    elif codigo == '105':
        print('Você pediu um X-Tudo no valor de 17,00')
        acumu += 17 # Pegue o valor que tinha no acumu e some com 17.

    elif codigo == '200':
        print('Você pediu um Refrigerante Lata no valor de 5,00')
        acumu += 5 # Pegue o valor que tinha no acumu e some com 5.

    elif codigo == '201':
        print('Você pediu um Chá Gelado no valor de 4,00')
        acumu += 4 # Pegue o valor que tinha no acumu e some com 4.

    print('Deseja pedir mais alguma coisa? ')
    print('1 - Sim')
    print('0 - Não')

    pedir_mais = input('>> ') # Escolha se pedir mais alguma coisa ou não.
    if pedir_mais == '1':
        continue # Se digitar 1 o nosso programa volta para o inicio do while.

    else:
        print('O total a ser pago: R${:.2f}'.format(acumu))
        break # Se não força o fim do laço.