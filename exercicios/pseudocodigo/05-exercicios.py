print('Sistema de Marcearia')

temCompras = False
compras = []

def perguntaProduto(produto, preco):
    print(f'Deseja comprar {produto}?')
    resposta = int(input("SIM = 1  NÂO = 2 "))

    if(resposta == 1):
        print('Qual quantidade?')
        quantidade = int(input())
        adicionarCompra(quantidade, produto, preco)

def  adicionarCompra(quantidade, produto, preco):
    compras.append([produto, quantidade, preco])
    global temCompras
    temCompras = True


perguntaProduto('Batata', 3)
perguntaProduto('Cenoura', 7)
perguntaProduto('Rabanete', 5)

if(temCompras):
    for compras in compras:
        print(f'Produto: {compras[0]}, Quantidade {compras[1]}, Preço Unitário {compras[2]}, Preço Total: R$ { compras[1] * compras[2]}')

print('Sistema de Marcearia Finalizado')
input('Digite uma tecla para encerrar ')

