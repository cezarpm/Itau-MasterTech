print('Contador de Letra')

frase = input('Insira uma frase ')

letra = input('Insira uma letra ')

frase_separada = list(frase)

quantidade = frase_separada.count(letra)

print(f'O quantidade que a letra {letra} aparece é {quantidade}')

input('Digite uma tecla para fechar o programa')