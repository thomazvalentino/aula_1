faturamento = input("preencha apenas com o faturamento (apenas números)")
faturamento = faturamento.replace("R$", "").replace(",", ".")
faturamento = float(faturamento)
custo = 600


lucro = faturamento - custo
print(lucro)

vendas_dia1 = float(input("vendas dia 1:"))
vendas_dia2 = float(input("vendas dia 2:"))
print(vendas_dia1 + vendas_dia2)

