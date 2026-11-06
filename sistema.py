from time import sleep
import os
from funçoes import *

usuarios = []
cont = 1
# FUNÇÃO PARA CADASTRO
def cadastro(cont):
    print("-" * 15, "Cadastro do Cliente", "-" * 15)
    nomeC = input("Digite o seu nome: ")
    idade = input("Digite a sua idade: ")
    idade = int(idade.strip())
    if idade < 18:
        print("Você é de menor, infelizmente não poderá realizar o cadastro")
        return cont
    usuario = [nomeC, idade, cont]
    usuarios.append(usuario) 
    with open("Cadastrados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nomeC.strip()} / {idade} / {cont}\n")

    cont += 1
    print("Cliente Cadastrado!")
    return cont


def buscar():
    print("-" * 15, "Buscar cliente", "-" * 15)
    idB = input("Digite o id que voce quer procurar: ")

    if not os.path.exists("Cadastrados.txt"):
        print("Nenhum usuário com esse ID encontrado!")
        return
    
    encontrar = False

    with open("Cadastrados.txt", "r", encoding="utf-8") as arquivo:
        for user in arquivo:
            dados = user.strip().split("/")

            id = dados[2].strip()
            nome = dados[0].strip()
            idade = dados[1].strip()

            if idB == id:
                print(f"\nO usuario {nome} com o id {id} e idade {idade}")
                encontrar = True
                break

    if encontrar == False:
        print("Nenhum ID encontrado!")


def lerArquivo(nome):
    with open(nome, "r", encoding="utf-8") as arquivo:
        print(arquivo.read())

# Login do usuário


def login():
    print("-" * 20, "Login de usuário", "-" * 20)

    nomeL = input("Digite seu nome: ")
    senhaL = input("Digite sua senha: ")

    if not os.path.exists("Cadastrados.txt"):
        print("Nenhum usuário com esse nome ou senha encontrado!")
        return

    with open("Cadastrados.txt", "r", encoding="utf-8") as arquivo:
        for user in arquivo:
            dados = user.strip().split(",")

            nomeC = dados[0].strip()
            senhaC = dados[1].strip()
            if nomeL == nomeC and senhaL == senhaC:
                print(f"\nBem-Vindo {nomeC}\n\n")
                return True

        return False

    print("Nome ou senha incorretos")


def listaLanches(comida):
    preco = [6.00, 4.00, 3.29, 3.78]
    cont = 1
    for item in comida:
        for valor in preco:
            print(f"{cont} ------ {item} ------ {valor}")
        with open("Comidas.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{item} / ")
    cont += 1
    linha()
    opc = input("Digite o item de sua escolha: ")
    return opc


# TITULO DO NEGOCIO
painel("               SISTEMA DE GERENCIAMENTO           ")

# CODIGO QUE TA RODANDO
while True:
    digito = menu(["Gerenciar Clientes", "Gerenciar Produtos", "Gerenciar Vendas", "Sair"])
    if digito == "1":
        while True:
            escolha = menuCliente(["CADASTRAR", "BUSCAR", "SAIR"])
            if escolha == "1":
                cadastro()
            elif escolha == "2":
                buscar()
            elif escolha == "3":
                break

    elif digito == "2":
        # LOGIN DO USUARIO
        if login():
            e = listaLanches(["PASTEL", "COXINHA", "GUARÁNA", "COCA-COLA"])

    elif digito == "3":
        print("Programa Encerrado")
        break

    else:
        print("\nDigite uma opção valida\n")
    sleep(1)
