nome = input ("Digite o nome: ")
idade = int (input("Digite a Idade: "))
prioridade = "Não"
if idade >= 65:
    prioridade="Sim"
print("O(A) paciente " + nome + " possui atendimento prioritário? " + prioridade)
