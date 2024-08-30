def is_Fibonacci(n):
    valor_1, valor_2, soma = 0, 1, 0
    while True:
        soma = valor_1 + valor_2
        valor_1 = valor_2
        valor_2 = soma
        if soma > n:
            return f'{n} não pertence a Fibonacci'
        elif soma == n:
            return f'{n} pertence a Fibonacci'

        
n = int(input('Qual número você quer saber se prentence a Fibonacci? '))
print(is_Fibonacci(n))




