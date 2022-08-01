def menu():
    resposta = input("Digite a letra correspondente a função desejada para continuar:\n" +
                  "Digite 'I' para inserir\n" +
                  "Digite 'P' para pesquisar\n" +
                  "Digite 'E' para excluir\n" +
                  "Digite 'L' para listar\n").upper()
    return resposta

def insertUser(dicionario):
    dicionario[str(input("Digite a Matrícula: "))] =[input("Digite o nome: ").upper(),
                                                     input("Digite a última data de acesso: "),
                                                     input("Qual a última estação acessada: ").upper(),
                                                     input("Qual a hora do acesso: "),
                                                     input("Qual o nível de acesso: ").upper(),
                                                     input("Qual o Login? ").upper()]

def pesquisarUser(dicionario, login):
    pesquisa=dicionario.get(login[5])
    if pesquisa != None:
         print("Nome....................: " + pesquisa[0])
         print("Último acesso...........: " + pesquisa[1])
         print("Última estação..........: " + pesquisa[2])
         print("Último horário de acesso: " + pesquisa[3])
         print("Nível de acesso.........: " + pesquisa[4])
         print("Matricula...............: " + pesquisa)

def deletarUser(dicionario, login):
    excluir=dicionario.get(login[5])
    if excluir!= None:
        del dicionario[login]
    print(("Usuário deletado"))

def listar(dicionario):
    for chave, valor in dicionario.items():
        print("Objeto.....")
        print("Matrícula: ", chave)
        print("Dados: ", valor)
