# Escreva um programa que leia dois números inteiros e compare-os.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1>num2:
    print('O primeiro número é maior')
elif num2>num1:
    print('O segundo número é maior')
else:
    print('Os números são iguais')