"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Provide Java code for graph implementation, as referenced in the "graph_imple" section of the webpage.
Generated: DETERMINISTIC_0bd7688d5b527ed6
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.*;

/**
 * Graph implementation in Java.
 * 
 * This implementation provides basic operations for a graph, including adding vertices and edges,
 * removing vertices and edges, and traversing the graph using depth-first search (DFS) and
 * breadth-first search (BFS).
 * 
 * @author [Your Name]
 */
public class Graph<T> {

    // Adjacency list representation of the graph
    private final Map<T, List<T>> adjacencyList;

    /**
     * Constructs an empty graph.
     */
    public Graph() {
        this.adjacencyList = new HashMap<>();
    }

    /**
     * Adds a vertex to the graph.
     * 
     * @param vertex the vertex to add
     */
    public void addVertex(T vertex) {
        if (!adjacencyList.containsKey(vertex)) {
            adjacencyList.put(vertex, new ArrayList<>());
        }
    }

    /**
     * Removes a vertex from the graph.
     * 
     * @param vertex the vertex to remove
     */
    public void removeVertex(T vertex) {
        if (adjacencyList.containsKey(vertex)) {
            adjacencyList.remove(vertex);
            for (List<T> adjacentVertices : adjacencyList.values()) {
                adjacentVertices.remove(vertex);
            }
        }
    }

    /**
     * Adds an edge between two vertices in the graph.
     * 
     * @param source      the source vertex
     * @param destination the destination vertex
     */
    public void addEdge(T source, T destination) {
        if (adjacencyList.containsKey(source) && adjacencyList.containsKey(destination)) {
            adjacencyList.get(source).add(destination);
            adjacencyList.get(destination).add(source); // Comment out for directed graph
        }
    }

    /**
     * Removes an edge between two vertices in the graph.
     * 
     * @param source      the source vertex
     * @param destination the destination vertex
     */
    public void removeEdge(T source, T destination) {
        if (adjacencyList.containsKey(source) && adjacencyList.containsKey(destination)) {
            adjacencyList.get(source).remove(destination);
            adjacencyList.get(destination).remove(source); // Comment out for directed graph
        }
    }

    /**
     * Performs a depth-first search (DFS) traversal of the graph.
     * 
     * @param startVertex the starting vertex
     * @return a list of visited vertices
     */
    public List<T> dfs(T startVertex) {
        Set<T> visited = new HashSet<>();
        List<T> traversalOrder = new ArrayList<>();
        dfsHelper(startVertex, visited, traversalOrder);
        return traversalOrder;
    }

    private void dfsHelper(T vertex, Set<T> visited, List<T> traversalOrder) {
        visited.add(vertex);
        traversalOrder.add(vertex);
        for (T adjacentVertex : adjacencyList.get(vertex)) {
            if (!visited.contains(adjacentVertex)) {
                dfsHelper(adjacentVertex, visited, traversalOrder);
            }
        }
    }

    /**
     * Performs a breadth-first search (BFS) traversal of the graph.
     * 
     * @param startVertex the starting vertex
     * @return a list of visited vertices
     */
    public List<T> bfs(T startVertex) {
        Set<T> visited = new HashSet<>();
        List<T> traversalOrder = new ArrayList<>();
        Queue<T> queue = new LinkedList<>();

        visited.add(startVertex);
        traversalOrder.add(startVertex);
        queue.add(startVertex);

        while (!queue.isEmpty()) {
            T vertex = queue.poll();
            for (T adjacentVertex : adjacencyList.get(vertex)) {
                if (!visited.contains(adjacentVertex)) {
                    visited.add(adjacentVertex);
                    traversalOrder.add(adjacentVertex);
                    queue.add(adjacentVertex);
                }
            }
        }

        return traversalOrder;
    }

    public static void main(String[] args) {
        Graph<String> graph = new Graph<>();

        // Add vertices
        graph.addVertex("A");
        graph.addVertex("B");
        graph.addVertex("C");
        graph.addVertex("D");

        // Add edges
        graph.addEdge("A", "B");
        graph.addEdge("A", "C");
        graph.addEdge("B", "D");
        graph.addEdge("C", "D");

        // Perform DFS traversal
        List<String> dfsTraversal = graph.dfs("A");
        System.out.println("DFS Traversal: " + dfsTraversal);

        // Perform BFS traversal
        List<String> bfsTraversal = graph.bfs("A");
        System.out.println("BFS Traversal: " + bfsTraversal);

        // Remove edge
        graph.removeEdge("A", "C");

        // Perform DFS traversal after edge removal
        List<String> dfsTraversalAfterRemoval = graph.dfs("A");
        System.out.println("DFS Traversal after edge removal: " + dfsTraversalAfterRemoval);
    }
}
```
