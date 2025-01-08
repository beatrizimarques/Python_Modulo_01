#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome:')).strip()
print ('O seu nome com as letras maiúscula fica: {}'.format(nome.upper()))
print ('Oseu nome em minúsculo fica: {}'.format(nome.lower()))
print ('O seu nome tem {} letras'.format(len (nome)-nome.count(' ')))
separa = nome.split()
print ('Seu primeiro nome tem {} letras'.format(len(separa[0])))