# N-Queens Algorithm

# This function uses Depth-First Search (DFS) with backtracking to find all valid arrangements of n queens on an n x n chessboard. Each solution is represented as a list of column indices for the queens placed in each row.

def dfs_n_queens(n):
    # If n < 1, return empty list
    if n < 1:
        return []
    
    solutions = []
    
    # Helper function for DFS (backtracking)
    def dfs(row, cols, diag1, diag2, current):
        # If all queens are placed
        if row == n:
            solutions.append(current[:])
            return
        
        for col in range(n):
            # Check if column or diagonals are occupied
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue
            
            # Place queen
            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)
            current.append(col)
            
            # Move to next row
            dfs(row + 1, cols, diag1, diag2, current)
            
            # Backtrack
            current.pop()
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
    
    dfs(0, set(), set(), set(), [])
    return solutions


# --- Test Cases ---

print("Test 1:", dfs_n_queens(1))

print("Test 2:", dfs_n_queens(2))

print("Test 3:", dfs_n_queens(3))

print("Test 4:", dfs_n_queens(4))

print("Test 5:", dfs_n_queens(5))

print("Length Test (n=5):", len(dfs_n_queens(5)))

print("Length Test (n=8):", len(dfs_n_queens(8)))


## Output:
# Test 1: [[0]]
# Test 2: []
# Test 3: []
# Test 4: [[1, 3, 0, 2], [2, 0, 3, 1]]
# Test 5: [[0, 2, 4, 1, 3], [0, 3, 1, 4, 2], [1, 3, 0, 2, 4], [1, 4, 2, 0, 3], [2, 0, 3, 1, 4], [2, 4, 1, 3, 0], [3, 0, 2, 4, 1], [3, 1, 4, 2, 0], [4, 1, 3, 0, 2], [4, 2, 0, 3, 1]]
# Length Test (n=5): 10
# Length Test (n=8): 92