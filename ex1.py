indice = 13
soma = 0
k = 0
while k < indice:
    k += 1
    print(f'{k:2} + {soma:2} =', end = ' ')
    soma += k
    print(soma)
print(f'Resultado final da variável soma= {soma}')
