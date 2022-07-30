def preencherInventario(lista):
    resp = "S"
    while resp == "S":
        equipamento = [input("Equipamento: "),
                       float(input("Valor: ")),
                       int(input("Número Serial: ")),
                       input("Departamento: ")]
    lista.append(equipamento)
    resp = input("Digite 'S' para continuar: ").upper()


def exibirInventario(lista):
    for elemento in lista:
        print("Equipamento..: ", elemento[0])
        print("Valor........: ", elemento[1])
        print("Número Serial: ", elemento[2])
        print("Departamento.: ", elemento[3])


def localizarPorNome(lista):
    busca = input("Digite o nome do equipamento que deseja buscar: ")
    for elemento in lista:
        if busca == elemento[0]:
            print("Valor........: ", elemento[1])
            print("Número Serial: ", elemento[2])


def depreciarPorNome(lista, porc):
    depreciacao = input("Digite o nome do equipamento que deseja depreciar: ")
    for elemento in lista:
        if depreciacao == elemento[0]:
            print("Valor antigo: ", elemento[1])
            elemento[1] = elemento[1] * (1 - porc / 100)
            print("Valor depreciado: ", elemento[1])


def excluirPorSerial(lista):
    serial = int(input("Digite o Serial do produto que deseja excluir: "))
    for elemento in lista:
        if serial == elemento[2]:
            lista.remove(elemento)
    return "Itens excluídos."


def resumirValores(lista):
    valores = []
    for elemento in lista:
        valores.append(elemento[1])
    if len(valores) > 0:
        print("O valor mais alto encontrado é: ", max(valores))
        print("O valor mais baixo do inventário é: ", min(valores))
        print("O total de equipamentos é de: ", sum(valores))
