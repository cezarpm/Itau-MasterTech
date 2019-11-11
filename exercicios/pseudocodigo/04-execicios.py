print('Entre com o salário do colaborador')
salario = int(input())

print(f'Salário R$ {salario}')

descontoINSS = salario * 9 / 100
salario = salario - descontoINSS
print(f'Valor descontado do INSS R$ {descontoINSS}')

descontoVT = salario * 3 / 100
salario = salario - descontoVT
print(f'Valor descontado do Vale-Transporte R$ {descontoVT}')

descontoSaude = 347 * 15 / 100
salario = salario - descontoSaude
print(f'Valor descontado do Plano de Saúde R$ {descontoSaude}')

salario = round(salario)
print(f'Salário líquido R$ {salario}')


input('Digite uma tecla para encerrar ')