
a = int(input('Vc quer que eu comece a contar a partir de qual número? Favor digite um número: '))
b = int(input('Onde vc quer que termine a contagem? Favor digitar um número: '))
qtdNumPrimos = 0
for num in range(a,b):
    div = 0
    for x in range(1, num + 1):
        resto = num % x
        #print(x,resto)
        if resto == 0:
            div += 1


    if div == 2:
        qtdNumPrimos = qtdNumPrimos + 1
        print(num)
print('Existem {} '.format(qtdNumPrimos) + 'números primos entre {}'.format(a)+' e {}'.format(b))