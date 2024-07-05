import os

os.system ("cls")

print("Exemplo extrutura Condicional Simples")
print("-------------------------------------")

#1 Passo - Entrada
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a Segunda nota: "))
nota3 = float(input("Digite a Terceira nota: "))
nota4 = float(input("Digite a Quarta nota: "))

#2 Passo - Processamento
media = (nota1 + nota2 + nota3 + nota4) / 4


#3 Passo - Saída
print("-------------------------------------")
print ("Sua média foi: ", media)
print("-------------------------------------")

if media >= 6:
    print("PARABENS!!! Você foi *APROVADO!*")

elif media >=4 and media <=5:
    print("Você ficou de *RECUPERAÇÃO*")

else:
    print("OPS, Você foi *REPROVADO*")

print("-------------------------------------")

input("Pressione <Enter> para Continuar")