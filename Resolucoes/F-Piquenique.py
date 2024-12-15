# Leitura dos valores de entrada
L, N, C = map(int, input().split())

# Inicialização de um conjunto para armazenar as vitórias-régias alcançáveis por ambos
vitorias_napinha = set()
vitorias_capinho = set()

# Calcula as posições alcançáveis para Napinha
for i in range(1, L + 1):
    if i % N == 0:
        vitorias_napinha.add(i)

# Calcula as posições alcançáveis para Capinho
for i in range(1, L + 1):
    if i % C == 0:
        vitorias_capinho.add(i)

# Interseção entre os dois conjuntos
vitorias_comuns = vitorias_napinha & vitorias_capinho

# Imprime o número de vitórias-régias em que eles podem se encontrar
print(len(vitorias_comuns))