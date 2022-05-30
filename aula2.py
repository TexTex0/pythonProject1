a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

resultado = 'Soma: {soma}. \nSubtração: {sub}. ''\nMultipicação: {mult}. ''\nDivisão: {div}. ' '\nResto: {rest} ' .format(soma=soma,
                                                   sub=subtracao,
                                                   mult=multiplicacao,
                                                   div=divisao,
                                                 rest=resto)
print(resultado)

         # x = '1'
         #    soma2 = (x) + 1
         #    print(format(soma2))