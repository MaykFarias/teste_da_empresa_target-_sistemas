"""
5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
    a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no
    código;
    b) Evite usar funções prontas, como, por exemplo, reverse;

"""

# definindo a palavra a ser invertida
palavra = str(input("Digite uma palavra: "))

# convertendo a string em uma lista de caracteres
lista_caracteres = list(palavra)

# invertendo a ordem dos caracteres
lista_caracteres_invertidos = []
for caracter in range(len(lista_caracteres) - 1, -1, -1):
    lista_caracteres_invertidos.append(lista_caracteres[caracter])

# convertendo a lista de caracteres invertidos de volta para uma string
palavra_invertida = "".join(lista_caracteres_invertidos)

# resultado
print(palavra_invertida)
