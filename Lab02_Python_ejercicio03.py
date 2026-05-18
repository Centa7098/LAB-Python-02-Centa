# Ejercicio 3 - Map
# Datos base para verificar todos los puntos.

import math

temperaturas_celsius = [0, 10, 20, 30]
lista_1 = [1, 2, 3, 4]
lista_2 = [10, 20, 30, 40]
radios = [1, 2, 3, 4]
precios = {"pan": 1000, "leche": 2500, "cafe": 5000}
matriz = [[1, 2, 3], [4, 5, 6]]

print("Temperaturas Celsius:", temperaturas_celsius)
print("Lista 1:", lista_1)
print("Lista 2:", lista_2)
print("Radios:", radios)
print("Precios:", precios)
print("Matriz:", matriz)


# Enunciado a: Dada una lista de temperaturas en Celsius, convertirlas a Fahrenheit.
temperaturas_fahrenheit = list(map(lambda celsius: (celsius * 9 / 5) + 32, temperaturas_celsius))
print("a. Temperaturas Fahrenheit:", temperaturas_fahrenheit)


# Enunciado b: Dadas dos listas con la misma cantidad de elementos, generar una nueva sumando cada elemento.
sumas_por_posicion = list(map(lambda par: par[0] + par[1], zip(lista_1, lista_2)))
print("b. Suma por posicion:", sumas_por_posicion)


# Enunciado c: Dada una lista de radios de circulos, generar la lista de sus areas.
areas_circulos = list(map(lambda radio: math.pi * radio ** 2, radios))
print("c. Areas de circulos:", areas_circulos)


# Enunciado d: Dado un diccionario, generar una lista de tuplas (nombre, valor + 10 por ciento).
precios_mas_10 = list(map(lambda item: (item[0], item[1] * 1.10), precios.items()))
print("d. Precios con aumento del 10 por ciento:", precios_mas_10)


# Enunciado e: Dada una matriz, multiplicar todos los elementos por 10.
matriz_por_10 = list(map(lambda fila: list(map(lambda numero: numero * 10, fila)), matriz))
print("e. Matriz por 10:", matriz_por_10)
