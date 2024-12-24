dias = int(input('Quantos dias você alugou o carro?'))
km = float(input('Quantos km você rodou com o carro?'))
pago = (60*dias) + (0.15*km)

print('O total a pagar é de R${:.2f}'.format(pago))