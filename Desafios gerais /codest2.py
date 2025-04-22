"""Crie um programa que:
Solicita dois números do usuário.
Pede para escolher uma operação: soma, subtração, multiplicação ou divisão.
Mostra o resultado."""
try :
    number1 = int(input('digite um número: '))
    number2 = int(input('digite outro número: '))

    print('Selecine qual operação será feita')
    operacao = int(input('Digite 1 : Soma; \nDigite 2 : Subtração ;\nDigite 3 : Multiplicação ; \nDigite 4 : Divisão ;\nDigite 5 : Divisão Exata.\n'))

    sm = number1 + number2
    sb = number1 - number2
    mul = number1 * number2
    div = number1 / number2
    divex = number1 % number2

    if operacao > 5 or operacao < 1 :
        print('Número inválido')
    elif  operacao == 1 :
        print(f'A soma entre os números é :{sm}')
    elif  operacao == 2 :
        print(f'A subtração entre os números é :{sb}')
    elif  operacao == 3 :
        print(f'A multiplicação entre os números é :{mul}')
    elif  operacao == 4 :
        if number2 != 0 :
            print(f'A divisão entre os números é :{div}')
        else :
            print('[ERRO] Não é possível dividir por 0')
    elif  operacao == 5 :
        if number2 != 0 :
            print(f'A divisão entre os números é :{divex}')
        else :
            print('[ERRO] Não é possível dividir por 0')
        
except: 
    print('[ERRO]Você precisa digitar um número.')