# Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.

x=int(input('Digite um número: '))
for i in range(11):
    print('{}x{}='.format(x,i),i*x)