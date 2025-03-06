'''Calculadora com While'''

print('Calculadora.')

while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador: ')
    
    numeros_validos = None
    
    try:
        num_1_float = float(numero_1)
        num_2_float = float(numero_2)
        numeros_validos = True
    except:
        numeros_validos = None
        
    if numeros_validos is None:
        print('Os números digitados não são válidos!')
        continue
    
    if len(operador) > 1:
        print('Digite apenas um operador!')
        continue
    
    elif operador not in '+/-*':
        print('Não foi digitado um operador válido!')
        continue
    
    if operador == '+':
        print(f'A soma de {numero_1} + {numero_2} = {num_1_float + num_2_float:.0f}.')
    elif operador == '-':
        print(f'A subtração de {numero_1} - {numero_2} = {num_1_float - num_2_float:.0f}.')
    elif operador == '/':
        print(f'A divisão de {numero_1} / {numero_2} = {num_1_float / num_2_float:.2f}.')
    elif operador == '*':
        print(f'A multiplicação de {numero_1} * {numero_2} = {num_1_float * num_2_float:.0f}.')
        
    #print(f'A soma de {numero_1} + {numero_2} = {int(numero_1) + int(numero_2)}.')
    
    sair = input('Você deseja sair? Digite [s]im ou [n]ão: ').lower().startswith('s')
    
    if sair is True:
        break
print('Obrigado por usar nossa calculadora.')
    