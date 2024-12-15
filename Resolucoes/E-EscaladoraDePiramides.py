# Leitura do tamanho da base
N = int(input())

# Leitura das dificuldades das pedras na base
dificuldades = list(map(int, input().split()))

# Construção da pirâmide até o topo
while len(dificuldades) > 1:
    nova_camada = [dificuldades[i] + dificuldades[i + 1] for i in range(len(dificuldades) - 1)]
    dificuldades = nova_camada

# A maior dificuldade da pedra no topo
print(dificuldades[0])