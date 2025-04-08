class pessoa:
    def __init__(self,nome, idade, profissão):
        self.nome = nome
        self.idade = idade
        self.profissão = profissão

    def __str__(self):
        return f'{self.nome}|{self.idade}|{self.profissão}'
    
    def saudação(self):
        if self.profissão:
            return f'Olá, sou {self.nome}! Trabalho com {self.profissão}'
        else:
            return f'Olá, sou {self.nome}!'
            
    
    def aniversario(self):
        self.idade += 1 