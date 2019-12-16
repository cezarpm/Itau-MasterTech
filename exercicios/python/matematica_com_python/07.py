lista_numeros = []

quantidade = int(input('Quantos numeros voce deseja inserir? '))

while len(lista_numeros) + 1 <= quantidade:
    numero = int(input('Digite um numero '))
    lista_numeros.append(numero)
    

maior_numero = max(lista_numeros)

print(f'O maior número da lista é {maior_numero}')

input('Digite uma tecla para fechar o programa')