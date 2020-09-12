class Fila:
    def __init__(self):
        self.dado = []

    def entrar(self, valor):
        self.dado.append(valor)

    # caso eu queira saber se um objeto é iterável eu preciso
    # ter um um método getitem
    def __getitem__(self, pos: int):
        return self.dado[pos]

    """caso queira criar uma representação do objeto, você precisa criar
    um método __repr__
    Esse método repr é mais ou menos como vocẽ quer printar o seu objeto
    caso você não faça um repr, você não consegue printar o objeto,
    quando você mandar printar, ele vai retornar um bocado de número e letras
    que é uma representação padrão de um objeto qualquer.
    As vezes é importante fazer uma representação para passar nos testes.
    Você vai perceber que algumas vezes o unitest vai pedir para você criar
    uma representação. 
    """

    def __rept__(self):
        return f'{self.dado}'
