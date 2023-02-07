import os
import abc

cls = os.system('cls')
class Conta(abc.ABC):
    def __init__(self, agencia, conta, saldo=0):
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        
    @abc.abstractclassmethod
    def sacar(self, valor):
        ...

    def depositar(self, valor):
        self.saldo += valor
        self.detalhes(f'DEPOSITO: R${valor:.2f}')     

    def detalhes(self, msg):
        print(f'O seu saldo é R${self.saldo:.2f} {msg}')
        print('----------------------------------------')

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia},\n {self.conta}\n, {self.saldo}\n'
        return f'{class_name}, {attrs}'

class ContaPoupanca(Conta):
    def sacar(self, valor):
        valor_saque = self.saldo - valor

        if valor_saque >= 0:
            self.saldo -= valor
            self.detalhes(f'SAQUE:{valor} ')
            return self.saldo
        print('Não foi possivel sacar o valor desejado')
        self.detalhes(f'SAQUE NEGADO R${valor:.2f}')

class ContaCorrente(Conta):
    def __init__(self, agencia, conta, saldo=0, limite=0):
        super().__init__(agencia, conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        valor_saque = self.saldo - valor
        limite_maximo = -self.limite

        if valor_saque >= limite_maximo:
            self.saldo -= valor
            self.detalhes(f'SAQUE:{valor} ')
            return self.saldo

        print('Não foi possivel sacar o valor desejado. Saque acima do limite.')
        self.detalhes(f'SAQUE NEGADO R${valor:.2f}')
        
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencia},\n {self.conta}\n, {self.saldo}\n, {self.limite}\n'
        return f'{class_name}, {attrs}'


if __name__ == '__main__':
    cp1 = ContaPoupanca(111, 222, 0)
    cp1.depositar(1)
    cp1.sacar(1)
    print('##')
    cc1 = ContaCorrente(111, 222, 0, 1)
    cc1.depositar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar(1)
    cc1.sacar('123')