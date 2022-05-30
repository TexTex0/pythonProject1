#ESSE CONTADOR PRETENDE MOSTRAR AO USUÁRIO A QUANTIDADE DE NÚMEROS PRIMOS EXISTENTES EM UM INTERVALO DETERMINADO.
#PARA ISSO, O USUÁRIO DEVE INFORMAR O NÚMERO INICIAL E FINAL DA CONTAGEM.

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
