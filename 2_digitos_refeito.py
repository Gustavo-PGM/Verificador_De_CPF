import sys
try:
    discagem = input("Digite seu CPF, (SOMENTE 11 NÚMEROS): ").replace('.', '').replace('-', '') #66224185352 -52 11111111111
    tirar_num1 = discagem[:9]
    multi_1 = 10

    discou_mesma_coisa = discagem == discagem[0] * len(discagem)
    print('Você digitou vários números iguais') if discou_mesma_coisa else '', sys.exit() if discou_mesma_coisa else ''

    resul = 0
    for digitos_1 in tirar_num1:
        resul += int(digitos_1) * multi_1
        multi_1 -= 1
        resto_1 = resul * 10 % 11 if multi_1 <= 1 else 0

    print(f'O valor do primeiro digito é {resto_1}' if resto_1 <= 9 else 'O valor do primeiro digito é 0')


    #SEGUNDO DIGITO

    tirar_num2 = discagem[:9] + str(resto_1)
    multi_2 = 11

    resul_2 = 0
    for digitos_2 in tirar_num2:
        resul_2 += int(digitos_2) * multi_2
        multi_2 -= 1
        resto_2 = resul_2 * 10 % 11 if multi_2 <= 1 else 0


    print(f'O valor do segundo digito é {resto_2}' if resto_2 <= 9 else 'O valor do segundo digito é 0')

    print(f'O seu CPF é válido' if resto_1 == int(discagem[-2]) and resto_2 == int(discagem[-1]) else 'O seu CPF é inválido')

except ValueError:
    print("Por favor, digite somente números inteiros")
