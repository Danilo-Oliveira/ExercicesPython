# Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.

x = int(input("Digite um número: "))
ant = x - 1
suc = x + 1
print(f"O antecessor de {x} é : {ant}")
print(f"O sucessor   de {x} é : {suc}")