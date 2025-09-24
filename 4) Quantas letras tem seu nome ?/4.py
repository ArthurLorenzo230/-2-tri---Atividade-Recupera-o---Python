# colocar teu nome em uma variável
nome = "Arthur Lorenzo Pessoa Fernandes"

# Contador de letras
contador = 0

for letra in nome:
    if letra.isalpha():   # Verifica se o coiso é uma letra
        contador += 1

print(f"O nome '{nome}' tem {contador} letras.")
