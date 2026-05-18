# Ejercicio 4 - Filter
# Datos base para verificar los puntos de filter.

palabras = ["casa", "perro", "universidad", "oso", "radar", "ana", "python", "reconocer"]
valores = [1, None, 2, None, 3, 0, None]
numeros = [5, 10, 15, 23, 35, 40, 105]
productos_dict = [
    {"nombre": "Teclado", "precio": 80},
    {"nombre": "Mouse", "precio": 40},
    {"nombre": "Monitor", "precio": 300},
    {"nombre": "Webcam", "precio": 150}
]

print("Palabras:", palabras)
print("Valores:", valores)
print("Numeros:", numeros)
print("Productos:", productos_dict)


# Enunciado a: Dada una lista de palabras, filtrar solo aquellas con mas de 4 letras.
palabras_mas_de_4 = list(filter(lambda palabra: len(palabra) > 4, palabras))
print("Filter a. Palabras con mas de 4 letras:", palabras_mas_de_4)


# Enunciado b: Dada una lista, filtrar los elementos que son nulos (None).
sin_nulos = list(filter(lambda valor: valor is not None, valores))
print("Filter b. Lista sin nulos:", sin_nulos)


# Enunciado c: Dada una lista de palabras, filtrar aquellas que empiezan por una vocal.
vocales = "aeiouAEIOU"
empiezan_por_vocal = list(filter(lambda palabra: len(palabra) > 0 and palabra[0] in vocales, palabras))
print("Filter c. Palabras que empiezan por vocal:", empiezan_por_vocal)


# Enunciado d: Dada una lista de palabras, filtrar aquellas que son palindromos.
palindromos = list(filter(lambda palabra: palabra.lower() == palabra.lower()[::-1], palabras))
print("Filter d. Palindromos:", palindromos)


# Enunciado e: Dada una lista de numeros, filtrar los que terminan en 5.
terminan_en_5 = list(filter(lambda numero: abs(numero) % 10 == 5, numeros))
print("Filter e. Numeros que terminan en 5:", terminan_en_5)


# Enunciado f: Dada una lista de diccionarios, filtrar los productos con precio mayor a 100.
productos_mayores_a_100 = list(filter(lambda producto: producto["precio"] > 100, productos_dict))
print("Filter f. Productos con precio mayor a 100:", productos_mayores_a_100)

# Ejercicio 4 - Reduce
# Datos base para verificar los puntos de reduce.

from functools import reduce

numeros_reduce = [2, 3, 4, 5]
palabras_reduce = ["Hola", " ", "mundo", " ", "Python"]
numeros_para_mayor = [12, 9, 33, 21, 7]

print("Numeros para multiplicar:", numeros_reduce)
print("Palabras para concatenar:", palabras_reduce)
print("Numeros para hallar mayor:", numeros_para_mayor)


# Enunciado a: Dada una lista de numeros, calcula la multiplicacion de estos.
multiplicacion_total = reduce(lambda acumulado, numero: acumulado * numero, numeros_reduce, 1)
print("Reduce a. Multiplicacion total:", multiplicacion_total)


# Enunciado b: Dada una lista de palabras, concatenarlas en una sola.
texto_concatenado = reduce(lambda acumulado, palabra: acumulado + palabra, palabras_reduce, "")
print("Reduce b. Texto concatenado:", texto_concatenado)


# Enunciado c: Dada una lista, hallar el mayor de todos.
# Definir una funcion auxiliar que dado dos numeros retorne el mayor.
def mayor_de_dos(numero_1, numero_2):
    if numero_1 > numero_2:
        return numero_1
    return numero_2

mayor_total = reduce(mayor_de_dos, numeros_para_mayor)
print("Reduce c. Mayor de todos:", mayor_total)

# Ejercicio 4 - Sorted
# Datos base para verificar los puntos de sorted.

palabras_sorted = ["pera", "manzana", "uva", "banano"]
tuplas = [(3, "c"), (1, "a"), (2, "b")]
productos_tuplas = [
    ("Camisa", 30),
    ("Pantalon", 55),
    ("Medias", 10),
    ("Chaqueta", 80)
]
numeros_sorted = [7, 2, 9, 4, 1, 6, 3, 8]
palabra_para_conteo = "programacion"
empleados = [
    ("Maria", "Ventas", 30),
    ("Luis", "Tecnologia", 25),
    ("Ana", "Ventas", 25),
    ("Pedro", "Tecnologia", 28)
]

print("Palabras:", palabras_sorted)
print("Tuplas:", tuplas)
print("Productos:", productos_tuplas)
print("Numeros:", numeros_sorted)
print("Palabra para conteo:", palabra_para_conteo)
print("Empleados:", empleados)


# Enunciado a: Ordenar una lista de palabras alfabeticamente.
palabras_ordenadas = sorted(palabras_sorted)
print("Sorted a. Palabras alfabeticamente:", palabras_ordenadas)


# Enunciado b: Ordenar una lista de tuplas por el primer elemento.
tuplas_ordenadas = sorted(tuplas, key=lambda tupla: tupla[0])
print("Sorted b. Tuplas por primer elemento:", tuplas_ordenadas)


# Enunciado c: Dada una lista de productos, ordenar por precio de mayor a menor y luego por nombre.
productos_ordenados = sorted(productos_tuplas, key=lambda producto: (-producto[1], producto[0]))
print("Sorted c. Productos por precio mayor a menor y nombre:", productos_ordenados)


# Enunciado d: Dada una lista de palabras, ordenarlas segun su longitud.
palabras_por_longitud = sorted(palabras_sorted, key=lambda palabra: len(palabra))
print("Sorted d. Palabras por longitud:", palabras_por_longitud)


# Enunciado e: Dada una lista de numeros, ordenarlos para que aparezcan primero los pares y luego los impares.
pares_luego_impares = sorted(numeros_sorted, key=lambda numero: (numero % 2, numero))
print("Sorted e. Pares primero e impares despues:", pares_luego_impares)


# Enunciado f: Convertir una palabra a un diccionario que cuente la aparicion de cada letra.
# Luego ordenar dicho diccionario segun la frecuencia de aparicion.
conteo_letras = {}
for letra in palabra_para_conteo:
    conteo_letras[letra] = conteo_letras.get(letra, 0) + 1

conteo_ordenado = dict(sorted(conteo_letras.items(), key=lambda item: item[1], reverse=True))
print("Sorted f. Conteo de letras ordenado por frecuencia:", conteo_ordenado)


# Enunciado g: Dada una lista de tuplas, ordenar primero por el departamento del empleado y luego por la edad.
empleados_ordenados = sorted(empleados, key=lambda empleado: (empleado[1], empleado[2]))
print("Sorted g. Empleados por departamento y edad:", empleados_ordenados)
