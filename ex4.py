fat_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

fat_total = sum(fat_estado.values())

print(f"Faturamento total = {fat_total}")

for estado, faturamento in fat_estado.items():
    percentual = (faturamento / fat_total) * 100
    print(f"{estado} teve {percentual:.2f}% do faturamento total")
