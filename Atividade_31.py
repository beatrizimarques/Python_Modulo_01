#Crie um programa que faça o computador jogar Jokenpô com você

from random import randint
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

print ('Vamos jogar Jokenpô!!!')
print ('''Escolha sua jogada:
       [1] Pedra
       [2] Papel
       [3] Tesoura''')

jogador = int(input('Digite a opção desejada: '))
print ('O jogador escolheu {}'.format(itens[jogador]))
print ('O computador escolheu {}'.format(itens[computador]))

if computador == 0:
    if jogador == 0:
        print ('EMPATE')
    elif jogador == 1:
        print ('JOGADOR VENCE')
    elif jogador == 2:
        print ('COMPUTADOR VENCE')
    else:
        print('Jogada inválida')
elif computador == 1:
    if jogador == 0:
        print ('COMPUTADOR VENCE')
    elif jogador == 1:
        print ('EMPATE')
    elif jogador == 2:
        print ('JOGADOR VENCE')
    else:
        print('Jogada inválida')
elif computador == 2:
    if jogador == 0:
        print ('JOGADOR VENCE')
    elif jogador == 1:
        print ('COMPUTADOR VENCE')
    elif jogador == 2:
        print ('EMPATE')
    else:
        print('Jogada inválida')




