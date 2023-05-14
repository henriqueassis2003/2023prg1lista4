def hanoi(n, origem, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 da pilha {origem} para a pilha {destino}")
    else:
        hanoi(n-1, origem, auxiliar, destino)
        print(f"Mover disco {n} da pilha {origem} para a pilha {destino}")
        hanoi(n-1, auxiliar, destino, origem)

# Exemplo de uso
hanoi(3, 'Esquerda', 'Direita', 'Auxiliar')

