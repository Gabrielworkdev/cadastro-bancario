

class Conta:
    def __init__(self, numero,titular,saldo,limite):
        print("Construindo objeto...{}".format(self))
        #acessando o arquivo que o self já sabe
        self.numero = 123
        self.titular = "Gabriel"
        self.saldo = 1000