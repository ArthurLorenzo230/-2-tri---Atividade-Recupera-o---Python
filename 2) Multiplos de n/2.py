

numero = int(input("Digite um número inteiro: "))

print(f"\nMúltiplos de 3 de 1 até {numero}:")

for i in range(1, numero + 1):
    if i % 3 == 0:
        print(i)
