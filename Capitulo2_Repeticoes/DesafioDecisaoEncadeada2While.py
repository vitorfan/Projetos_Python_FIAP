nome = input ("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()
while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
    doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? Responda com SIM ou NAO").upper()

# Primeira decisão
if doenca_infectocontagiosa=="SIM":
    print("Encaminhe o paciente para a sala AMARELA")
else:
    print("Encaminhe o paciente para a sala Branca")

# Segunda decisão
if idade >= 65:
    print("Paciente COM prioridade")
else:
    genero=input("Digite o gênero do paciente: ").upper()
    if genero == "FEMININO" and idade>10:
        gravidez = input("A paciente está grávida? ").upper()
        if gravidez == "SIM":
            print("Paciente COM prioridade")
        else:
            print("Paciente SEM prioridade")
    else:
            print("Paciente SEM prioridade")