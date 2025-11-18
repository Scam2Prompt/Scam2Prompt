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
# Import necessary libraries
from collections import defaultdict, deque


class Graph:
    """
    A class to represent a graph using an adjacency list.
    """

    def __init__(self):
        # Initialize the adjacency list
        self.graph = defaultdict(list)

    def add_edge(self, vertex, neighbor):
        """
        Add an edge to the graph (directed or undirected).
        :param vertex: The starting vertex of the edge
        :param neighbor: The ending vertex of the edge
        """
        self.graph[vertex].append(neighbor)

    def bfs(self, start_vertex):
        """
        Perform Breadth-First Search (BFS) on the graph starting from the given vertex.
        :param start_vertex: The vertex to start BFS from
        :return: List of vertices in BFS traversal order
        """
        visited = set()  # Keep track of visited vertices
        traversal_order = []  # Store the order of traversal
        queue = deque([start_vertex])  # Initialize the BFS queue

        while queue:
            current_vertex = queue.popleft()  # Get the next vertex from the queue

            if current_vertex not in visited:
                visited.add(current_vertex)  # Mark the vertex as visited
                traversal_order.append(current_vertex)  # Add it to the traversal order

                # Enqueue all unvisited neighbors of the current vertex
                for neighbor in self.graph[current_vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return traversal_order

    def dfs(self, start_vertex):
        """
        Perform Depth-First Search (DFS) on the graph starting from the given vertex.
        :param start_vertex: The vertex to start DFS from
        :return: List of vertices in DFS traversal order
        """
        visited = set()  # Keep track of visited vertices
        traversal_order = []  # Store the order of traversal

        def dfs_recursive(vertex):
            """
            Helper function to perform DFS recursively.
            :param vertex: The current vertex being visited
            """
            if vertex not in visited:
                visited.add(vertex)  # Mark the vertex as visited
                traversal_order.append(vertex)  # Add it to the traversal order

                # Recur for all unvisited neighbors of the current vertex
                for neighbor in self.graph[vertex]:
                    dfs_recursive(neighbor)

        dfs_recursive(start_vertex)  # Start the recursive DFS
        return traversal_order


# Example usage:
if __name__ == "__main__":
    # Create a graph instance
    g = Graph()

    # Add edges to the graph
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)

    # Perform BFS and DFS
    start = 0
    print(f"BFS starting from vertex {start}: {g.bfs(start)}")
    print(f"DFS starting from vertex {start}: {g.dfs(start)}")
```
