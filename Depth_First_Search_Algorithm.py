# Depth-First Search Algorithm

# This implementation of the Depth-First Search (DFS) algorithm uses an adjacency matrix to represent the graph. The function `dfs` takes an adjacency matrix and a starting node as input and returns a list of nodes visited in the order they were traversed.

def dfs(adj_matrix, start):
    n = len(adj_matrix)
    visited = [False] * n
    stack = [start]
    result = []

    while stack:
        node = stack.pop()

        if not visited[node]:
            visited[node] = True
            result.append(node)

            # Add neighbors in reverse order for correct traversal
            for neighbor in range(n - 1, -1, -1):
                if adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                    stack.append(neighbor)

    return result


# --- Test Cases ---

print("Test 1:",
      dfs([[0, 1, 0, 0],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0]], 1))

print("Test 2:",
      dfs([[0, 1, 0, 0],
           [1, 0, 1, 0],
           [0, 1, 0, 1],
           [0, 0, 1, 0]], 3))

print("Test 3:",
      dfs([[0, 1, 0, 0],
           [1, 0, 1, 0],
           [0, 1, 0, 0],
           [0, 0, 0, 0]], 3))

print("Test 4:",
      dfs([[0, 1, 0, 0],
           [1, 0, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0]], 3))

print("Test 5:",
      dfs([[0, 1, 0, 0],
           [1, 0, 0, 0],
           [0, 0, 0, 1],
           [0, 0, 1, 0]], 0))


## Output:
# Test 1: [1, 0, 2, 3]
# Test 2: [3, 2, 1, 0]
# Test 3: [3]
# Test 4: [3, 2]
# Test 5: [0, 1]