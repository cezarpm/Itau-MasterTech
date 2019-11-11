print('Entre com 4 notas')

numero1 = float(input('Nota 01: '))
numero2 = float(input('Nota 02: '))
numero3 = float(input('Nota 03: '))
numero4 = float(input('Nota 04: '))

media = (numero1 + numero2 + numero3 + numero4) / 4

if media > 7:
    print('Aprovado')

elif media > 5.5:
    print('Recuperação')

else:
    print('Reprovado')

input('Digite uma tecla para encerrar ')