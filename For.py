lista_vendas = [1000, 500, 3000, 580, 699, 9300]

meta = 300

percentual_bonus = 0.1


for venda in lista_vendas:
    if venda >= meta:
        bonus = percentual_bonus * venda

    else: 
        bonus = 0 
    print(bonus)
