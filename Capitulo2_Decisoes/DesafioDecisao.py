acesso = input("Digite o seu nível de acesso: ").upper()
if acesso == "ADMINISTRADOR":
    genero = input("Digite o seu gênero: ").upper()
    if genero == "MASCULINO":
        print("Olá administrador")
    else:
        print("Olá administradora")
if acesso == "USUARIO":
    genero = input("Digite o seu gênero: ").upper()
    if genero == "MASCULINO":
        print("Olá usuário")
    else:
        print("Olá usuária")
if acesso == "CONVIDADO":
    genero = input("Digite o seu gênero: ").upper()
    if genero == "MASCULINO":
        print("Olá convidado")
    else:
        print("Olá convidada")
if acesso != "ADMINISTRADOR" or acesso != "USUARIO" or acesso != "CONVIDADO":
    print("Olá desconhecido(a)")
