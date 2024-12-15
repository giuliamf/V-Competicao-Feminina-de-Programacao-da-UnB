# Leitura do número total de andares
N = int(input())

# Leitura da lista de andares em funcionamento
andares = list(map(int, input().split()))

# A soma esperada de todos os andares de 1 a N
soma_esperada = N * (N + 1) // 2

# A soma dos andares presentes na lista
soma_presente = sum(andares)

# O andar faltante é a diferença entre as somas
andar_faltante = soma_esperada - soma_presente

# Impressão do resultado
print(andar_faltante)