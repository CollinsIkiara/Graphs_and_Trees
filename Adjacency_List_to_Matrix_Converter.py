# Adjacency List to Matrix Converter

# This function takes an adjacency list representation of a graph and converts it into an adjacency matrix. The adjacency list is a dictionary where each key is a node and the value is a list of neighboring nodes. The resulting adjacency matrix is a 2D list where the entry at row i and column j is 1 if there is an edge from node i to node j, and 0 otherwise.

def adjacency_list_to_matrix(adjacency_list):
    n = len(adjacency_list)
    matrix = [[0] * n for _ in range(n)]
    
    for node, neighbors in adjacency_list.items():
        for neighbor in neighbors:
            matrix[node][neighbor] = 1
    
    for row in matrix:
        print(row)
    
    return matrix

# Test examples
adjacency_list_to_matrix({0: [1, 2], 1: [2], 2: [0, 3], 3: [2]})
adjacency_list_to_matrix({0: [1], 1: [0]})
adjacency_list_to_matrix({0: [], 1: [], 2: []})
adjacency_list_to_matrix({0: [2], 1: [2, 3], 2: [0, 1, 3], 3: [1, 2]})

## Output:
# [0, 1, 1, 0]
# [0, 0, 1, 0]
# [1, 0, 0, 1]
# [0, 0, 1, 0]
# [0, 1]
# [1, 0]
# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 0]
# [0, 0, 1, 0]
# [0, 0, 1, 1]
# [1, 1, 0, 1]
# [0, 1, 1, 0]