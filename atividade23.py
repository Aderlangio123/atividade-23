# Crie um programa que receba um número do usuário e exiba a tabuada desse número de 1 a 10.

numero = int(input("Digite um numero para ver a tabuada: "))

print(f"Tabuada do {numero}:")
for tb in range(1, 11):
    resultado = numero * tb
    print(f"{numero} x {tb} = {resultado}")
    