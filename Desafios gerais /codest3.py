''' Desafio: Par ou Ímpar
    Peça um número ao usuário e diga se ele é par ou ímpar.
'''
try:
    num = int(input('Digite um número aleatório:\n'))
    if num % 2 == 0:
        print('É par, pois o resto da divisão por 2 é 0.')
    else:
        print('É ímpar, pois o resto da divisão por 2 não é 0.')
except ValueError:
    print('[ERRO] Você precisa digitar um número inteiro.')
