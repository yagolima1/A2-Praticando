'''Faça um programa em Python que leia dois números inteiros e exiba o quadrado da diferença do primeiro valor pelo segundo. '''

num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Agora digite outro número inteiro: "))

resultado = (num1 - num2) ** 2

print(f"O quadrado da diferença entre {num1} e {num2} é {resultado}.")