N = int(input())

contador = 0
while contador < N:
    for _ in range(N):
        a, b, c = map(float, input().split())
        
        media = (a * 2 + b * 3 + c * 5) / (2 + 3 + 5)

        contador += 1
        
        print("Valores lidos:", a, b, c)
        print(f"Média: {media:.2f}")