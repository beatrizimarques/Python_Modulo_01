#Escreva um programa que leia a velocidade de um carro. 
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.

velocidade = float(input('Qual é a velocidade atual do carro? '))
multa = (velocidade - 80) * 7

if (velocidade>80):
    print('Você ultrapassou a velocidade e recebeu uma multa no valor de R${:.2F} reais'.format(multa))
else:
    print('Você está dentro do limite de velocidade!')