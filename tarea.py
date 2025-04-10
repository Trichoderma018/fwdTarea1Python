#Ejercico 1
lista_num = [1,2,3,4,5,6,7,8,9,10]

def es_par(lista_num):
    return lista_num % 2 == 0

pares = filter(es_par, lista_num)

#print(list(pares))

#Ejercicio 2
def por_3(x):
    return x * 3

lista_num2 = [1,2,3,4,5,6,7,8,9,10]

resultado = map(por_3, lista_num2)

#print(list(resultado))

#Ejercico 3
def mayus(x):
    return x.upper

lista_num2 = [1,2,3,4,5,6,7,8,9,10]

resultado = map(por_3, lista_num2)

palabras = ['casa', 'mata', 'tapa']

