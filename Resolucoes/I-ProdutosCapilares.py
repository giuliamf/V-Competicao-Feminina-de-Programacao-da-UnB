def max_maciez(N, M, V, C):
    max_maciez_total = 0
    
    # Percorre todas as subsequências possíveis de tamanho M
    for start in range(N - M + 1):
        maciez = 0
        for i in range(M):
            maciez += V[start + i] * C[i]
        max_maciez_total = max(max_maciez_total, maciez)
    
    return max_maciez_total

# Leitura do input
N, M = map(int, input().split())   # N: total de produtos, M: tamanho da rotina
V = list(map(int, input().split()))  # Valores de impacto dos produtos
C = list(map(int, input().split()))  # Coeficientes de uso

# Calcula e imprime o resultado
resultado = max_maciez(N, M, V, C)
print(resultado)