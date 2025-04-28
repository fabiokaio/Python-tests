# # Peça 4 notas, armazene numa lista e calcule a média.

# print('Vamos saber se você está aprovado ou reprovado!')
# notas = []
# for i in range(4) :
#     while True :
#         try :
#             nota = float(input(f'Digite sua nota{i+1} de 0 a 10: '))
#             if nota >= 0 and nota <= 10 :
#                 notas.append(nota)
#                 break
#             else :
#                 print('[ERRO] Valor inserido não é válido.')
#         except ValueError :
#              print('[ERRO]Você deve digitar apenas números nos campos sugeridos.')

# media = sum(notas) / len(notas)
# if media < 6 :
#     print(f'Acho que reprovamos ... sua média foi {media :.2f}')
# elif media == 6 :
#     print(f'Essa foi por pouco !! Sua média foi 6!')
# else :
#     print(f'Parabénsss !!! Sua média foi {media:.2f}')

print('Vamos saber se você está aprovado ou reprovado!')

notas = []

for i in range(4):
    while True:
        try:
            nota = float(input(f'Digite sua nota {i+1} de 0 a 10: '))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print('[ERRO] Valor inserido não é válido. Digite uma nota entre 0 e 10.')
        except ValueError:
            print('[ERRO] Você deve digitar apenas números nos campos sugeridos.')

media = sum(notas) / len(notas)

if media < 6:
    print(f'Acho que reprovamos... Sua média foi {media:.2f}')
elif media == 6:
    print(f'Essa foi por pouco! Sua média foi 6!')
else:
    print(f'Parabénsss!!! Sua média foi {media:.2f}')
