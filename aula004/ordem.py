lista = [64, 34, 25, 12, 22, 11, 90]

def ordernar_lista(lista: list) -> list:
    lista_ordenada = lista.copy()

    for i in range(len(lista_ordenada)):
        for j in range(i+1, len(lista_ordenada)):
            if lista_ordenada[i] > lista_ordenada[j]:
                lista_ordenada[i], lista_ordenada[j] = lista_ordenada[j], lista_ordenada[i]

    return lista_ordenada

print(ordernar_lista(lista))