

class Conta:
    def __init__(self, numero,titular,saldo,limite):
        print("Construindo objeto...{}".format(self))
        #acessando o arquivo que o self já sabe
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
    def extrato(self):
        print("Saldo {} do titular {} o limite é {}".format(self.saldo, self.titular, self.limite))
    def depositar(self):
        self.saldo += valor
    def saca(self, valor):
        self.saldo += valor