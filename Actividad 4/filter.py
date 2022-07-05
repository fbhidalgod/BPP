def numerosPrimos():
    lista = [3, 4, 8, 5, 5, 22, 13]

    primos = list(filter(es_primo, lista))

    print(primos)

def es_primo(lista):
    for i in range(2,lista):
        if(lista != i and lista%i == 0):
            lista = 0
    return lista

numerosPrimos()