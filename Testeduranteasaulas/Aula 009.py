# Manipulando Texto

frase = 'Curso em Vídeo Python'

# Fatiamento de estring
# o começo da de todas as estring começa com 0. quando for fatiar uma str o ultimo valor não entra na contagem.
# se colocar um terceiro numero no fatiamento ele vai fazer pulando a contagem ex: [9:14:2] ele vai ir pulando de 2 e em caracteres
# se colocar ex: [:5] ele vai do inicio ate o numero 5. e se colocar ex: [15:] vai começar do decimo quinto caractere e vai ate o final da str
# [9::3] começa no caractere 9 e vai ate ofinal da str e vai mostrando de 3 em 3

print(frase[9:14])

# Funções e operador de análise

print(len(frase))  # a função len Análisa a frase fala quantos caracteres tem nela
print(frase.count('o'))  # a função count conta quantas letras se repete na str
# Com com os numeros dps da letra sugerida a ser contada se aplica a tecnica de fatiamento
print(frase.count('o', 0, 20))
# Vai me dizer em que momento ou em qual numero de caractere do começo dele ate o fim ele encontrou a str "Python"
print(frase.find('Python'))
# se ele não encontrar uma str ou uma (palavra) ele vai retornar -1 dizendo que a palavra não foi encontrada
print(frase.find('IOS'))
# esse vai me dizer se existe a palavra curso dentro da variavel frase
print('Curso' in frase)


# Métodos de transformação

# ele ira substituir a palavra "Python" pela "IOS"
print(frase.replace('Python', 'IOS'))
print(frase.upper())  # o upper ira colocar as letras em maiusculas
print(frase.lower())  # o lower ira colocar todas as letras em minusculas
# o capitalize vai colocar todas as letras em minusculas e vai colocar so a primeira letra em maiusculas em uma str
print(frase.capitalize())
print(frase.title())  # o title funciona parecido com o capitalize mas ele não deixa so a primeira letra da str em maiuscula ele vai deixar todo começo de frase em letra maiuscula!!!
print(frase.strip())  # ira remover todos os espaços inuteis tipo quando se colocar espaços no começar da frase e no final dela, os espaços entre as frases não sera alterado
# Com o R antes do strip ele ira remover so os espaços do final da str
print(frase.rstrip())
# Com o L antes do strip ele ira remover so os espaços do começo da str
print(frase.lstrip())

# Divisão

print(frase.split())  # a onde tiver espaços ele criara uma divisão começando a outra frase contando o caractere do 0, ele irar dividir a str em uma lista cada frase ira ser separada

# Junção
print('-'.join(frase))
