#CONTA BANCÁRIA

from datetime import datetime

class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo=0):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo
        self.transacoes = []

    def deposito(self, valor):
        if valor >= 0:
            self.saldo += valor
            self.transacoes.append((datetime.now(), "Depósito", valor))
            print("Depósito de R$", format(valor, ".2f"), "realizado com sucesso.")
        else:
            print("Valor inválido para depósito.")

    def saque(self, valor):
        if valor > 0:
            if self.saldo >= valor:
                self.saldo -= valor
                self.transacoes.append((datetime.now(), "Saque", valor))
                print("Saque de R$", format(valor, ".2f"), "realizado com sucesso.")
            else:
                print("Saldo insuficiente para saque.")
        else:
            print("Valor inválido para saque.")

    def extrato(self):
        print("Extrato bancário da conta:", self.numero_conta)
        print("Beneficiário:", self.titular)
        print("Saldo atual: R$", format(self.saldo, ".2f"))
        print("Transações:")
        for transacao in self.transacoes:
            data_hora = transacao[0].strftime("%Y-%m-%d %H:%M:%S")
            tipo = transacao[1]
            valor = transacao[2]
            print(f"{data_hora} - {tipo}: R$ {format(valor, '.2f')}")


def exibir_menu():
    print("=== Menu ===")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("0. Sair")


conta = ContaBancaria("123456789", "Lanny")

while True:
    exibir_menu()
    opcao = input("Digite o número da opção desejada: ")

    if opcao == "1":
        valor = float(input("Digite o valor do depósito: "))
        conta.deposito(valor)
    elif opcao == "2":
        valor = float(input("Digite o valor do saque: "))
        conta.saque(valor)
    elif opcao == "3":
        conta.extrato()
    elif opcao == "0":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
