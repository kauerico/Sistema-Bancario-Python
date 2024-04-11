'''
3 operações -> depósito, saque, extrato

deposito
    1. somente valores positivos 
    2. Todos os depósitos devem ser armazenados em uma variavel 
       e exibido na operação extrato

saque
    1. Somente 3 saque diários
    2. Limite máximo de 500,00 por saque
    3. Exibir mensagem para o usuário caso ele não tenha saldo
    4. Todos os saques devem ser armazenados em uma variavel e exibidas na operação extrato

extrato
    1. Listar todos os depósitos e saques realizados na conta
    2. No fim da listagem deve ser exibida o saldo atual
    3. Se o extrato estiver em branco, exibir a mensagm "Não foram
       realizadas movimentações"
    4. Os valores devem ser exibidos utilizando o formato R$ xxx.xx
'''

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