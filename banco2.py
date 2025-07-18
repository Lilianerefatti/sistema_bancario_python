import textwrap


def menu():
    menu = """\n
    =================== MENU =================== 
        [d] Depositar
        [s] Sacar
        [e] Extrato
        [nu] Novo Usuário
        [nc] Nova Conta
        [lc] Listar Contas
        [q] Sair
        ==> """
    return textwrap.dedent(menu)
print("=" * 100)


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("✅ Depósito realizado com sucesso.")
    else:
        print("❌ Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("❌ Operação falhou! Saldo insuficiente.")

    elif excedeu_limite:
        print("❌ Operação falhou! O valor excede o limite.")

    elif excedeu_saques:
        print("❌ Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("✅ Saque realizado com sucesso.")

    else:
        print("❌ Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("❌ Já existe um usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ").strip()
    nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ").strip()
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ").strip()

    usuarios.append({"nome": nome, "data_nascimento": nascimento, "cpf": cpf, "endereco": endereco})
    
    print("✅ Usuário criado com sucesso.")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ").strip()
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("✅ Conta criada com sucesso.")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    else:
        print("❌ Usuário não encontrado. Cadastre-o primeiro.")
        return None


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência: \t{conta['agencia']}
            C/C:\t\t {conta['numero_conta']}
            Titular:\t {conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 5000
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = input(menu())

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("🏦 Obrigado por usar nosso sistema bancário!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
