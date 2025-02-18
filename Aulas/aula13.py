'''Formatação de strings'''

nome = 'Vladimyr'
altura = 1.71
peso = 80
imc = peso / altura**2

print(nome, ' tem ', altura, 'm, e pesa ', peso, 'kg.\n', f'Seu IMC é {imc:.2f}', sep='')