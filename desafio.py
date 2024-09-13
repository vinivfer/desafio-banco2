
def menu():
    menu = """

    Bem-vindo ao nosso sistema bancário! Para iniciar, por favor, digite a opção desejada.

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Nova conta
    [5] Novo usuario
    [6] Listar contas
    [0] Sair

    => """
    return input(menu)

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"valor de R$ {valor:.2f} depositado! ")
    else:
        print("###Operação falhou! Valor informado é invalido.###")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! Valor máximo de saque: R$500,00")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n ###Saque realizado com sucesso!###")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def exibir_extrato(saldo,/,*, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF(somente numeros): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Esse cpf já está vinculado a um usuário.")
        return

    nome = input("Digite seu nome completo:")
    data_de_nasc = input("Digite sua data de nascimento (dd-mm-aaaa): ")
    endereco = input("Digite seu cep: ")
    numero_endereco = input("Digite o numero de sua residencia: ")

    usuarios.append({"nome": nome, "data_de_nasc": data_de_nasc, "endereco": endereco, "numero_endereco": numero_endereco})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite o cpf do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("Usuário não encontrado! Operação encerrada")

def listar_contas(contas):

    for conta in contas:
        linha = f"""\
            Agência:{conta['agencia']}
            C/C:{conta['numero_conta']}
            Titular:{conta['usuario']['nome']}
        """
        print("=" * 100)
        
        print(linha)


def main():
    AGENCIA = "0001"
    LIMITE_SAQUES = 5

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas= []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo= saldo,
                valor= valor,
                extrato= extrato,
                limite= limite,
                numero_saques= numero_saques,
                limite_saques= LIMITE_SAQUES,
            )



        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
            numero_conta = len(contas) + 1 
            conta = criar_conta(AGENCIA, numero_conta, usuarios)


        elif opcao == "5":
            usuarios = criar_usuario(usuarios)


            if conta:
                contas.append(conta)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "0":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
