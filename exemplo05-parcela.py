import os

os.system ("cls")

print("Loja Xing Ling - Parcelamento")
print("-----------------------------")

# 1 Passo
valor_compra = float(input ("Digite o valor da compra: "))
valor_parcelas = int(input("Digite em quantas vezes: "))

# 2 Passo - Processamento
resultado = valor_compra / valor_parcelas

# 3 Passo - Resultado
#print("O valor de cada parcela: R$ ", resultado)
print (f"O total de reais será R$  {resultado:2f}")
input("Pressione <ENTER> para continuar...")
