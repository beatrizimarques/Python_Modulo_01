dinheiro = float(input("Quanto dinheiro você tem na carteira? R$"))
dolar = dinheiro / 3.27

print("Com R${:.2f} você pode comprar US${:.2f}".format(dinheiro,dolar))