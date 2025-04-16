from datetime import datetime

# Dados pessais e data atual
nome = input('Qual o seu nome ?')
nascimento = int(input('Em que ano você nasceu?'))
hoje = datetime.today()
# Para calculo de IMC
peso =float(input('Quanto você pesa?'))
height = float(input('Qual a sua altura ?'))
# Para o ajuste salarial
sal_atual= float(input('Quanto você recebe?'))
sal_desejado=float(input('Qual salário que quer receber?'))
# Calculo simples
numb1=int(input('Agora digite um número:'))
numb2=int(input('Digite outro número:'))

idade = hoje.year - nascimento
print('Olá {}! Sua idade é {} , nascido em {}' .format(nome,idade,nascimento))

imc = peso / height**2

if imc < 18.5:
    print("Cuidado: Abaixo do peso")
elif 18.5 <= imc < 25:
    print("Tudo Bem: Peso normal")
elif 25 <= imc < 30:
    print("Cuidado: Sobrepeso")
elif 30 <= imc < 35:
    print("Alerta: Obesidade grau I")
elif 35 <= imc < 40:
    print("Urgente: Obesidade grau II")
else:
    print("Procure um médico imediatamente: Obesidade grau III (mórbida)")

ajuste = sal_desejado - sal_atual
porcent = (ajuste / sal_atual)*100
print('O aumento percentual é de {}% , e a diferença de salário  é de {} reais.'.format(porcent , ajuste))

soma = numb1 + numb2 
subt = numb1 - numb2
div  = numb1 / numb2
div_ex = numb1 % numb2
mult = numb1 * numb2

print('O resultado da soma entre esses dois números é :{} , a subtração é :{} , a divisão é :{}, o resto da divisão é :{}, e sua multiplicação:{}'.format(soma,subt,div,div_ex,mult))