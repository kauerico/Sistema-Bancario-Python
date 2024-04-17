from colorama import init, Fore, Style

init(autoreset=True)  # Inicializa o colorama para que as cores sejam resetadas após cada mensagem

def menu():
    """
    Apresenta um menu de opções para interação com o sistema bancário.

    Retorna:
        str: A opção selecionada pelo usuário.
    """
    print(Fore.BLUE + "╔═════════════════════════════════════════╗")
    print("║            " + Style.BRIGHT + "Sistema Bancário" + Style.RESET_ALL + "             ║")
    print("╠═════════════════════════════════════════╣")
    print("║ Selecione uma opção:                    ║")
    print("║ 1. Criar novo usuário                   ║")
    print("║ 2. Abrir nova conta corrente            ║")
    print("║ 3. Realizar saque                       ║")
    print("║ 4. Realizar depósito                    ║")
    print("║ 5. Ver extrato                          ║")
    print("║ 6. Listar contas correntes              ║")
    print("║ 7. Sair                                 ║")
    print("╚═════════════════════════════════════════╝")

    opcao = int(input(Fore.BLUE + "Digite o número da opção desejada: "))
    print("========================")
    return opcao

def sacar(*, saldo, valor_saque, extrato, limite_saques_dia , numero_saques, limite_saque):
    '''
    Realiza um saque na conta bancária.

    Parâmetros:
        saldo (float): O saldo atual da conta bancária.
        valor_saque (float): O valor a ser sacado.
        extrato (list): Uma lista contendo o registro das transações.
        limite_saques_dia (int): O limite de saques permitidos por dia.
        numero_saques (int): O número de saques já realizados no dia.
        limite_saque (float): O limite de valor por saque.

    Retorna:
        tupla: Uma tupla contendo o saldo atualizado após o saque e o extrato atualizado.

    '''

    if numero_saques == limite_saques_dia:
        print(Fore.RED + "Você já realizou o limite de saques diários. Por favor, tente novamente amanhã.") 

    else:
        
        if valor_saque > limite_saque:
            print(Fore.RED + "\nLimite de saque por operação é de R$ 500,00. Por favor, insira um valor válido.\n")

        elif valor_saque > saldo:
            print(Fore.RED + "\nSaldo insuficiente para realizar o saque.\n")
        
        else:
            saldo -= valor_saque
            extrato += f"Saque: R$ {valor_saque:.2f} \n"
            numero_saques += 1
            print(Fore.GREEN + "==== Saque realizado com sucesso ====\n")

    return saldo, extrato


def depositar(saldo, valor_deposito, extrato):
    '''
    Realiza depósito na conta bancária.

    Parâmetros: 
        saldo (float): O saldo atual da conta bancária.
        valor_deposito (float): O valor a ser depositado.
        extrato (list): Uma lista contendo o registro das transações.

    Retorna: 
        tupla: Uma tupla contendo o saldo atualizado após o depósito e o extrato atualizado.

    '''
      
    if valor_deposito > 0:
        saldo += valor_deposito
        extrato += f"Depósito: R$ {valor_deposito:.2f} \n"
        print(Fore.GREEN + "==== Depósito realizado com sucesso ====\n")
        
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    '''
    Imprime o extrato da conta bancária.

    Esta função imprime o extrato da conta bancária, incluindo todas as transações registradas.
    
    Parâmetros: 
        saldo (float): O saldo atual da conta bancária.
        extrato (str): Uma string contendo o registro das transações.

    Retorna: 
        None
    
    '''

    if not extrato:
        print(Fore.YELLOW + "================== EXTRATO ==================")
        print("Ainda não houve nenhuma transação.")
        print(f"\nSaldo atual: R$ {saldo:.2f}")
        print("=============================================\n")

    else:
        print(Fore.YELLOW + "================== EXTRATO ==================")
        print(extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("=============================================\n")


def criar_usuario(lista_usuarios): 
    """
    Cria um novo usuário e o adiciona à lista de usuários.

    Parâmetros:
        lista_usuarios (list): A lista de usuários onde o novo usuário será adicionado.

    Retorna:
        None

    """
    print(Fore.CYAN + "===== Novo Usuário =====")
    novo_usuario = {
        "Nome": input("Informe seu nome completo: "),
        "Data de Nascimento": input("Informe sua data de nascimento (DD/MM/AAAA): "),
        "CPF": input("Informe seu CPF (apenas números): "),
        "Endereço": {
            "Logradouro": input("Informe seu endereço (logradouro): "),
            "Número": input("Informe o número: "),
            "Bairro": input("Informe o bairro: "),
            "Cidade/Estado": input("Informe a cidade e o estado (sigla): ")
        }
    }

    # Verifica se o usuário já não está cadastrado
    for usuario in lista_usuarios:
        if usuario["CPF"] == novo_usuario["CPF"]:
            print(Fore.RED + "!!! Este CPF já está cadastrado no sistema. Por favor, insira um CPF válido. !!!")
            print("======================================================================================\n")
            return

    # Cadastra os novos usuários
    lista_usuarios.append(novo_usuario)
    print(Fore.GREEN + "=== Usuário cadastrado com sucesso! ===")
    print("=======================================\n")
        

def criar_conta_corrente(agencia, numero_conta, lista_usuarios):
    '''
    Cria uma nova conta corrente para um usuário existente.

    Esta função solicita o CPF do usuário e verifica se existe na lista de usuários.
    Se o usuário for encontrado, uma nova conta corrente é criada para ele com a agência e número de conta fornecidos.

    Parâmetros:
        agencia (str): O número da agência da conta corrente.
        numero_conta (int): O número da conta corrente.
        lista_usuarios (list): A lista de usuários onde será procurado o usuário pelo CPF.

    Retorna:
        dict or None: Um dicionário representando a nova conta corrente criada, contendo as informações da agência,
                      número da conta e o usuário associado. Retorna None se o usuário não for encontrado.
    '''

    cpf = input("Informe o CPF do titular da conta: ")
    
    for usuario in lista_usuarios:
        if usuario["CPF"] == cpf:  # Corrigido aqui
            print(Fore.GREEN + "==== Conta corrente criada com sucesso ====\n")
            conta = {"Agência": agencia, "Número da Conta": numero_conta, "Titular": usuario}
            return conta
        
    print(Fore.RED + "!!! Usuário não encontrado. Por favor, cadastre o usuário antes de criar a conta. !!!\n")
    return None


def listar_contas(contas):
    """
    Lista todas as contas correntes registradas.

    Parâmetros:
        contas (list): A lista de contas correntes.

    Retorna:
        None
    """
    if not contas:
        print(Fore.YELLOW + "\nNenhuma conta corrente registrada no sistema.\n")
    else:
        print(Fore.CYAN + "=== Contas Correntes ===")
        for i, conta in enumerate(contas, start=1):
            print(f"Conta {i}:")
            print(f"Agência: {conta['Agência']}")
            print(f"Titular:")
            print(f"  Nome: {conta['Titular']['Nome']}")
            print(f"  CPF: {conta['Titular']['CPF']}")
            print("-------------------------")


def main():
    LIMITE_POR_SAQUE = 500
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0 
    extrato = ""
    numero_saques = 0
    lista_usuarios = []
    contas = []
    

    while True:
        opcao = menu()

        if opcao == 1: 
            criar_usuario(lista_usuarios)

        elif opcao == 2:
            numero_conta = len(contas) + 1
            conta = criar_conta_corrente(agencia=AGENCIA, 
                                lista_usuarios=lista_usuarios,
                                numero_conta=numero_conta)
            if conta:
                contas.append(conta)

        elif opcao == 3:
            valor_saque = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(saldo=saldo, valor_saque=valor_saque, extrato=extrato,
                  limite_saques_dia=LIMITE_SAQUES, 
                  numero_saques=numero_saques,
                  limite_saque=LIMITE_POR_SAQUE)
            
        elif opcao == 4:
            valor_deposito = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo=saldo, valor_deposito=valor_deposito, extrato=extrato)

        elif opcao == 5:
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == 6:
            listar_contas(contas)

        elif opcao == 7:
            print(Fore.YELLOW + "Sistema encerrado. Obrigado por utilizar nosso serviço!")
            break

main()
