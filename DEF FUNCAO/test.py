
lista = [0, 3, -4, -1, 2, 10, 5, 7]
print(lista)
print('-'*10)
numeros_impares = [x for x  in lista if x % 2 == 1]
print(f' Valores impares da lista são: {numeros_impares}')