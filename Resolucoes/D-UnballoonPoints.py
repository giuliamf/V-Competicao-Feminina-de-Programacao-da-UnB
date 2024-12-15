# Leitura do input
n = int(input())  # Tamanho da palavra
s = input()       # Palavra fornecida

# Define as letras da palavra "unballoon"
target = "unballoon"

# Cálculo dos "Unballoon Points"
unballoon_points = sum(s.count(letra) for letra in target)

# Saída do resultado
print(unballoon_points)