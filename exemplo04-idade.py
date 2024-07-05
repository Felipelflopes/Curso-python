import os

os.system ("cls")


print("Descobrindo sua idade!!!")
print("--------------------------")

# 1 Passo
anoatual = int(input ("Digite o ano atual: "))
anonascimento = int(input("Digite o ano de nascimento: "))

# 2 Passo - Processamento
resultado = anoatual - anonascimento

# 3 Passo - Resultado
print("O sua idade é de: ", resultado, "anos")

input("Pressione <ENTER> para continuar...")
