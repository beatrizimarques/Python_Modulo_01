# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
#à vista dinheiro/cheque: 10% de desconto
# vista no cartão: 5% de desconto
#em até 2x no cartão: preço formal 
#3x ou mais no cartão: 20% de juros


valor = float(input('Digite o valor do produto:'))
print ('''Escolha a forma de pagamento:
[1] À vista no dinheiro/cheque
[2] À vista no cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão''')

opcao = int(input('Digite a opção desejada: '))

if opcao == 1:
    total = valor - (valor * 10 / 100)
    print ('Você irá pagar o total de R${:.2f} reais'.format(total))
elif opcao == 2:
    total = valor - (valor * 5 / 100)
    print ('Você irá pagar o total de 2x de R${:.2f} reais'.format(total))
elif opcao == 3:
    total = valor / 2
    print ('Você irá pagar o total de R${:.2f} reais'.format(total))
elif opcao == 4:
    total = valor + (valor * 20 / 100)
    totalparc = int(input('Quantas parcelas? '))
    parcela = total / totalparc
    print ('Você irá pagar o total de R${:.2f} reais em {} parcelas'.format(parcela,totalparc)) 
else:
    print ('Opção inválida. Tente novamente.')