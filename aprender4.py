# Ciclo for con range que excluye números primos

def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(1, 101):
    if not es_primo(i):
        print(i)