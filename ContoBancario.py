from Persona import Persona

class ContoBancario(Persona):
    def __init__(self, nome: str, cognome: str, conto):
        super().__init__(nome, cognome)
        self.conto = conto
        self.saldo = int(100)

    def getSaldo(self):
        return self.saldo

    def versa(self, versamento: int):
        self.saldo = self.saldo + versamento

    def preleva(self, prelevamento: int):
        if self.saldo < prelevamento:
            return -1
        else:
            self.saldo = self.saldo - prelevamento