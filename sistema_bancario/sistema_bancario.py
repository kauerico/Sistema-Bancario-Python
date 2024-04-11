menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
LIMITE_POR_SAQUE = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f} \n"

    elif opcao == "s":
        if numero_saques == LIMITE_SAQUES:
            print("Limite de saques diários ja foram alcançados. Tente outro dia! ")

        else:
            valor = float(input("Informa o valor do saque: "))

            if valor > LIMITE_POR_SAQUE:
                print("Saques somente abaixo de R$ 500,00")

            elif valor > saldo:
                print("Saldo insuficiente!")

            else:
                saldo -= valor
                extrato += f"Saque: R$ {valor:.2f} \n"
                numero_saques += 1

            
    elif opcao == "e":

        if extrato == "":
            print("================== EXTRATO ==================")
            print("Ainda não ocorreu nenhuma operação!")
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=============================================")

        else:
            print("================== EXTRATO ==================")
            print(extrato)
            print(f"\nSaldo: R$ {saldo:.2f}")
            print("=============================================")

    elif opcao == "q":
        break

    else:
        print("Opção inválida! Tente novamente.")
