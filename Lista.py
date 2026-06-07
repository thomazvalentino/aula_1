lista_vendas = [100, 50, 200, 1000, 150]

print(lista_vendas[1]) # pegar um iten da lista 

# tamanho da lista
qtde_vendas = len(lista_vendas)
print(qtde_vendas)

# somar todos os itens 
total_vendas = sum(lista_vendas)
print(total_vendas)

# max, media, min 
print(max(lista_vendas))
print(min(lista_vendas))
print(total_vendas / qtde_vendas)

# encontrar um elemento (posicao do elemento)
lista_de_produtos = ["iphone", "ipad", "apple watch", "airpod", "macbook"]
print("airpod" in lista_de_produtos) # verificar se um elemento existe na lista

posicao = lista_de_produtos.index("airpod")
print(posicao)

pedaco_da_lista = lista_de_produtos[posicao: ]
print(pedaco_da_lista)  

# edita um item
lista_precos = [100, 50, 200, 1000, 150]
novo_preco = lista_precos[0] * 1.1
lista_precos[0] = novo_preco
print(lista_precos)


# remover um item da lista 
lista_de_produtos. remove("macbook")
print(lista_de_produtos)
# item_removoido = lista_de_produtos.pop(4)
# print(item_removoido)

# adicionar_item = "macbook"
lista_de_produtos.append("macbook")
print(lista_de_produtos)


lista2_produtos = ["monitor", "teclado", "mouse"]
# lista_de_produtos.append(lista2_produtos)
print(lista_de_produtos)

lista_de_produtos.extend(lista2_produtos)
print(lista_de_produtos)

# inserir um item em uma posicao especifica
lista_de_produtos.insert(3,"air pod max")
print(lista_de_produtos)

 # contar quantas vezes um item aparece na lista
print(lista_de_produtos.count("airpod"))


# ordenar a lista
lista_de_produtos.sort()
print(lista_de_produtos)

lista_precos. sort()
print(lista_precos)

lista_precos.sort(reverse=True)
print(lista_precos)
