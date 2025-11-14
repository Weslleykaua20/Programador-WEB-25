
"""
class Pessoa():
    def __init__(self, nome: str, idade: int):
        # "Self" Refere-se a própria instância, salvando os dados como atributos.
        self.name = nome
        self.idade = idade

    def apresentar(self):
        # Um método simples que usa atributos da instância.
        print(f"Olá, meu nome é {self.nome} e tenho {self.idade} anos.")

    p = Pessoa("manoel", 30)
    p.apresentar()
"""

class Livro():
    def __init__(self, titulo, autor, preco):
        self.titulo = titulo
        self.autor = autor 
        self.preco = preco

    def info(self):
        print(" Digite as informações a baixo do livro a ser cadastrado. ")
        print(f"Titulo: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Preço: {self.preco:.2f}")
        
       
    Livro.info()