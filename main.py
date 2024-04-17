from datetime import datetime
from validate_docbr import CPF


#declarando variaveis 

saques = 0
data_atual = datetime.now()
usuarios = []
contas = []
accountNumber = 0


def createUser():
    nome = input("digite seu nome: ")
    data_nascimento = input("digite sua data de nascimento: ")
    cpf = input("Digite seu cpf: ")
    

    if not CPF().validate(cpf):
        print("Cpf inválido")
        return None
    
    #Verifica se o nome não é nulo
    if nome == None: print("Digite um nome válido") 
   
    #verifica se o cpf é válido
    if CPF(cpf) == False: print("Digite um CPF válido")

    endereco = {
        "logradouro": input("Digite o logradouro: "),
        "cidade":  input("Digite sua cidade: "),
        "estado": input("Digite a sigla do seu estado: ")
    }

    user = {
        "nome": nome,
        "cpf": cpf, 
        "data_nascimento": data_nascimento,
        "endereço": endereco
    }    
    usuarios.append(user)
    print(user)
    return user
    


def createAcc():
    global accountNumber, usuarios
    user = createUser()
    if user is not None:

        accountNumber += 1

        cpf = user["cpf"]

        contas.append({
            "cpf": cpf,
            "nome": user["nome"],
            "agencia": "0001",
            "NumeroConta": accountNumber,
            "saldo": 0,
            "senha": input("Digite sua senha: "),
            "extrato": []
        })
        print(contas)
        return contas
    



def deposit():
    global  saldo, extrato, contas, users
    
    numeroConta = input("Digite o numero da conta: ")
    senha = input("Digite sua senha: ")
    


    for conta in contas:
        if numeroConta == str(conta["NumeroConta"]) and senha == conta["senha"]:
            print(f"Olá {conta['nome']}")
            print("Senha correta")
        
            valor = float(input("Digite o valor a ser depositado :"))
            if(valor <= 500):
                conta["saldo"] += valor
                print(f"Depósito de {valor} realizado com sucesso. Saldo atual: R${conta['saldo']:.2f}")
                conta["extrato"].append(f"Depósito de R${valor} Reais na data {data_atual}")
                return conta["saldo"]
                    
            else:
                print("Deposito máximo de R$500,00 reais")
                    
        else: 
            print("Senha inválida")


    

    

def withdrawal():
    numeroConta = input("Digite o numero da conta: ")
    senha = input("Digite sua senha: ")
    

    for conta in contas:
        if str(conta["NumeroConta"]) == numeroConta:
            if(conta["senha"] == senha):
                print("senha correta!")
                

                valor = float(input("digite o valor para saque"))

                if conta["saldo"] >= valor:
                    conta["saldo"] -= valor
                    print(f"Saque de {valor} realizado com sucesso, saldo atual: R${conta['saldo']:.2f}")
                    conta["extrato"].append(f"Saque de R${valor} Reais na data {data_atual}") 
                    return conta["saldo"]

                else:
                    print("Saldo insuficiente")
                    
        else:
            print("Senha ou numero de conta inválido")  


def statement():
    numeroConta = input("Digite o numero da conta: ")
    senha = input("Digite sua senha:  ")
    
    for conta in contas:
        if str(conta["NumeroConta"]) == numeroConta and conta["senha"] == senha:
            print(f"""
                ------------------------------
                            EXTRATO
                ------------------------------
                    
                """)
            for conta in contas:
                print(f"""
                Olá {conta['nome']}, segue seu extrato:
                {conta['extrato']}                      
                      """)
                print(f"SALDO EM CONTA: R${conta['saldo']:.2f}")
        else:
            print("Não foram realizadas movimentações")

print("""
      ------------------------------------------------
                INICIANDO OPERAÇÃO BANCARIA
      -------------------------------------------------
          MENU

          1 = DEPOSITAR
          2 = SACAR
          3 = EXTRATO
          4 = Cria conta
          5 = SAIR 
      
      """)


while True:
    opr = int(input("Digite a opção desejada: "))

    if opr == 1:
        
        deposit()
    elif opr == 2:
        
        withdrawal()
    elif opr == 3:
        statement()
    elif opr == 4:
        createAcc()
    elif opr == 5:
        print("Saindo...")
        break
    else:
        print("Digite uma opção válida")