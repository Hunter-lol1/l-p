numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print('O número é par!')
else:
    print('O número é impar!')

====================================================================================================

idade = int(input('Digite sua idade: '))

if idade <= 12:
    print('Você é criança!')
elif idade < 18:
    print('Você é adolescente!')
if idade <= 24:
    print('Já pode ir preso em!')
if idade <= 25:
    print('Ser adulto é triste né? se fodeu!')
if idade <= 100:
    print('Ta velho em, MORRA, MORRA, MORRA, MORRA')

====================================================================================================

usuario_correto = 'canabis'
senha_correta = '123'

usuario = input('Digite seu nome de usúario: ')
senha = input('Digite sua senha: ')

if usuario == usuario_correto and senha == senha_correta:
    print('Login correto, bem vindo!')
else:
    print('Login incorreto, tente novamente!')
