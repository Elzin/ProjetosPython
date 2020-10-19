chamador = ''
pergunta_grau = int(input('Digite o valor a ser convertido: '))

#Abaixo vou perguntar ao usuário qual a sua escala

print('[1] Celsius')
print('[2] Fahrenheit')
print('[3] Kelvin')
pergunta_escala = int(input('Em que escala o valor digitado está?: '))

#Abaixo vou perguntar em qual escala deve ser convertida
while True:
    if pergunta_escala == 1 :
        print('[2] Fahrenheit')
        print('[3] Kelvin')
        break

    elif pergunta_escala == 2:
        print('[1] Celsius')
        print('[3] Kelvin')
        break
    elif pergunta_escala == 3:
        print('[1] Celsius')
        print('[2] Fahrenheit')
        break
    else:
        print('Você digitou um númer inválido, tente novamente')
        pergunta_escala = int(input('Em que escala o valor digitado está?: '))

pergunta_conversão = int(input('Digite o número correspondente a escala a ser convertido: '))

#Conversão de celsius em Fahrenheit
if pergunta_escala == 1 and pergunta_conversão == 2:
    r = (pergunta_grau * 9/5) + 32
    chamador = 'Celsius'
#Conversão de celsius em kelvin
if pergunta_escala == 1 and pergunta_conversão == 3:
    r = pergunta_grau + 273
    chamador = 'Celsius'
#Fahrenheit em celcius
if pergunta_escala == 2 and pergunta_conversão == 1:
    r = (pergunta_grau - 32) * 5/9
    chamador = 'Fahrenheit'
#Fahrenheit em kelvin
if pergunta_escala == 2 and pergunta_conversão == 3:
    r = ((pergunta_grau - 32) * 5/9 + 273.15)
    chamador = 'Fahrenheit'
#Kelvin para celsius
if pergunta_escala == 3 and pergunta_conversão == 1:
    r = pergunta_grau - 273.15
    chamador = 'Kelvin'
#Kelvin para Fahrenheit
if pergunta_escala == 3 and pergunta_conversão == 2:
    r = (pergunta_grau - 273.15) * 9/5 + 32
    chamador = 'Kelvin'

print(f'O valor é {r} {chamador}')







