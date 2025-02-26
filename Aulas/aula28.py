'''Exercício'''

nome = input('Digite seu nome: ')
idade = input('Digite sua idade: ')

if nome and idade:
    print(f'Seu nome é {nome}, seu nome invertido é {nome[::-1]}.')
    if ' ' in nome:
        print('Seu nome possuí espaços.')
    else:
        print('Seu nome não possuí espaços.')
    print(f'A quantidade letras no seu nome é de {len(nome)} digitos.')
    print(f'A primeira letra do seu nome é um "{nome[0]}", e a ultima letra é um "{nome[-1]}".')
else:
    print('Você deixou campos em brancos!')