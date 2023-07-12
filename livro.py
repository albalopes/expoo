class Livro:
    def __init__(self, titulo, autor, anoPublicacao):
        self.__titulo = titulo
        self.__autor = autor
        self.__anoPublicacao = anoPublicacao
    
    def getTitulo(self):
        return self.__titulo