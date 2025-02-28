'''Escreva um programa em Python que permita ao usuário digitar dois números inteiros e exibir o resultado para cada uma das seguintes operações, nesta ordem: soma, subtração, multiplicação, divisão, divisão truncada, resto e exponenciação. '''

num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

soma = num1 + num2
sub = num1 - num2
mult = num1 * num2
div = num1 / num2
div_trunc = num1 // num2
resto = num1 % num2
expo = num1 ** num2

print(f"A soma dos dois números é de: {soma}")
print(f"A subtração dos dois números é de: {sub}")
print(f"A multiplicação dos dois números é de: {mult}")
print(f"A divisão dos dois números é de: {div}")
print(f"A divisão truncada dos dois números é de: {div_trunc}")
print(f"O resto dos dois números é de: {resto}")
print(f"A exponenciação dos dois números é de: {expo}")