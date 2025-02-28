'''Faça um programa em Python que resolva o seguinte problema: 

Um concurso possui um prêmio no montante de R$ 780.000,00 para dividir entre três ganhadores da seguinte forma: 

- o primeiro ganhador receberá 46% do prêmio; 

- o segundo ganhador receberá 32% do prêmio; 

- o terceiro ganhador receberá o restante do prêmio. 

Calcule e mostre o valor do prêmio de cada ganhador, nesta ordem: primeiro colocado, segundo colocado e terceiro colocado.

Observe que este programa não tem valor de entrada feita pelo usuário. '''

p_g1 = int(780000 * 0.46)
p_g2 = int(780000 * 0.32)
p_g3 = int(780000 - (p_g1 + p_g2))

print(f"O prêmio do 1° colocado foi de: R${p_g1}")
print(f"O prêmio do 2° colocado foi de: R${p_g2}")
print(f"E o prêmio do 3° colocado foi de: R${p_g3}")