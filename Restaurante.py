from avaliação import Avaliacao


#classe
class Restaurante:
    restaurantes = []
    #Serve para definir o objeto de cada restaurante
    def __init__(self, nome , categoria): #Metodo
        self.nome = nome.title() #o title deixa a primeira letra maiscula 
        self.categoria = categoria.upper()
        self._ativo = False #o _ indica que é protegido
        self._avaliacao = []
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
    
    @classmethod #Funcoes que executam ação
    def listarrestaurantes(cls):
        print(f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação' .ljust(25)} | {'Status'}")
        for restaurante in cls.restaurantes:
            print(f'{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {str(restaurante.mediaavaliacoes).ljust(25)} | {restaurante.ativo}')


    @property #muda como o atributo vai ser lido
    def ativo(self):
        return 'verdadeiro' if self._ativo else 'falso'

    def alternarestado(self):
        self._ativo = not self._ativo

    def receberavaliacao(self, cliente, nota):
        if 0 < nota <= 5:
            avaliacao = Avaliacao(cliente, nota)
            self._avaliacao.append(avaliacao)
        

    @property
    def mediaavaliacoes(self):
        if not self._avaliacao:
            return '-'
        somadasnotas = sum(avaliacao._nota for avaliacao in self._avaliacao) #pega todas as avaliações e pra cada avaliação eu quero somente a nota 
        quantnotas = len(self._avaliacao)
        media = round(somadasnotas / quantnotas,1) #round serve para arredondar a divisao
        return media
    
        

