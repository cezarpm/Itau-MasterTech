print('-=' * 13)
print('Bem vindo ao Groger Bank')
print('-=' * 13)

first_name = input('Para começarmos, digite seu primeiro nome ')
nickname = input('Agora digite seu sobrenome ')
idade = int(input('Agora digite seu idade '))
saldo = int(input('Agora digite seu saldo '))

print('-=' * 13)
print('''Suas opções são
[ 1 ] SAQUE
[ 2 ] DEPÓSITO
[ 3 ] EMPRÈSTIMO
[ 4 ] VISUALIZAR''')
print('-=' * 13)

opcao = input('Selecione uma opção ')


def saque():
    valor_saque = input('Digite o valor do saque')
    if valor_saque > 1000 or valor_saque < saldo:
        print('num pode')
    else:
        saldo = saldo - valor_saque
        print(f'Saque realizado, seu saldo atual é {saldo}')


def deposito():
    valor_deposito = input('Digite o valor do depósito')
    if valor_deposito > 5000:
        print('num pode')

    else:
        saldo = saldo + valor_saque
        print(f'Depósito realizado, seu saldo atual é {saldo}')


def emprestimo():
    if idade < 21:
        print('num pode')

    else:
        valor_emprestimo = input('Digite o valor do empréstimo')

        if saldo >= 1000 and valor_emprestimo >= 2000:
            print('Foi meu bom')
            saldo = saldo + valor_emprestimo
            print(f'Depósito realizado, seu saldo atual é {saldo}')

        else:
            print('num pode')


def visualizar():
    print(f'''
    NOME: {nome}
    SOBRENOME: {sobrenome}
    IDADE: {idade}
    SALDO {saldo}
    ''')


def sair():
    input('Digite uma tecla para encerar o programa')


if opcao == '1':
    saque()
elif opcao == '2':
    deposito()

elif opcao == '3':
    emprestimo()

elif opcao == '4':
    visualizar()

else:
    sair()
