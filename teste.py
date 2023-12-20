#funcao criar conta

def criar_conta(numero,titular,saldo,limite):
    conta = {"Numero":numero, "titular": titular, "saldo":saldo, "limite":limite}
    #retornar informações da conta
    return conta
def deposita(conta, valor):
    conta["saldo"]+= valor
def saca(conta,valor):
    conta["saldo"]-= valor
def extrato(conta):
    print("Saldo é {}".format(conta["saldo"]))