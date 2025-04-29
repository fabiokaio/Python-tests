'''
Calculando a média ponderada e evoluindo o script anterior para o nível 2 !
'''
print('Vamos calcular uma média ponderada !')

notas = []
pesos = []
quantidade_notas = 4

for contador in range (quantidade_notas) :
    while True :
        try :
            nota = float(input(f'Digite sua {contador+1}ª nota de 0 a 10: '))
            if 0 <= nota <= 10 :
                notas.append(nota)
                break
            else:
                print('[ERRO] Insira um valor entre 0 e 10')
        except ValueError:
            print('[ERRO]Digite um número válido')

for contador in range (quantidade_notas) :
    while True:
        try:
            peso = float(input(f'Digite o {contador+1}º peso de nota: '))
            if peso > 0 :
                pesos.append(peso)
                break
            else :
             print('[ERRO] Digite um valor maior que 0')
        except: 
            print('[ERRO] Insira um valor válido')

soma_ponderada = 0
soma_peso = 0

for contador in range(quantidade_notas):
    soma_ponderada +=  notas[contador] * pesos[contador]
    soma_peso += pesos[contador]

media_ponderada = soma_ponderada / soma_peso

if media_ponderada < 6 :
    print(f'Infelizmente você foi reprovado:\nSua média foi {media_ponderada:.2f} ')
elif media_ponderada == 6:
    print('Essa foi por pouco , sua média foi 6')
else:
    print(f'Parabéns você foi aprovado :\nSua média foi : {media_ponderada:.2f}')