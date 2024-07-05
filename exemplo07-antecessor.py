import os

os.system ("cls")


print("Descobrindo o Antecessor e Sucessor")
print("-----------------------------------")

# 1 Passo - Entrada
número_digitado = int(input ("Digite um número: "))

# 2 Passo - Processamento
antecessor = número_digitado - 1
sucessor = número_digitado + 1

# 3 Passo - Resultado
print("---------------------")
print("O Número Digitado: ", número_digitado)
print("Antecessor: ", antecessor)
print("Sucessor: ", sucessor)


input("Pressione <ENTER> para continuar...")