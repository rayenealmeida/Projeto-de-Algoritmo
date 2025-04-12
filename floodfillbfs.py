from collections import deque
def flood_fill_bfs(matriz, i , j , cor_antiga, cor_nova):
    if matriz[i][j] != cor_antiga:
        return
    
    fila = deque()
    fila.append((i, j))

    while fila:
        x, y = fila.popleft()
        matriz[x][y] = cor_nova

        for dx, dy in [(-1, 0), (1,0), (0,-1), (0,1)]:
            nx, ny = x+ dx, y +dy
            if 0 <= nx< len(matriz)  and 0 <= ny < len(matriz[0]) and matriz[nx][ny] == cor_antiga:
                fila.append((nx, ny))

matriz = [
    [1, 1, 0],
    [0, 1, 1],
    [1, 0, 0]
]

flood_fill_bfs(matriz, 1, 1, 1, 5)

for linha in matriz:
    print(linha)