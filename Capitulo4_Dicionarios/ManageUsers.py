from Capitulo4_Dicionarios.Funcoes.ManagerUsersFuncoes import *

usuarios = {}

opcao = menu()
while opcao == "I" or opcao == "P" or opcao == "E" or opcao == "L":
    if opcao == "I":
        insertUser(usuarios)
    if opcao == "P":
        pesquisarUser(usuarios, input("Qual login deseja pesquisar? "))
    if opcao == "E":
        deletarUser(usuarios, input("Qual login deseja excluir? "))
    if opcao == "L":
        listar(usuarios)
    opcao = menu()
