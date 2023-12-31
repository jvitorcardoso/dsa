def binarySearch(lista: list, item: int) -> int:
    baixo = 0
    alto = len(lista) - 1

    while baixo <= alto:
        meio = (baixo + alto) // 2
        chute = lista[meio]

        if chute == item:
            return meio
        
        elif chute > item:
            alto = meio - 1

        else:
            baixo = meio + 1

    return None

minha_lista = list(range(0, 101, 4))

print(binarySearch(minha_lista, 100))