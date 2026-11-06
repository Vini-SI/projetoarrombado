from time import sleep
from funçoes import *

usuarios = []
cont1 = 1
# FUNÇÃO PARA CADASTRO
def cadastroUser(cont):
    while True:
        print("-" * 15, "Cadastro do Cliente", "-" * 15)
        nomeC = input("Digite o seu nome: ")
        idade = input("Digite a sua idade: ")
        idade = int(idade.strip())
        if idade < 18:
            print("Você é de menor, infelizmente não poderá realizar o cadastro")
            sleep(1.5)
            return cont
        
        usuario = [nomeC, idade, cont]

        usuarios.append(usuario)

        with open("Cadastrados.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write(f"{nomeC.strip()} / {idade} / {cont}\n")

        print(f"nome: {nomeC}, idade: {idade}, id: {cont}")
        sleep(1)
        print(f"Cliente Cadastrado com Sucesso!")
        sleep(1.5)
        return cont

def buscar():
    print("-" * 15, "Buscar cliente", "-" * 15)
    idB = input("Digite o id que voce quer procurar: ")
    
    encontrar = False

    with open("Cadastrados.txt", "r", encoding="utf-8") as arquivo:
        for user in arquivo:
            dados = user.strip().split("/")

            id = dados[2].strip()
            nome = dados[0].strip()
            idade = dados[1].strip()

            if idB == id:
                print(f"\nO usuario com nome {nome} com o id {id} e idade {idade} foi encontrado!")
                encontrar = True
                break

    if encontrar == False:
        print("Nenhum ID encontrado!")
        sleep(1.5)


def lerArquivo(nome):
    with open(nome, "r", encoding="utf-8") as arquivo:
        print(arquivo.read())

produtos = []
cont2 = 1
def cadastroProduto(cont):
    print("-" * 15, "Cadastro de Produto", "-" * 15)
    produtoC = input("Digite aqui o nome do produto: ")


    produto = [produtoC]
    produtos.append(produto)
    with open("Comidas.txt", "a", encoding="utf=8") as arquivo:
            arquivo.write(f"{produtoC} / {cont}")

    cont += 1
    print("Produto Cadastrado com Sucesso!")
    print(f"O seu produto é: {produtoC} e id: {cont}")
    return cont

def buscarProduto ():
    print("-" * 15, "Busca de Produto", "-" * 15)

    idBP = input("Digite o id do produto que você quer procurar: ")

    encontrar = False

    with open("Comidas.txt", "a", encoding="utf-8") as arquivo:
        for p in arquivo:
            alimento = p.strip().split()

            idC = alimento[1]
            comida = alimento[0]

            if idBP == idC:
                print(f"Produto de nome {comida} e id {idC} encontrado com sucesso!")
                encontrar = True

    if encontrar == False:
        print("ID de produto não encontrado")
        sleep(1.5)
                
                


# TITULO DO NEGOCIO
painel("               SISTEMA DE GERENCIAMENTO           ")

# CODIGO QUE TA RODANDO
while True:
    digito = menu(["Gerenciar Clientes", "Gerenciar Produtos", "Gerenciar Vendas", "Sair"])
    if digito == "1":
        while True:
            escolha = menu(["CADASTRAR", "BUSCAR", "SAIR"])
            if escolha == "1":
                cadastroUser(cont1)
            elif escolha == "2":
                buscar()
            elif escolha == "3":
                print("Voltando")
                sleep(1.5)
                break

    elif digito == "2":
        while True:
            opc = menu(["Cadastrar", "Buscar", "Sair"])
            if opc == "1":
                cadastroProduto(cont2)
            elif opc == "2":
                buscarProduto()
            elif opc == "3":
                print("Voltando...")
                sleep(1.5)
                break

    elif digito == "3":
        print("Programa Encerrado")
        break

    else:
        print("\nDigite uma opção valida\n")
    sleep(1)
