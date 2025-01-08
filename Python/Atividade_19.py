#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

numero = int(input('Digite um número de 0 a 9999:'))
numero2 = str(int(10000 + numero))

separa = numero2.split()
print ('A unidade do número {} é {}'.format(numero, numero2[4]))
print ('A dezena do número {} é {}'.format(numero, numero2[3]))
print ('A centena do número {} é {}'.format(numero, numero2[2]))
print ('O milhar do número {} é {}'.format(numero, numero2[1]))