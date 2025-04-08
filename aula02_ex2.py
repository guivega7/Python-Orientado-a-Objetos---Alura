class carros:
    def __init__(self, modelo, cor, ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = int(ano)
carrro1 = carros('Ford ka','Branco','2013')

class restaurante:
    def __init__(self, nome, categoria, ativo):
        self.nome = nome
        self.categoria = categoria
        self.ativo = ativo
    def __str__(self):
        return f'{self.nome} | {self.categoria}'
Restaurante1 = restaurante('Mandu','Esfihas')
    
class clientes:
    def __init__(self, nome, vendas, meta):
        self.nome = nome
        self.vendas = vendas 
        self.meta = meta
cliente1 = clientes('Guilherme','500','1000')
    


    

