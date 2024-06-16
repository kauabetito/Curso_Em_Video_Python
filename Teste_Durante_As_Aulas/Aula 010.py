tempo = int(input('Quantos anos tem seu carro? '))

if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')
print('-_-FIM-_-')

# ---------------------------------------------////////////////////////////////////////////////////////////-------------------------------------------------------------------------

nome = str(input('Qual o seu nome? '))

if nome == 'Kauã':
    print(f'Olá mestre {nome}')
    print(f'Você esta fraco mestre, {nome}!')
else:
    print(f'Olá Bom treino, {nome}!')

# ---------------------------------------------////////////////////////////////////////////////////////////-------------------------------------------------------------------------

n1 = int(input('Digite a primeira nota do aluno: '))
n2 = int(input('Digite a segunda nota do aluno: '))
Me = (n1 + n2) / 2

print(f'a sua media foi {Me}')

if Me <= 6.0:
    print('Você não passou!')
else:
    print('A sua nota foi boa parabens, você passou!!!')

# ---------------------------------------------////////////////////////////////////////////////////////////-------------------------------------------------------------------------
