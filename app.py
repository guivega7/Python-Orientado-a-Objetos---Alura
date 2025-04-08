from Restaurante2 import Restaurante 

restaurante3 = Restaurante('Restaurante Kenshin','Japonês')
restaurante3.receberavaliacao('Guilherme',4)
restaurante3.receberavaliacao('Sophia',5)


def main():
    Restaurante.listarrestaurantes()
    

if __name__  == '__main__':
    main()