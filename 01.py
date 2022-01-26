print("olá")

# a = 10
# b = 12
a = int(input('informe o valor: '))
b = int(input('informe o valor: '))
soma = a + b
subtracao = b - a
multiplicacao = a * b
divisao = a / b
resto = a % b

print('soma: ' + str(soma))
print('subtracao: ' + str(subtracao))
print('multiplicacao: ' + str(multiplicacao))
print('divisao: ' + str(divisao))
print(resto)

print('soma: {}. subtração: {}'.format(soma, subtracao))
print('soma: {}. \nsubtração: {}'.format(soma, subtracao))

