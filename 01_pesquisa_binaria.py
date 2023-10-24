
def pesquisa_binaria(lista, item):
    comeco = 0  # começo da array
    final = len(lista) - 1  # final da array

    # Enquanto você não tenha reduzido a 1 elemento (apenas) / não tenho acertado
    while comeco <= final:
        # // faz a função do floor, arredondar o número pra baixo
        # Achando o meio da array/lista
        meio_real = (comeco + final) / 2
        meio = (comeco + final) // 2
        chute = lista[meio]
        print("Meio:", meio)
        print("Meio Real:", meio_real)
        print("Chute Número:", chute)
        print("Bucket:", meio)

        # Achamos o item
        if chute == item:
            return meio
        # Chute foi abaixo
        if chute < item:
            print("Chute Baixo")
            comeco = meio + 1
            print("Começo:", comeco)
        # Chute foi acima
        elif chute > item:
            print("Chute Alto")
            final = meio - 1
            print("Final:", final)
    return None

# Lembre-se que a lista deve estar ordenada!
# Pois quando fazemos a checagem dos itens (chute > item), checamos seus valores e não a suas respectivas posições

#              0  1  2  3  4  5   6
minha_lista = [1, 3, 6, 7, 9, 80, 50]
print(pesquisa_binaria(minha_lista, 50))
