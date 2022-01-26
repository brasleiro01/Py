# comparação ente números
# a = int(input('Primeiro valor: '))
# b = int(input('Segundo valor: '))
# c = int(input('Terceiro valor: '))
#
# if a > b and a > c:
#     print('o maior número é {}'.format(a))
# elif b > a and b > c:
#     print('o maior número é: '.format(b))
# else:
#     print('o maior número é: '.format(c))
# print('final do programa')

# verificar se o número é par
# a = int(input('Informe o número: '))
# resto = a % 2
#
# if resto == 0:
#     print('o número é par')
# else:
#     print('o número é impar')
# print('fim')

#verificar se foi informado um númeor par
# a = int(input('Informe o primeiro número: '))
# b = int(input('Informe o segundo número: '))
# resto_a = a % 2
# resto_b = b % 2
# if resto_a == 0 or resto_b == 0:
#     print('foi digitado um númeor par')
# else:
#     print('nenhum numero par foi digitado')
# print('fim')

#média aritimetica
# a = int(input('Informe o primeira nota: '))
# b = int(input('Informe o segunda nota: '))
# c = int(input('Informe o terceira nota: '))
#
# media = (a + b + c) / 4
#
# if a <= 10 and b <= 10 and c <= 10:
#     print('média: {}'.format(media))
# else:
#     print('foi informado um valor fora do padrão')

a = int(input('Informe o primeira nota: '))
if a > 10:
    a = int(input('nota errada. Informe a nota correta: '))
b = int(input('Informe o segunda nota: '))
if b > 10:
    b = int(input('nota errada. Informe a nota correta: '))
c = int(input('Informe o terceira nota: '))
if c > 10:
    c = int(input('nota errada. Informe a nota correta: '))

media = (a + b + c) / 4
print('média: {}'.format(media))