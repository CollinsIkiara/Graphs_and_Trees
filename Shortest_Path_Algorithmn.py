# Shortest Path Algorithmn

# This code implements Dijkstra's algorithm to find the shortest path from a starting node to a target node (or all nodes if no target is specified) in a graph represented as an adjacency matrix. The algorithm maintains a list of distances from the starting node to each node, and a list of paths taken to reach each node. It iteratively selects the unvisited node with the smallest distance, marks it as visited, and updates the distances to its neighboring nodes. Finally, it prints the shortest distance and path from the starting node to the target node(s).

INF = float('inf') # The value representing infinity, used to indicate no direct path between nodes in the adjacency matrix.
adj_matrix = [
    [0, 5, 3, INF, 11, INF],
    [5, 0, 1, INF, INF, 2],
    [3, 1, 0, 1, 5, INF],
    [INF, INF, 1, 0, 9, 3],
    [11, INF, 5, 9, 0, INF],
    [INF, 2, INF, 3, INF, 0],
] # The adjacency matrix representing the graph, where the value at matrix[i][j] is the distance from node i to node j. A value of INF indicates that there is no direct path between the nodes.

def shortest_path(matrix, start_node, target_node=None):
    n = len(matrix)
    distances = [INF] * n
    distances[start_node] = 0
    paths = [[node_no] for node_no in range(n)]
    visited = [False] * n

    for _ in range(n):
        min_distance = INF
        current = -1
        for node_no in range(n):
            if not visited[node_no] and distances[node_no] < min_distance:
                min_distance = distances[node_no]
                current = node_no

        if current == -1:
            break
        visited[current] = True

        for node_no in range(n):
            distance = matrix[current][node_no]
            if distance != INF and not visited[node_no]:
                new_distance = distances[current] + distance
                if new_distance < distances[node_no]:
                    distances[node_no] = new_distance
                    paths[node_no] = paths[current] + [node_no]

    targets = [target_node] if target_node is not None else range(n)
    for node_no in targets:
        if node_no == start_node or distances[node_no] == INF:
            continue
        string_path = (str(n) for n in paths[node_no])
        path = ' -> '.join(string_path)
        print(f'\n{start_node}-{node_no} distance: {distances[node_no]}\nPath: {path}')

    return distances, paths

shortest_path(adj_matrix, 0, 5)

## Output:
# 0-5 distance: 6
# Path: 0 -> 2 -> 1 -> 5