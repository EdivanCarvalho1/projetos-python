class ContaBancaria:
    def __init__(self, titular, numero_conta):
        self.titular = titular
        self.numero_conta = numero_conta
        self.saldo = 0.0

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f'Depósito de R${valor:.2f} realizado com sucesso!')
        else:
            print('O valor do depósito deve ser positivo.')

    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            print(f'Saque de R${valor:.2f} realizado com sucesso!')
        else:
            print('Saldo insuficiente ou valor inválido.')

    def consultar_saldo(self):
        return self.saldo


class Banco:
    def __init__(self):
        self.contas = {}

    def criar_conta(self, titular, numero_conta):
        if numero_conta not in self.contas:
            nova_conta = ContaBancaria(titular, numero_conta)
            self.contas[numero_conta] = nova_conta
            print(f'Conta criada com sucesso para {titular}.')
        else:
            print('Número da conta já existe.')

    def encontrar_conta(self, numero_conta):
        return self.contas.get(numero_conta, None)


if __name__ == '__main__':
    banco = Banco()

    banco.criar_conta('Alice', '001')
    banco.criar_conta('Bob', '002')

    conta_alice = banco.encontrar_conta('001')
    if conta_alice:
        conta_alice.depositar(500)
        conta_alice.sacar(150)
        saldo = conta_alice.consultar_saldo()
        print(f'Saldo de Alice: R${saldo:.2f}')

    conta_bob = banco.encontrar_conta('002')
    if conta_bob:
        conta_bob.depositar(300)
        conta_bob.sacar(100)
        saldo = conta_bob.consultar_saldo()
        print(f'Saldo de Bob: R${saldo:.2f}')
