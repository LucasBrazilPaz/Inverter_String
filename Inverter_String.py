# Definindo uma string
string = "Ola mundo!"

# Inicializando a string invertida
string_invertida = ""

# Invertendo os caracteres da string
for i in range(len(string)-1, -1, -1):
    string_invertida += string[i]

# Imprimindo a string invertida
print("A string original é:", string)
print("A string invertida é:", string_invertida)
