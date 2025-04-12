from collections import deque

def flood_fill(matriz, i , j, cor_antiga, cor_nova):
    if i <0 or i>= len(matriz) or j<0 or j >= len(matriz[0]):
        return # fora dos limites
    
    if matriz[i][j] != cor_antiga:
        return # já foi preenchido ou é de outra cor
    
    matriz[i][j] = cor_nova # pintar

    flood_fill(matriz, i+1,  j, cor_antiga, cor_nova) # baixo
    flood_fill(matriz, i-1, j, cor_antiga, cor_nova) # cima
    flood_fill(matriz,i ,j+1, cor_antiga, cor_nova) # direita
    flood_fill(matriz, i, j-1, cor_antiga, cor_nova) # esquerda


matriz = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 0]
]

flood_fill(matriz, 0, 0, 1, 9)

for linha in matriz:
    print(linha)