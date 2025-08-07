# Sistema bancário
AGENCIA = "0001"
numero_conta = 0

#lista de usuario
usuarios = []
contas = []

def procurar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if cpf == usuario['cpf']:
            return usuario
    return

def Cadastrar_usuario(usuarios):
    cpf = input("Digite seu CPF: ")
    usuario = procurar_usuario(cpf, usuarios)
    if usuario:
        return print("Usuario ja cadastrado")
    else:
        nome = input("Digite seu nome: ")
        data_nascimento = input("Digite sua data de nascimento: ")
        endereco = input("Digite seu endereco, logradouro, numero - bairro - cidade - sigla estado: ")   
        usuarios.append({"nome": nome, "cpf": cpf, "data_nascimento": data_nascimento, "endereco": endereco})
    return print(f"Usuario {nome} cadastrado com sucesso!")

def Cadastrar_Conta_Bancaria(agencia, numero_conta, usuarios, contas):
    cpf = input("Digite seu CPF: ")
    usuario = procurar_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada com sucesso!")
        numero_conta += 1
        contas.append({"Agencia": agencia, "numero da conta": numero_conta, "usuario": usuario})
        print(f"Agencia: {agencia}, numero da conta: {numero_conta}, usuario: {usuario}")
        return numero_conta
    else:
        print("Usuario nao encontrado")

def Depositar(saldo, valor, extrato, /):
    if valor <= 0:
        print("O valor a ser depositado precisa ser acima de 0.")
    else:
        saldo += valor
        print(f"Saldo atual: R${saldo:.2f}")
        extrato += f"Depósito: R${valor:.2f}\n"
    return saldo, extrato
    
def Saque(*, saldo, valor_saque, extrato, limite_max, saques, LIMITE_SAQUE):
    if saques < LIMITE_SAQUE:
        if valor_saque <= 0:
            print("O valor do saque precisa ser positivo.")
        elif valor_saque > saldo:
            print("Saldo insuficiente.")
        elif valor_saque > limite_max:
            print("O saque excede o valor máximo.")
        else:
            saldo -= valor_saque
            saques += 1
            print(f"Você sacou: R${valor_saque:.2f}")
            extrato += f"Saque: R${valor_saque:.2f}\n"
    else:
        print("Limite de saques diários atingido.")
    return saldo, extrato, saques
    
def Extrato(saldo, /, *, extrato):
    print("Extrato:")
    print(extrato if extrato else "Nenhuma movimentação realizada.")
    print(f"Saldo atual: R${saldo:.2f}")
    
menu = ("""
          Menu
    Opções:
    (cd) Cadastrar usuario
    (cb) Cadastrar conta bancaria
    (d) Depositar
    (s) Sacar
    (e) Extrato
    (q) Sair

===> """)

saldo = 0
limite_max = 500
saques = 0
extrato = ""
LIMITE_SAQUE = 3

while True:
    print(menu, end="")
    opcao = input("").upper()

    #Cadastrar usuario
    if opcao == "CD":
        Cadastrar_usuario(usuarios)
    
    #Cadastrar conta bancaria
    elif opcao == "CB":
        numero_conta = Cadastrar_Conta_Bancaria(AGENCIA, numero_conta, usuarios, contas)

    # Depósito
    elif opcao == "D":
        valor = float(input("Valor a depositar: "))
        saldo, extrato = Depositar(saldo, valor, extrato)

    # Saque
    elif opcao == "S":
        valor_saque = float(input("Valor a sacar: "))
        saldo, extrato, saques = Saque(saldo = saldo, valor_saque = valor_saque, extrato = extrato, limite_max = limite_max, saques = saques, LIMITE_SAQUE = LIMITE_SAQUE)
            
    # Extrato
    elif opcao == "E":
        Extrato(saldo, extrato = extrato)

    # Sair
    elif opcao == "Q":
        break

    # Opção inválida
    else:
        print("Opção inválida. Tente novamente.")