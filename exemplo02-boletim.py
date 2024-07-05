import os

os.system ("cls")

print("Seja Bem Vindo ao Boletim Eletrônico")

#1 Passo - Entrada de Dados
nome = input ("Digite seu nome:  ")
p1 = float(input("Digite sua Primeira Nota:  "))
p2 = float(input("Digite sua Segunda Nota:  "))
p3 = float(input("Digite sua Terceira Nota:  "))
p4 = float(input("Digite sua Quarta Nota:  "))

# 2 Passo  - Processamento
media = (p1 + p2 + p3 + p4) / 4

#3 Passo - Saída
print ("Aluno: ", nome, " - Sua média foi:", media)

 


input("Pressione <enter> para continuar")
