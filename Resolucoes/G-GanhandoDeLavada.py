# Leitura da entrada
m = int(input())  # Número de cartas de Alberto
cartas_alberto = []
for _ in range(m):
    c, d, t = map(int, input().split())  # c: pontos de vida, d: dano, t: tipo
    cartas_alberto.append((c, d, t))

n = int(input())  # Número de cartas de Guilherme
cartas_guilherme = []
for _ in range(n):
    c, d, t = map(int, input().split())  # c: pontos de vida, d: dano, t: tipo
    cartas_guilherme.append((c, d, t))

# Função para calcular se Guilherme vence Alberto
def guilherme_ganha(cartas_alberto, cartas_guilherme):
    # Ordena as cartas de ambos os jogadores pela maior diferença de dano (d - c)
    cartas_alberto.sort(key=lambda x: x[1] - x[0], reverse=True)
    cartas_guilherme.sort(key=lambda x: x[1] - x[0], reverse=True)
    
    # Verificação se cada carta de Guilherme pode vencer a correspondente de Alberto
    for i in range(min(len(cartas_alberto), len(cartas_guilherme))):
        c_a, d_a, t_a = cartas_alberto[i]
        c_g, d_g, t_g = cartas_guilherme[i]
        
        # Calcula dano total (Guilherme vs Alberto)
        if d_g - c_a <= d_a - c_g:
            return "NAO"
    
    return "SIM"

# Verifica se Guilherme pode ganhar
resultado = guilherme_ganha(cartas_alberto, cartas_guilherme)

# Saída do resultado
print(resultado)