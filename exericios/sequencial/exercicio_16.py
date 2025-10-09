import math
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))
litros_por_metro = 1 / 3
capacidade_lata = 18
preco_lata = 80.00
litros_necessarios = area * litros_por_metro
latas_necessarias = math.ceil(litros_necessarios / capacidade_lata)
preco_total = latas_necessarias * preco_lata
print("Você precisará de", latas_necessarias ,"lata(s) de tinta.")
print("O custo total será de R$",preco_total)
