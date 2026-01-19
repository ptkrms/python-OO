from Cliente import Cliente
from Conta import Conta

cliente1 = Cliente("123", "João", "Rua 1")
cliente2 = Cliente("456", "Maria", "Rua 2")

conta1 = Conta(numero=1, saldo=2000)
conta2 = Conta(numero=2, saldo=500)

conta1.depositar(1000)
conta1.sacar(1500)
conta1.transferir(conta2, 200)

conta1.extrato.imprimir()
conta2.extrato.imprimir()
