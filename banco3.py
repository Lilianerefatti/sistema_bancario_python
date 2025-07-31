import textwrap
from abc import ABC, abstractclassmethod,abstractmethod
from datetime import datetime

# ===================== CLASSES DE DOMÍNIO ===================== 
# =========== CLIENTE  ===========
class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []
    
    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nascimento, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.cpf = cpf
        self.data_nascimento = data_nascimento

# =========== CONTA  ===========
class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._agencia = "0001"
        self._saldo = 0
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        if valor <= 0:
            print("❌ Operação inválida! Valor deve ser positivo.")
            return False
        if valor > self._saldo:
            print("❌ Saldo insuficiente.")
            return False
        self._saldo -= valor
        print(f"✅ Saque de R$ {valor:.2f} realizado com sucesso.")
        return True

    def depositar(self, valor):
        if valor <= 0:
            print("❌ Operação inválida! Valor deve ser positivo.")
            return False
        self._saldo += valor
        print(f"✅ Depósito de R$ {valor:.2f} realizado com sucesso.")
        return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques
        self.numero_saques = 0

    def sacar(self, valor):
        if self.numero_saques >= self.limite_saques:
            print("❌ Limite de saques diários atingido.")
            return False
        if valor > self.limite:
            print("❌ Valor excede o limite por saque.")
            return False
        if super().sacar(valor):
            self.numero_saques += 1
            return True
        return False

# =========== HISTÓRICO  ===========
class Historico:
    def __init__(self):
        self._transacoes = []
    
    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append({
            "tipo": transacao.__class__.__name__,
            "valor": transacao.valor,
            "data": datetime.now().strftime("%d/%m/%Y   %H:%M:%S")
        })

    def extrato(self, conta):
        print("\n========== EXTRATO ==========")
        if not self.transacoes:
            print("\n⚠️  Não foram realizadas movimentações.")
        else:
            for t in self.transacoes:
                print(f"{t['data']} - {t['tipo']}: R$ {t['valor']:.2f}")
            print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
            print("=============================")

# =========== TRANSAÇÕES ===========
class Transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass

class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        if conta.sacar(self.valor):
            conta.historico.adicionar_transacao(self)

# =========== TRANSAÇÕES ===========
def localizar_cliente(cpf, clientes):
    for cliente in clientes:
        if isinstance(cliente, PessoaFisica) and cliente.cpf == cpf:
            return cliente
    return None

def criar_usuario(clientes):
    cpf = input("Informe o CPF (somente números): ")
    cliente = localizar_cliente(cpf, clientes)

    if cliente:
        print("⚠️  CPF já cadastrado.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    cliente = PessoaFisica(nome, cpf, data_nascimento, endereco)
    clientes.append(cliente)
    print("✅ Usuário criado com sucesso.")

def criar_conta(numero, clientes, contas):
    cpf = input("Informe o CPF do usuário: ")
    cliente = localizar_cliente(cpf, clientes)

    if not cliente:
        print("❌ Usuário não encontrado.")
        return

    conta = ContaCorrente(numero=numero, cliente=cliente)
    cliente.adicionar_conta(conta)
    contas.append(conta)
    print("✅ Conta criada com sucesso.")

def listar_contas(contas):
    for conta in contas:
        cliente = conta.cliente
        print(f"Agência: {conta.agencia} | Conta: {conta.numero} | Titular: {cliente.nome}")

# ===================== MAIN =====================
def main():
    clientes = []
    contas = []

    while True:
        print("""
=================== MENU ===================
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair
""")
        opcao = input("Escolha uma opção: ")

        if opcao == "d":
            cpf = input("Informe o CPF do cliente: ")
            cliente = localizar_cliente(cpf, clientes)

            if not cliente or not cliente.contas:
                print("❌ Cliente não encontrado ou não possui conta.")
                continue

            valor = float(input("Informe o valor do depósito: "))
            transacao = Deposito(valor)
            cliente.realizar_transacao(cliente.contas[0], transacao)

        elif opcao == "s":
            cpf = input("Informe o CPF do cliente: ")
            cliente = localizar_cliente(cpf, clientes)

            if not cliente or not cliente.contas:
                print("❌ Cliente não encontrado ou não possui conta.")
                continue

            valor = float(input("Informe o valor do saque: "))
            transacao = Saque(valor)
            cliente.realizar_transacao(cliente.contas[0], transacao)

        elif opcao == "e":
            cpf = input("Informe o CPF do cliente: ")
            cliente = localizar_cliente(cpf, clientes)

            if not cliente or not cliente.contas:
                print("❌ Cliente não encontrado ou não possui conta.")
                continue

            conta = cliente.contas[0]
            print(f"\nSaldo atual: R$ {conta.saldo:.2f}")
            conta.historico.extrato(conta)

        elif opcao == "nu":
            criar_usuario(clientes)

        elif opcao == "nc":
            numero = len(contas) + 1
            criar_conta(numero, clientes, contas)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("👋 Encerrando o sistema. Até mais!")
            break

        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()