import contas

class Pessoa:
    def __init__(self, nome: str, idade: int):
        self._nome = nome
        self._idade = idade

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome:str):
        self._nome = nome
    
    @property
    def idade(self):
        return self._idade
    
    @idade.setter
    def idade(self, idade:int):
        self._idade = idade
    
    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.nome},\n {self.idade}\n'
        return f'{class_name}, {attrs}'

class Cliente(Pessoa):
    def __init__(self, nome: str, idade: int):
        super().__init__(nome, idade)
        self.conta: contas.Conta | None = None

    
if __name__ == '__main__':
    c1 = Cliente('chrys', 20)
    c1.conta = contas.ContaCorrente(111, 222, 0, 0)
    print(c1)
    print(c1.conta)