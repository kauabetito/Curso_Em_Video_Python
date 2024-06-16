# os comandos da importação da blibioteca inteira e a importação de so alguns itens da blibioteca são diferentes segue os exemplos abaixo
# Aqui em baixo é o comando importando tuda a blibioteca (import math)
import random
import math
import emoji  # type: ignore

# Esse aqui em baixo é a importação so de alguns itens da blibioteca

from math import sqrt, floor

N1 = int(input('Digite um número: '))
Raiz = sqrt(N1)

print('A raiz de {} é igual a {}'.format(N1, floor(Raiz)))

# Aqui em baixo é o comando importando o calculo da raiz quadrada da blibioteca de matematica math (import math.sqrt)

N1 = float(input('Digite um número: '))
Raiz = math.sqrt(N1)

print('A raiz de {} é igual a {}'.format(N1, math.ceil(Raiz)))


# importação de um numero aleatorio (random)

N2 = random.random()
print(N2)

# importação de um numero aleatorio de x ate y (randint)

N3 = random.randint(1, 100)
print(N3)

# importação de uma blibioteca da comunidade essa blibioteca foi uma de emoji kkkk posso colocar qualquer emoji nos prints

print(emoji.emojize('Tudo Joia? :thumbs_up:'))
