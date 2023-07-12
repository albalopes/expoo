from livro import Livro

t = input("Digite o título do livro: ")
aut = input ("Digite o autor do livro: ")
ano = input("Digite o ano de publicação do livro: ")

livro1 = Livro(t, aut, ano)

print("O título do livro é: ", livro1.getTitulo())