#Sistema bancario 

menu = ("""
          Menu
    Opcoes:
    (d)depositar
    (s)sacar
    (e)extrato
    (q)sair

===> """)


saldo = 0
limite_max = 500
saques = 0
extrato = ""
LIMITE_SAQUE = 3

while True:
    print(menu, end="")
    opcao = input("").upper()

    #Deposito
    if opcao == "D":
        valor = float(input("valor a depositar: "))
        if valor <= 0:
            print("O valor a ser depositado precisa ser acima de 0")
        else:
            saldo += valor
            print(f"Saldo atual: {saldo}")
            extrato += f"Deposito de: R${valor:.2f}""\n"

    #Saque
    elif opcao == "S":
        if saques < LIMITE_SAQUE:
            valor_saque = float(input("Valor a sacar: "))
            if valor_saque <= 0:
                print("O valor do saque precisa ser positivo")
            elif valor_saque > saldo:
                print("Saldo insuficiente")
            elif valor_saque > limite_max:
                print("O saque excede o valor maximo")
            else:
                saldo -= valor_saque
                saques += 1
                print(f"Voce sacou: R${valor_saque:.2f}")
                extrato += f"Saque: R${valor_saque:.2f}\n"
        else:
            print("Limites de saques diarios atingido.")
            
    #Extrato
    elif opcao == "E":
        print(f"Extrato:\n{extrato}")     
        print(f"Saldo Atual: {saldo}")

    #Sair
    elif opcao == "Q":
        break

    #???
    else:
        print("Opcao invalida. Tente novamente")