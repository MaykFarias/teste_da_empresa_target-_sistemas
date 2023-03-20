"""
    2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE:
Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no
código;

"""

indici = 13
soma = 0
k = 0

while k < indici:
    k = k + 1
    soma = soma + k


print(soma)


fibonacci = [0, 1]
primeiro = 0
segundo = 0

numero = int(input("Digite um número: "))

for i in range(numero):
    terceiro = primeiro + segundo
    fibonacci.append(terceiro)
    primeiro = segundo
    segundo = terceiro

if numero in fibonacci:
    print(f"O número {numero} está na sequência de Fibonacci!")

else:
    print(f"O número {numero} não está na sequência de Fibonacci!")
