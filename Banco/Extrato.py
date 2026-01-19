from datetime import datetime

class Extrato:
    def __init__(self):
        self.transacoes = []

    def registrar(self, tipo, valor):
        self.transacoes.append({
            "tipo": tipo,
            "valor": valor,
            "data": datetime.now()
        })

    def imprimir(self):
        print("\n=== EXTRATO ===")
        for t in self.transacoes:
            print(
                f"{t['tipo']:30} "
                f"R$ {t['valor']:8.2f} "
                f"{t['data'].strftime('%d/%m/%Y %H:%M')}"
            )
