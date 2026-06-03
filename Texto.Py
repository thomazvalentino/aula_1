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

posicao = email.find("e")
print(posicao)