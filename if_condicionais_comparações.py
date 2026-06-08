fatumento = 1000
custo = 600
lucro = fatumento - custo

# if lucro > 0:
    # o que eu quero que aconteça se a condição for verdadeira
# else:
    # o que eu quero que aconteça se a condição for falsa

if lucro >= 0: 
        print("lucro de" , lucro )
        print("deu lucro")
else:
        print("prejuizo de" , lucro)
        print("deu prejuizo")


        # exemplo

    # produtos = ["iphone", "ipad", "airpod",]
    # novo_produto = input("digite o nome do produto")

    # if novo_produto in produtos:
    #     print ("produto já existente")
    # else: 
    #     print (f"{novo_produto} cadastrado com sucesso")
    #     produtos.append(novo_produto)
    #     print(produtos)


 # exemplo 2
 # bonus dos funcionarios
 # vendas maiores do que 15000, então ele ganha 500 de bonus
 # se as vendas forem ente 5000 e 15000, então ele ganha 100 de bonus
# se as vendas forem menores do que 5000, então ele não ganha bonus


# vendas = 11000

# if vendas >= 15000:
#       bonus = 500
# else:
#     if vendas >= 5000:
#           bonus = 100 
#     else: 
#           bonus = 0 

# print(f"bonus do funcionario é de {bonus} reis")

# if vendas >= 15000:
#       bonus = 500
# elif vendas >= 5000:
#     bonus = 100
# else:
#       bonus = 0

# print(f"bonus do funcionario é de {bonus} reis")



# exemplo 3 
# bonus dos funcionários 
# vendas maiores do que 15000, então ele ganha 500 de bonus 
# se as vendas forem entre 5000 e 15000 então ele ganha 100 de bonus 
# se as vendas forem menores do que 5000 então ele não ganha bonus 
# só ganha bonus se as vendas totais da empresa forem maiores do que 10000

vendas_empresa = 200_00
metas_empresa = 100_000
vendas_funcionarios = 110

if vendas_funcionarios >= 15000 and  vendas_empresa >= metas_empresa:
        bonus = 500
elif vendas_funcionarios >= 5000 and vendas_empresa + metas_empresa:
        bonus = 100
else:
        bonus = 0 

print(f"bonus do funcionário: {bonus}")
