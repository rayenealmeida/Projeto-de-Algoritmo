from collections import deque

def is_bipartite(graph):
    color = {}
    for node in color:
        queue = deque([node])
        color[node] = 0
        
        while queue:
            current = queue.popleft()
            for neighbor in graph[current]:
                if neighbor not in color:
                    color[neighbor] = 1 - color[current]
                    queue.append(neighbor)

                elif color[neighbor] == color[current]:
                    return False
    return True

graph =    {
    'A': ['1'],
    'B': ['2'],
    'C': ['3'],
    '1': ['A'],
    '2': ['B'],
    '3': ['C']
}     

print(is_bipartite(graph))