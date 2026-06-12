# lista_produtos = ["airpod", "ipad" , "iphone" , "macbook"]
# precos = [2000, 9000, 6000, 11000]

dic_produtos = {"airpod": 2000, "ipad": 9000, "iphone": 6000, "macbook": 11000}

# pegar um elemento 
print(dic_produtos["iphone"])

# editar um elemento 
dic_produtos["iphone"] = dic_produtos["iphone"] * 1.3
print(dic_produtos)

#quantidade de itens 
print(len(dic_produtos))

#retirar um item do dicionario 
# dic_produtos. pop("airpod")
# print(dic_produtos)

#adicionar um item no dicionario 
dic_produtos["apple wacth"] = 2500
print(dic_produtos)

#verificar se um item existe no dicionario 
if "iphone" in dic_produtos:
    print("existe produto")
else: 
    print("não existe")

#verificar se uma chave existe 


#verificar se um valor existe nos valores do dicionario 
if 9000 in dic_produtos.values():
    print("existente")
else:
    print("não existente"
          


          