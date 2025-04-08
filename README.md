# 🍽️ Restaurante App

Projeto desenvolvido durante o curso da Alura, com foco em orientação a objetos em Python. O app simula o gerenciamento de restaurantes e avaliações feitas por clientes.

## 🧠 Conceitos aplicados

- Classes e objetos
- Encapsulamento (`_propriedades`)
- Métodos de classe (`@classmethod`)
- Propriedades com `@property`
- Listas e iteração
- Validação de entrada

## 📁 Estrutura dos arquivos

```
restaurante-app/
├── app.py                 # Script principal que roda o programa
├── restaurante.py         # Define a classe Restaurante
├── avaliacao.py           # Define a classe Avaliacao
├── exercicios/            # (Opcional) Exercícios feitos durante o curso
└── README.md              # Este arquivo
```

## 🚀 Como executar

1. Certifique-se de que tem o Python 3 instalado.
2. Clone ou baixe o repositório.
3. No terminal, execute:

```bash
python app.py
```

Você verá a listagem dos restaurantes cadastrados e suas avaliações.

## ✍️ Exemplo de uso

```python
restaurante = Restaurante("Pizzaria Alura", "Italiana")
restaurante.alternar_estado()
restaurante.receber_avaliacao("João", 5)
restaurante.receber_avaliacao("Maria", 4)

Restaurante.listar_restaurantes()
```

---

## 📚 Créditos

Projeto feito com base no curso da [Alura](https://www.alura.com.br/) sobre Python e orientação a objetos.
