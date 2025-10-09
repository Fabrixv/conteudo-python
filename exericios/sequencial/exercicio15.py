valor_hora = float(input("Quanto você ganha por hora? R$ "))
horas_trabalhadas = float(input("Quantas horas você trabalhou no mês? "))
salario_bruto = valor_hora * horas_trabalhadas
desconto_ir = salario_bruto * 0.11
desconto_inss = salario_bruto * 0.08
desconto_sindicato = salario_bruto * 0.05
salario_liquido = salario_bruto - (desconto_ir + desconto_inss + desconto_sindicato)
print("\n--- Detalhamento do Salário ---")
print("Salário Bruto R$:",salario_bruto)
print("Desconto IR (11%) R$",desconto_ir)
print("Desconto INSS 8% R$: ",desconto_inss)
print("Desconto Sindicato 5%: R$ ",desconto_sindicato)
print("Salário Líquido R$:" ,salario_liquido)

