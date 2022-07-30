equipamento = []
valor = []
serial = []
departamento = []
resposta = "S"
while resposta == "S":
    equipamento.append(input("Equipamento: "))
    valor.append(float(input("Valor: ")))
    serial.append(input("Número Serial: "))
    departamento.append(input("Departamento: "))
    resposta = input("Digite 'S' para continuar: ").upper()
for indice in range(0, len(equipamento)):
    print("Equipamento..: ", (indice + 1))
    print("Nome.........: ", equipamento[indice])
    print("Valor........: ", valor[indice])
    print("Número Serial: ", serial[indice])
    print("Departamento.: ", departamento[indice])

busca = input("Digite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamento)):
    if busca == equipamento[indice]:
        print("Valor.......: ", valor[indice])
        print("Serial......: ", serial[indice])
        print("Departamento: ", departamento[indice])
depreciacao = input("Digite o nome do equipamento que sofreu depreciação: ")
for indice in range(0, len(equipamento)):
    if depreciacao == equipamento[indice]:
        print("Valor antigo: ", valor[indice])
        valor[indice] = valor[indice] * 0.9
        print("Valor atual: ", valor[indice])
descarte = input("Digite o número Serial da máquina descartada: ")
for indice in range(0, len(equipamento)):
    if descarte == serial[indice]:
        del equipamento[indice]
        del valor[indice]
        del serial[indice]
        del departamento[indice]
        print("Máquina deletada dos arquivos")
        print("Nome.........: ", equipamento[0])
        print("Valor........: ", valor[0])
        print("Número Serial: ", serial[0])
        print("Departamento.: ", departamento[0])
        break
    else:
        print("Máquina não encontrada.")
