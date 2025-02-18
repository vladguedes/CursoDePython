'''Exercício de comparação'''


valor_1 = input("Digite um valor: ")
valor_2 = input("Digite outro valor: ")

if valor_1 > valor_2:
    print(f'O primeiro valor ({valor_1}) é maior que o segundo valor ({valor_2}).')
elif valor_2 > valor_1:
    print(f'O segundo valor ({valor_2}) é maior que o primeiro valor ({valor_1}).')
else:
    print('Os dois valores são iguais.')

    