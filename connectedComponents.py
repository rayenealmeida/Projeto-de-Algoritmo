def dfs(graph, v, visited, component):
    visited[v] = True
    component.append(v)
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(graph, neighbor, visited, component)


def connected_components(graph):
    visited = {v: False for v in graph}
    components= []

    for v in graph:
        if not visited[v]:
            component = []
            dfs(graph, v, visited, component)
            components.append(component)

    return components

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['F'],
    'F': ['E']
}

print(connected_components(graph))