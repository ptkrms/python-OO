from Extrato import Extrato

class Conta:
    def __init__(self, numero, saldo=0):
        self.numero = numero
        self.saldo = saldo
        self.extrato = Extrato()

    def depositar(self, valor):
        if valor <= 0:
            return False
        self.saldo += valor
        self.extrato.registrar("DEPÓSITO", valor)
        return True

    def sacar(self, valor):
        if valor <= 0 or valor > self.saldo:
            return False

        self.saldo -= valor
        self.extrato.registrar("SAQUE", valor)
        return True

    def transferir(self, conta_destino, valor):
        if valor <= 0 or valor > self.saldo:
            return False

        self.saldo -= valor
        conta_destino.saldo += valor

        self.extrato.registrar(
            f"TRANSFERÊNCIA PARA CONTA {conta_destino.numero}",
        valor
    )
        conta_destino.extrato.registrar(
            f"TRANSFERÊNCIA DE CONTA {self.numero}",
        valor
    )
            
        return True