print('Calculadora IMC')

peso = float(input('Coloque seu peso: '))
altura = float(input('Coloque sua altura:  '))

imc = round(peso / (altura * altura))

if imc < 18:
    print(f'Você está abaixo do peso ideal, seu IMC é: {imc}')

elif imc <= 24:
    print(f'Parabéns você está em seu peso normal, seu IMC é: {imc}')

elif imc <= 30:
    print(f'Você está acima de seu peso (sobrepeso), seu IMC é: {imc}')

elif imc > 30:
    print(f'Você está Obeso, seu IMC é: {imc}')


input('Digite uma tecla para encerrar ')