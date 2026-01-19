class Extrato:
    def __init__(self):
        self.transacoes = [] #lista das transações da conta

    def extrato(self, numeroConta):
        print(f"Extrato: {numeroConta}\n")
        for transacao in self.transacoes:
            print(f"{transacao[0]:15s} {transacao[1]:10.2f} {transacao[2]:10s} {transacao[3].strftime('%d/%m/%Y')}")