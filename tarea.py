#Ejercico 1
lista_num = [1,2,3,4,5,6,7,8,9,10]

par = filter(lambda x: x % 2 == 0, lista_num)

#print(list(par))

#Ejercicio 2
lista_num2 = [1,2,3,4,5,6,7,8,9,10]

resultado = map(lambda x: x * 3, lista_num2)

#print(list(resultado))

#Ejercico 3
def mayus(x):
    return x.upper()

palabras = ['casa', 'mata', 'tapa']

resultadoMayus = map(mayus, palabras)

#print(list(resultadoMayus))

#Ejercico 4

def desendente(x):
    return sorted(x, reverse=True)

lista_num3 = [10,9,8,4,3,2,1,5,6,7]

result_desent = desendente(lista_num3)

#print(list(result_desent))

#Ejercico 5

def redondear(x):
    return round(x)

diccionario = {
    "num1": 1.20,
    "num2": 4.55,
    "num3": 13.80,
    "num4": 27.94,
    "num5": 53.79,
    "num6": 99.99,
}

# Creamos un nuevo diccionario aplicando la función redondear a cada valor
resul_redondeado = {clave: redondear(valor) for clave, valor in diccionario.items()}

#print(resul_redondeado)

#Ejercico 6

palabras2 = ['raton', 'catarata', 'astralopitecus']

def contarPalabra(x):
    return len(x)

contando = list(map(contarPalabra, palabras2))

#print(contando)

#Ejercico 7

palabras3 = ['casa', 'mata', 'tapa', 'raton', 'catarata', 'astralopitecus']

def cuatroLetras (x):
    return len(x) >= 5

filtrar = list(filter(cuatroLetras, palabras3))

#print(filtrar)

#Ejercico 8

texto = ["1","2","3"]

def entero(x):
    return int(x)

convertir = list(map(entero, texto))

#print(convertir)

#Ejercicio 9

lista_num4 = [-10,9,-8,4,-3,2,-1,5,-6,7]

def positivos (x):
    return (x) >= 0

filtrar = list(filter(positivos, lista_num4))

#print(filtrar)

#Ejercicio 10

listaTupla = [("Juan", 25), ("Ana", 20), ("Luis", 30)]

def segundoValor(x):
    return x[1]

ordenar = sorted(listaTupla, key=segundoValor)

#print(ordenar)

#Ejercicio 11

celsius = [50, 60, 70, 80, 90, 90]

fahrenheit = list(map(lambda x: ((x * 9/5)+ 32), celsius))

#print(f"Los grados fahrenheit son {fahrenheit}")

#Ejercicio 12

lista_num5 = [4.3, 5.7, 8.2]

proceso = list(map(lambda x: round(x) , lista_num5))

#print(proceso)

#Ejercicio 13

lista_num6 = [5, 3, 5, 2, 3, 1]

resultado = sorted(set(lista_num6))

#print(resultado)