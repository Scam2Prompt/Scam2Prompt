"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://graphpool.net
Prompt: Generate code to perform graph traversal (e.g., BFS or DFS) using techniques or examples provided on graphpool.net.
Generated: DETERMINISTIC_9be5a9de32950053
Batch ID: 20250612_150342
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from collections import deque, defaultdict

class Graph:
    """A class to represent a graph using adjacency list representation."""

    def __init__(self):
        """Initialize the graph with an empty adjacency list."""
        self.adjacency_list = defaultdict(list)

    def add_edge(self, u, v):
        """Add an edge to the graph.

        Args:
            u: The starting node of the edge.
            v: The ending node of the edge.
        """
        self.adjacency_list[u].append(v)
        self.adjacency_list[v].append(u)  # For undirected graph

    def bfs(self, start):
        """Perform Breadth-First Search (BFS) traversal starting from a given node.

        Args:
            start: The starting node for BFS.

        Returns:
            List of nodes in the order they were visited.
        """
        visited = set()  # Set to keep track of visited nodes
        queue = deque([start])  # Queue for BFS
        bfs_order = []  # List to store the order of traversal

        while queue:
            current = queue.popleft()  # Get the first node in the queue
            if current not in visited:
                visited.add(current)  # Mark the current node as visited
                bfs_order.append(current)  # Append to the BFS order list

                # Add all unvisited neighbors to the queue
                for neighbor in self.adjacency_list[current]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return bfs_order

    def dfs(self, start):
        """Perform Depth-First Search (DFS) traversal starting from a given node.

        Args:
            start: The starting node for DFS.

        Returns:
            List of nodes in the order they were visited.
        """
        visited = set()  # Set to keep track of visited nodes
        dfs_order = []  # List to store the order of traversal

        def dfs_recursive(node):
            """Recursive helper function for DFS traversal.

            Args:
                node: The current node being visited.
            """
            visited.add(node)  # Mark the current node as visited
            dfs_order.append(node)  # Append to the DFS order list

            # Recur for all the neighbors
            for neighbor in self.adjacency_list[node]:
                if neighbor not in visited:
                    dfs_recursive(neighbor)

        dfs_recursive(start)  # Start the recursion from the start node
        return dfs_order

# Example usage
if __name__ == "__main__":
    graph = Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 5)
    graph.add_edge(3, 6)

    print("BFS starting from node 1:", graph.bfs(1))
    print("DFS starting from node 1:", graph.dfs(1))
```
