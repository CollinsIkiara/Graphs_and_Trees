# 🧠 Graph Algorithms & Problem Solving in Python

A collection of classic computer science algorithms implemented in Python — covering **graph traversal**, **pathfinding**, **backtracking**, and **graph representation utilities**.

---

## 📁 File Overview

| File | Algorithm | Category |
|------|-----------|----------|
| `Adjacency_List_to_Matrix_Converter.py` | Graph Representation Converter | Graph Utilities |
| `Breadth_First_Search_Algorithm.py` | BFS — Parentheses Generation | Graph Traversal |
| `Depth_First_Search_Algorithm.py` | DFS — Graph Traversal | Graph Traversal |
| `N-Queens_Algorithm.py` | N-Queens via DFS + Backtracking | Backtracking |
| `Shortest_Path_Algorithm.py` | Dijkstra's Shortest Path | Pathfinding |

---

## 📄 File Descriptions

### 1. `Adjacency_List_to_Matrix_Converter.py`

**Purpose:** Converts a graph from adjacency list format to an adjacency matrix.

**How it works:**
- Accepts a dictionary where each key is a node and its value is a list of neighboring nodes.
- Initializes an `n × n` matrix filled with zeros, where `n` is the total number of nodes.
- Iterates over each node and its neighbors, setting `matrix[node][neighbor] = 1` to mark a directed edge.
- Prints and returns the completed adjacency matrix.

**Input:** `{0: [1, 2], 1: [2], 2: [0, 3], 3: [2]}`

**Output:**
```
[0, 1, 1, 0]
[0, 0, 1, 0]
[1, 0, 0, 1]
[0, 0, 1, 0]
```

> **Note:** This implementation handles directed graphs. A `1` at position `[i][j]` indicates a one-way edge from node `i` to node `j`.

---

### 2. `Breadth_First_Search_Algorithm.py`

**Purpose:** Generates all valid combinations of well-formed parentheses using a BFS approach.

**How it works:**
- Uses a queue initialized with an empty string and counters for open/close parentheses used.
- At each step, it dequeues the current state and:
  - Appends an open parenthesis `(` if the count of opens used is less than `pairs`.
  - Appends a close parenthesis `)` if the count of closes used is less than opens used.
- When the string reaches `2 * pairs` characters, it is added to the results.
- Validates that the input is an integer and at least `1`.

**Input:** `gen_parentheses(3)`

**Output:** `['((()))', '(()())', '(())()', '()(())', '()()()']`

> **Note:** While this problem is more combinatorial than a typical graph search, it uses the BFS queue-based level-order exploration strategy to systematically build valid strings.

---

### 3. `Depth_First_Search_Algorithm.py`

**Purpose:** Performs a Depth-First Search (DFS) traversal of a graph represented as an adjacency matrix.

**How it works:**
- Accepts an adjacency matrix and a starting node.
- Uses an explicit stack to simulate the DFS (iterative approach, not recursive).
- At each step, pops a node from the stack, marks it as visited, and appends it to the result.
- Adds unvisited neighbors to the stack in **reverse order** to ensure correct left-to-right traversal.
- Returns the list of nodes in the order they were visited.

**Example:**
```python
dfs([[0,1,0,0],[1,0,1,0],[0,1,0,1],[0,0,1,0]], start=1)
# Output: [1, 0, 2, 3]
```

> **Note:** Neighbors are iterated in reverse order before pushing to the stack so that the node with the smallest index is explored first — preserving the expected DFS left-to-right ordering.

---

### 4. `N-Queens_Algorithm.py`

**Purpose:** Finds all valid placements of `n` queens on an `n × n` chessboard such that no two queens threaten each other.

**How it works:**
- Uses recursive DFS with **backtracking**.
- Tracks three constraint sets: occupied columns (`cols`), occupied diagonals going top-left to bottom-right (`diag1` = `row - col`), and anti-diagonals (`diag2` = `row + col`).
- For each row, it tries placing a queen in every column. If placing there violates any constraint, it skips.
- On a successful placement, it recurses to the next row.
- On reaching the final row, the current arrangement is saved as a valid solution.
- Backtracks by removing the queen and its constraints before trying the next column.

**Output format:** Each solution is a list of column indices per row.

```python
dfs_n_queens(4)
# Output: [[1, 3, 0, 2], [2, 0, 3, 1]]

len(dfs_n_queens(8))
# Output: 92
```

> **Note:** Returns an empty list for `n < 1`, and no solutions exist for `n = 2` or `n = 3`.

---

### 5. `Shortest_Path_Algorithm.py`

**Purpose:** Finds the shortest path between nodes in a weighted graph using **Dijkstra's Algorithm**.

**How it works:**
- Represents the graph as an adjacency matrix where `INF` (infinity) denotes no direct connection.
- Maintains a `distances` array initialized to `INF`, with the start node set to `0`.
- Iteratively selects the unvisited node with the smallest known distance.
- For each unvisited neighbor, calculates the new distance through the current node and updates if it's shorter.
- Records the full path to each node for traceback.
- If a `target_node` is specified, only that path is printed; otherwise all reachable paths are shown.

**Example graph (6 nodes):**
```
Node 0 --5-- Node 1
Node 0 --3-- Node 2
Node 2 --1-- Node 1
Node 1 --2-- Node 5
...
```

**Output:**
```
0-5 distance: 6
Path: 0 -> 2 -> 1 -> 5
```

> **Note:** This implementation assumes a static adjacency matrix. `INF = float('inf')` is used as a sentinel value for absent edges.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher
- No external libraries required — all implementations use the Python standard library only.

### Running the Files

```bash
# Clone or download the files, then run any script:
python Adjacency_List_to_Matrix_Converter.py
python Breadth_First_Search_Algorithmn.py
python Depth_First_Search_Algorithm.py
python N-Queens_Algorithm.py
python Shortest_Path_Algorithmn.py
```

Each file contains built-in test cases that run automatically when executed.

---

## 🧩 Algorithm Complexity Summary

| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|-----------------|
| Adjacency List → Matrix | O(V + E) | O(V²) |
| BFS Parentheses | O(4ⁿ / √n) | O(4ⁿ / √n) |
| DFS Traversal | O(V²) | O(V) |
| N-Queens (Backtracking) | O(N!) | O(N) |
| Dijkstra's (Matrix) | O(V²) | O(V) |

> V = number of vertices, E = number of edges, N = board size

---

## 📚 Concepts Covered

- **Graph Representations** — adjacency list vs adjacency matrix
- **Breadth-First Search (BFS)** — level-order queue-based exploration
- **Depth-First Search (DFS)** — stack-based iterative graph traversal
- **Backtracking** — constraint-based pruning with state restoration
- **Greedy Algorithms** — Dijkstra's optimal substructure and greedy node selection
