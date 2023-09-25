
#1. Crie uma função que receba um número variado de argumentos numéricos e retorne a soma desses números
def soma(n, *args):
    valor = n
    for valr in  args:
        valor += valr   
    return valor
valor = soma(2,5)
print(valor)
print('1º')
print('-'*10)
#2. Modifique a função do exercício 1 para, caso a chave 'multi' exista no kwargs, retorne a soma vezes esse valor

def valor(n, **kwargs):
    if 'multi' in kwargs:
        resultado = n * kwargs['multi']
    else:
        resultado = n * 2
    return resultado 
   
print(valor(10, multi=20))
print('2º')
print('-'*10)

#3. Crie uma função recursiva que calcule a sequencia de Fibonacci para um número N
# A sequência de Fibinacci é realizada de modo que cada número é a soma dos dois anteriores
# 1 1 2 3 5 8

def fibo(n):
    if n == 1:
        return 0
    
    return n + fibo(n)

xx = fibo(3)
print(xx)
print('3º')
print('-'*10)

#4. Crie uma função que retorne uma Closure para potência N de um número
def gera_potencia(valor):
    def potencia(n):
        return n**valor
    return potencia
cubo = gera_potencia(3)
quintutplo = gera_potencia(5)
testando = quintutplo(7)
testando = cubo(3)
print(testando)
print('4º')
print('-'*10)

#5. Use list comprehension para criar uma nova lista a partir da lista abaixo contendo apenas os números ímpares
#[0, 3, -4, -1, 2, 10, 5, 7]
lista = [0, 3, -4, -1, 2, 10, 5, 7]
print(lista)
print('-'*10)
numeros_impares = [x for x  in lista if x % 2 == 1]
print(f' Valores impares da lista são: {numeros_impares}')
print('5º')
print('-'*10)


#6. Combine list comprehension com uma função lambda para obter o quadrado do dobro dos elementos da lista do exercício anterior
 
t = lambda a :a*2

print(t(numeros_impares))

print('6º')
print('-'*10)

#7. Modifique o item 4 para utilizar uma função lambda