import os

os.system ("cls")

print("Exemplo Par ou Impar")
print("-------------------------------------")

# 1 Passo - Entrada
numero = float(input("Digite um número: "))

# 2 Passo - Processamento
resto = numero % 2

print("-------------------------------------")

# 3 Passo - Saída
if resto == 0:
    print("O número digitado é ---------> *PAR* <----------")

else:
    print("O número digitado é ---------> *IMPAR* <----------")

print("-------------------------------------")
input("Pressione <ENTER> para continuar...")
print("-------------------------------------")