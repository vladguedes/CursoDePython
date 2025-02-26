"""
Interpolação básica de strings
s - string
d e i - int
f - float
x (minúsculo) e X (maiúsculo) - Hexadecimal (ABCDEF0123456789)
"""
nome = 'Vlad'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %i é %2x' % (15, 15))