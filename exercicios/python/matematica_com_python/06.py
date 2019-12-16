print('Calculadora de Média')

lista_numeros = []
continuar = True

while continuar :

    n1 = int(input('Insira um número '))
    lista_numeros.append(n1)

    resposta = input('Deseja continuar? Y - N ')

    if resposta == 'N' :
        continuar = False

media = round(sum(lista_numeros) / len(lista_numeros))

print(f'A média da lista {lista_numeros} é {media}')

input('Digite uma tecla para fechar o programa')