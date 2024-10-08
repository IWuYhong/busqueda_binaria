"""
Ejemplo Práctico Python (Búsqueda Binaria & Búsqueda Simple).
"""

import random
import time


def busqueda_simple(lista, objetivo):
    for i in range(len(lista)):
        if lista[i] == objetivo:
            return i
    return -1


def busqueda_binaria(lista, objetivo, limite_inferior=None, limite_superior=None):
    if limite_inferior is None:
        limite_inferior = 0 # Inicio de la lista
    if limite_superior is None:
        limite_superior = len(lista) - 1 # Final de la lista

    if limite_superior < limite_inferior:
        return -1

    punto_medio = (limite_inferior + limite_superior) // 2 # Aca estamos trayendo el número entero, no podemos manejar Float para establecer un punto medio

    if lista[punto_medio] == objetivo:
        return punto_medio
    elif objetivo < lista[punto_medio]:
        return busqueda_binaria(lista, objetivo, limite_inferior, punto_medio-1)
    else:
        return busqueda_binaria(lista, objetivo, punto_medio+1, limite_superior)


if __name__=='__main__':
    # Crear una lista ordenada con 10000 números aleatorios.
    cantidad = 10000
    conjunto_inicial = set()

    while len(conjunto_inicial) < cantidad:
        conjunto_inicial.add(random.randint(-3*cantidad, 3*cantidad))

    lista_ordenada = sorted(list(conjunto_inicial))

    # Medir el tiempo de búsqueda simple.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_simple(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda ingenua: {fin - inicio} segundos.")

    # Medir el tiempo de búsqueda binaria.
    inicio = time.time()
    for objetivo in lista_ordenada:
        busqueda_binaria(lista_ordenada, objetivo)
    fin = time.time()
    print(f"Tiempo de búsqueda binaria: {fin - inicio} segundos.")
