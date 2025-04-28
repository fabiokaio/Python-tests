
''' Peça uma palavra e mostre ela ao contrário.
    Exemplo: “python” → “nohtyp”
'''
print('Vamos colocar palavras de trás para frente.\n(Não sei porque alguém faria isso , mas...)')
palavra = input('Digite uma palavra :')
ao_contrario = palavra[::-1]
print(f'A palavra {palavra} fica assim ao contrário: {ao_contrario}' )