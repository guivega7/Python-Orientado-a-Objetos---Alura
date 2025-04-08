class Livro:
    livros = []
    def __init__(self, titulo, autor, ano_publicacao): #atributo
        self.titulo = titulo.title()
        self.autor = autor.title()
        self.ano_publicacao = ano_publicacao
        self.disponivel = True
        Livro.livros.append(self)
    
    def __str__(self): #metodo especial
        return f'{self.titulo} | {self.autor} | {self.ano_publicacao}'
    
    def emprestar(self): #metodo de instancia
        if self.disponivel:
            self.disponivel = False
            return f"O livro '{self.titulo}' foi emprestado com sucesso"
        else:
            return 'O livro está emprestado!'
        
    @staticmethod #método estatico 
    def verificar_disponibilidade(ano):
        livros_disponiveis = []
        for livro in Livro.livros:
            if livro.ano_publicacao == ano and livro.disponivel:
                livros_disponiveis.append(livro)
        return livros_disponiveis




        