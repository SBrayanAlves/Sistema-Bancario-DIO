# Sistema bancário

menu = ("""
          Menu
    Opções:
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

    # Depósito
    if opcao == "D":
        valor = float(input("Valor a depositar: "))
        if valor <= 0:
            print("O valor a ser depositado precisa ser acima de 0.")
        else:
            saldo += valor
            print(f"Saldo atual: R${saldo:.2f}")
            extrato += f"Depósito: R${valor:.2f}\n"

    # Saque
    elif opcao == "S":
        if saques < LIMITE_SAQUE:
            valor_saque = float(input("Valor a sacar: "))
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
            
    # Extrato
    elif opcao == "E":
        print("Extrato:")
        print(extrato if extrato else "Nenhuma movimentação realizada.")
        print(f"Saldo atual: R${saldo:.2f}")

    # Sair
    elif opcao == "Q":
        break

    # Opção inválida
    else:
        print("Opção inválida. Tente novamente.")