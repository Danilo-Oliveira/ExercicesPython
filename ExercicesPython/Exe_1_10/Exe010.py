# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

din = float(input('Quanto você tem na carteira:R$'))
print(f'Com R${din:.2f} você pode comprar US${din / 5.42:.2f}')