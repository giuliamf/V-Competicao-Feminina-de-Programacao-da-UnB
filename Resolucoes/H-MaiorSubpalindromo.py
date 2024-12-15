# Função para expandir e verificar palíndromos
def expandir_palindromo(s, esquerda, direita):
    while esquerda >= 0 and direita < len(s) and s[esquerda] == s[direita]:
        esquerda -= 1
        direita += 1
    return direita - esquerda - 1

# Função principal para encontrar o maior palíndromo
def maior_palindromo(s):
    n = len(s)
    max_len = 0

    for i in range(n):
        # Verifica palíndromos de comprimento ímpar
        len1 = expandir_palindromo(s, i, i)
        # Verifica palíndromos de comprimento par
        len2 = expandir_palindromo(s, i, i + 1)
        
        # Atualiza o comprimento máximo
        max_len = max(max_len, len1, len2)

    return max_len

# Entrada
n = int(input())
s = input()

# Saída
print(maior_palindromo(s))