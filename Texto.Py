faturamento = 1000
custo = 600
lucro = faturamento - custo
#texto = " o lucro foi de " + str(lucro) + " e o faturamento foi de " + str(faturamento)

texto = f" o lucro foi de R${lucro} e o faturamento foi de R${faturamento} "
print(texto)

email = " EMAIL_FALSE@GMAIL.COM "

email = email.lower()
email = email.strip()

print(email)

print(len(email))

posicao = email.find("@")
print(posicao)

print(email[posicao +1:])   


novo_email = email.replace("gmail.com", "yahoo.com")
print(novo_email)


nome = "thomaz valentio"
nome = nome.capitalize()
print(nome)

nome = nome.title()
print(nome)

nome = nome.upper()
print(nome)

nome = nome.lower()
print(nome)

faturamento = 1_000_000
custo = 600
lucro = faturamento - custo
margem = lucro / faturamento 
#texto = " o lucro foi de " + str(lucro) + " e o faturamento foi de " + str(faturamento)

texto = f" o lucro foi de R${lucro:,.2f} e o faturamento foi de R${faturamento:,.2f} e a margem foi de {margem: 1.2%} "

print(texto)


# exercício

nome = " thomaz valentino "
email = "emailfalsodovalenrino@gmail.com"


# descubra o servidor de email

# descubra o 1° nome de usuário         

# criar uma mensagem personalizanda dizendo " usuário 1° nome foi cadastrado com sucesso no email tal "

email = email.strip()
email = email.lower()

print(email)

print(len (email))

posicao = email.find("@")

print (email[posicao:])

nome = nome.capitalize()
print(nome)

nome = nome.title()
print(nome)

posicao = nome.find("thomaz")
print(nome[posicao:posicao+5]  )

nome = nome.strip()
primeiro_nome = nome.split()[0]
print(primeiro_nome)

mensagem = f" usuário {primeiro_nome} foi cadastrado com sucesso no email {email}"
print(mensagem)