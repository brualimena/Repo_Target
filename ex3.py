dados = [
    {'dia': 1, 'faturamento': 1000},
    {'dia': 2, 'faturamento': 1900},
    {'dia': 3, 'faturamento': 2000},
    {'dia': 4, 'faturamento': 0},
    {'dia': 5, 'faturamento': 2600}
]

faturamentos = [dia['faturamento'] for dia in dados if dia['faturamento'] > 0]

menor_fat = min(faturamentos)
maior_fat = max(faturamentos)

media_mensal = sum(faturamentos) / len(faturamentos)

dias_acima_da_media = sum(1 for faturamento in faturamentos if faturamento > media_mensal)

print(f'Menor valor de faturamento: {menor_fat}')
print(f'Maior valor de faturamento: {maior_fat}')
print(f'Dias com faturamento acima da média: {dias_acima_da_media}')
