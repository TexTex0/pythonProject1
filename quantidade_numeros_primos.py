#ESSE CONTADOR PRETENDE MOSTRAR AO USUÁRIO A QUANTIDADE DE NÚMEROS PRIMOS EXISTENTES EM UM INTERVALO DETERMINADO.
#PARA ISSO, ELE DEVE INFORMAR O NÚMERO INICIAL E FINAL DA CONTAGEM. EX.: O USUÁRIO DESEJA SABER QUAIS SÃO OS NÚMEROS PRIMOS ENTRE 1 E 20 OU ENTRE 5 E 200.

a = int(input('Digite um número para iniciar a contagem: '))
b = int(input('Agora me diga o número vocẽ quer que termine a contagem: '))
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
