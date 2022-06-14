# Vamos pedir o valor original do produto
valor_original = float( input("Valor original: R$ ") )

# Desconto ganho de 5%
valor_descontado = valor_original * 0.05

# Parcela em 2 vezes
nova_parcela = valor_original / 2

# Parcela em 3 vezes com 5% de juros
novo_valorparcelado = valor_original * 3 * 0.05

# Exibindo tudo
print('Valor original:     R$', valor_original)
print('Parcelado em duas vezes:    R$', nova_parcela)
print('Parcelado em 3 vezes com 5 por cento de juros:  R$', novo_valorparcelado)
print('Desconto ganho:     R$', valor_descontado)

