from persona import Persona

class ContoBancario(Persona):
    def __init__(self, nome: str, cognome: str, conto):
        super().__init__(nome, cognome)
        self.conto = conto
        self.saldo = int(0)

    def getSaldo(self):
        return self.saldo

    def versa(self):
        