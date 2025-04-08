class Restaurante:
    nome = ''
    categoria = ''
    ativo = False 

restaurante_praca = Restaurante()
restaurante_praca.categoria = 'Italiana'

if restaurante_praca.ativo:
    print(('Seu restaurante está ativo!'))
else:
    print('Seu restaurante esta inativo!')

restaurante_praca.nome = 'Bistrô'

restaurante_pizza = Restaurante()

restaurante_pizza.nome = 'Pizza place'
restaurante_pizza.categoria = 'Fast Food'
restaurante_pizza.ativo = True
if restaurante_pizza.categoria == 'Fast Food':
    print('O seu restaurante é um Fast Food')
else:
    print('Seu restaurante nao é um Fast food')
print(f'Nome: {restaurante_praca.nome}, Categoria: {restaurante_praca.categoria}')

