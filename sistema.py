from time import sleep
import os

#LINHA
def linha():
    print("-" * 40)


#FUNÇÃO DE PAINEL
def painel(txt):
    linha()
    print(txt)
    linha()


#FUNÇÃO PARA O MENU DE ESCOLHA DOQUE VOCE QUER FAZER
def menu(lista):
    painel("ESCOLHA SUA OPÇÃO")
    cont = 1
    for item in lista:
        print(f"{cont} - {item}")
        cont += 1
    linha()
    opcao = input("Digite sua opção: ")
    return opcao


#FUNÇÃO PARA CADASTRO
def cadastro():
    print("-" * 15,"Cadastro", "-" * 15)
    nomeC = input("Digite o seu nome(Digite 0 para voltar ao menu): ")
    if nomeC == "0":
            print("Voltando...")
            sleep(2)
            return
    senhaC = input("Digite a sua senha(Digite 0 para voltar ao menu): ")
    if senhaC == "0":
        print("Voltando...")
        sleep(2)
        return
    idade = input("Digite a sua idade(Digite 0 para voltar ao menu): ")
    if idade == "0":
            print("Voltando...")
            sleep(2)
            return
    while not idade.isnumeric():
        print("Digite um idade numerica")
        idade = input("Digite a sua idade: ")
    idade = int(idade.strip())
    if idade < 18:
        print("Você é de menor, infelizmente não poderá realizar o cadastro")
        return
    with open("Cadastrados.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"{nomeC.strip()}, {senhaC.strip()}, {idade}\n")
    print("Cadastro concluído!")
    return nomeC.strip(), senhaC.strip(), idade

def lerArquivo(nome):
    with open(nome, "r", encoding="utf-8") as arquivo:
        print(arquivo.read())


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
                print(f"Bem-Vindo {nomeC}")
                return True
            
            return False 
            
    print("Nome ou senha incorretos")

def listaLanches():
    print("")


#TITULO DO NEGOCIO
painel("               LANCHONETE           ")

#CODIGO QUE TA RODANDO
while True:
    digito = menu(["CADASTRO", "LOGIN", "SAIR"])
    if digito == "1":
        #CADASTRO DO USUARIO
        cadastro()

    elif digito == "2":
        #LOGIN DO USUARIO
        if login():
            listaLanches()

    elif digito == "3":
        print("Programa Encerrado")
        break

    else:
        print("\nDigite uma opção valida\n")
    sleep(1)