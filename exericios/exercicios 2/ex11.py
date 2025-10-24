salario = float(input("Digite o salario do colaborador em reais:"))
if salario <= 1450.00:
    percentual = 20
elif salario <= 2800.00:
    percentual = 15
elif salario <= 3500.00:
    percentual = 10
valor_aumento = salario * (percentual/100)
novo_salario = salario + valor_aumento
print("REAJUSTE")
print("salari antes do reajuste", salario)
print("Percenual de aumento aplicado",percentual)
print("Valor aumento:",valor_aumento)
print("Novo salário",novo_salario)