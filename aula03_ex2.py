class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def __str__(self):
        return f'{self.titular}|{self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta.ativo = True 
        return conta 
    
    @ativo.setter
    def ativo(self, valor):
        self._ativo = valor
    

    