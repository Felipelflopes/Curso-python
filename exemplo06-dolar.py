import os

os.system ("cls")

print("Cotação Dolar")
print("--------------")

# 1 Passo - Entrada
valor_troca = float(input ("Digite o valor que deseja converter em dolar: R$ "))
valor_cotação = float(input("Digite a cotação do dolar: $ "))

# 2 Passo - Processamento
resultado = (valor_troca) * (valor_cotação)

# 3 Passo - Resultado
#print("O valor em reais é de: R$ ", resultado)
print (f"O total de reais será R$  {resultado:2f}")
input("Pressione <ENTER> para continuar...")