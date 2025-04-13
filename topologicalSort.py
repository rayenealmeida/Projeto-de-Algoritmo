def topological_sort(graph):
    visited = set()
    stack = []

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    return stack[::-1]  # Inverter pilha

# DAG
graph = {
    'v1': [],
    'v2': ['v1', 'v3'],
    'v3': ['v4'],
    'v4': [],
    'v5': ['v1', 'v6'],
    'v6': ['v4'],
    'v7': ['v1']
}

print(topological_sort(graph))
