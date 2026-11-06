# LINHA
def linha():
    print("-" * 40)


# FUNÇÃO DE PAINEL
def painel(txt):
    linha()
    print(txt)
    linha()


# FUNÇÃO PARA O MENU DE ESCOLHA DOQUE VOCE QUER FAZER
def menu(lista):
    painel("ESCOLHA SUA OPÇÃO")
    cont = 1
    for item in lista:
        print(f"{cont} - {item}")
        cont += 1
    linha()
    opcao = input("Digite sua opção: ")
    return opcao


def menuCliente(lista):
    painel("ESCOLHA SUA OPÇÃO")
    cont = 1
    for item in lista:
        print(f"{cont} - {item}")
        cont += 1
    linha()
    opcao = input("Digite sua opção: ")
    return opcao
