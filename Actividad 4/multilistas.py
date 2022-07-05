import random
import pdb

pdb.set_trace()
def mayor():
    mayores = []
    lista = [[random.randint(0,15) for i in range(4)],
            [random.randint(0,15) for i in range(4)],
            [random.randint(0,15) for i in range(4)]]

    for i in lista:
        mayores.append(max(i))

    return lista,mayores

print(mayor())