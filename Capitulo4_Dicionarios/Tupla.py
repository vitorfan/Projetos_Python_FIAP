ips={}
resp="S"
while resp =="S":
    ips[(input("Digite os dois primeiros octetos: "),
         input("Digite os dois últimos octetos: "))]=input("Nome da máquina: ")
    resp=input("Digite 'S' para continuar: ").upper()

print("Exibindo IP's: ")
for ip in ips.keys():
    print(ip[0]+"."+ip[1])

print("Exibindo máquinas com o mesmo endereço: ")
sameAdress=input("Digite os dois últimos octetos: ")
for ip,nome in ips.items():
    print("Máquinas no mesmo endereço(redes diferentes)")
    if(ip[1] == sameAdress):
        print(nome)
print("Exibindo máquinas que compõem uma mesma rede: ")
rede=input("Digite os dois primeiros octetos: ")
for ip,nome in ips.items():
    print("Máquinas na mesma rede")
    if ip[0] == rede:
        print(nome)
