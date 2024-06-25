'''
maçã = 0

while maçã < 8:
    maçã += 1
    print(maçã)
print('Fim')'''

n = 1
par = impar = 0
while n != 2:
    n = int(input("Digita valor: "))
    if n % 2 == 0:
        par += 1
    else:
        impar += 1

print(f" você digitou {impar}numeros impares e {par} numeros pares")
