N = int(input())
palavra = input()

count_x = 0

for letra in palavra:
    if letra == 'x':
        count_x += 1

print(count_x)
