import math

m = int(input('Digite um numero primo: '))
n = int(input('Digite outro numero primo: '))

maior = 0 
menor = 0

if m > n:
    maior = m
    menor = n
else:
    maior = n
    menor = m

cateto1 = 2*m*n
cateto2 = maior**2-menor**2
hipotenusa = m**2+n**2

cateto1quad = cateto1**2
cateto2quad = cateto2**2
hipotenusaquad = hipotenusa**2

print('Parabéns, você criou um triangulo retângulo de lados {} e {}, com hipotenusa {}'.format(cateto1 , cateto2, hipotenusa))
print('caso queira testar se é verdade, {} ao quadrado é {} e {} ao quadrado é {}, e a hipotenusa, {}, ao quadrado é {}'.format(cateto1 , cateto1quad , cateto2 , cateto2quad , hipotenusa, hipotenusaquad))
