"""
Iterando strings com while
"""
#       012345678910
nome = input('Digite seu nome: ') # Iteráveis
#      1110987654321
tamanho_nome = len(nome)
print(nome)
print(tamanho_nome)

nova_string = ''
contador = 0

while tamanho_nome > 0:
    nova_string += '*' + nome[contador]
    contador += 1
    tamanho_nome -= 1

print(nova_string)
# nova_string += '*V*l*a*d* *G*u*e*d*e*s'