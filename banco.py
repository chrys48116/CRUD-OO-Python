import contas
import pessoas

class Banco:
    def __init__(self, 
    agencias: list[int] | None = None, 
    contas: list[contas.Conta] | None = None, 
    clientes: list[pessoas.Pessoa] | None = None
    ):
        self.agencias = agencias or []
        self.contas = contas or []
        self.cliente = clientes or []
    
    def _checa_agencia(self, conta):
        if conta.agencia in self.agencias:
            return True
        return False

    def _checa_cliente(self, cliente):
        if cliente in self.cliente:
            return True
        return False

    def _checa_conta(self, conta):
        if conta in self.contas:
            return True
        return False
    
    def _checa_cliente_conta(self, cliente, conta):
        if conta is cliente.conta:
            print('_checa_se_conta_e_do_cliente', True)
            return True
        print('_checa_se_conta_e_do_cliente', False)
        return False

    def autenticar(self, cliente: pessoas.Pessoa, conta:contas.Conta):
        return self._checa_cliente(cliente) and \
        self._checa_agencia(conta) and \
        self._checa_conta(conta) and \
        self._checa_cliente_conta(cliente, conta)

    def __repr__(self):
        class_name = type(self).__name__
        attrs = f'{self.agencias},\n {self.contas}\n, {self.clientes}\n'
        return f'{class_name}, {attrs}'

if __name__ == '__main__':
    c1 = pessoas.Cliente('Luiz', 30)
    cc1 = contas.ContaCorrente(111, 222, 0, 0)
    c1.conta = cc1
    c2 = pessoas.Cliente('Maria', 18)
    cp1 = contas.ContaPoupanca(112, 223, 100)
    c2.conta = cp1
    banco = Banco()
    banco.clientes.extend([c1, c2])
    banco.contas.extend([cc1, cp1])
    banco.agencias.extend([111, 222])

    if banco.autenticar(c1, cc1):
        cc1.depositar(10)
        c1.conta.depositar(100)
        print(c1.conta)