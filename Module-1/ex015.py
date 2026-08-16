carro = int(input('Quantos dias foi alugado? '))
km = float(input('Quantos km rodados? '))
valor = carro * 60 + km  * 0.15
print('O valor a pagar é de R${:.2f}'.format(valor))