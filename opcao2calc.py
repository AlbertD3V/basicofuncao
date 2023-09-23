# opcao 2 de calculadora ---- completem!!!

def soma():
    x = float(input('Primeiro numero: '))
    y = float(input('Segundo numero: '))
    print('Soma igual a:', x + y)
    
def sub():
    x = float(input('Primeiro numero: '))
    y = float(input('Segundo numero: '))
    print('Soma igual a:', x - y)

opcao = 1

while opcao:
    print('0. sair')
    print('1 para somar')
    print('2 para subtrair')
    print('3 para multiplicar')
    opcao = int(input('Informe a operação: '))
    if opcao == 1: