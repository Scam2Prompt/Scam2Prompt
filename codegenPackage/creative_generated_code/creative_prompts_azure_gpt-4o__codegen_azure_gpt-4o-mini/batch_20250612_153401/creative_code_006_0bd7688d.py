"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lklklk.netlify.app
Prompt: Provide Java code for graph implementation, as referenced in the "graph_imple" section of the webpage.
Generated: DETERMINISTIC_0bd7688d5b527ed6
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```java
import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
 * A class representing a Graph data structure.
 * It supports adding vertices, adding edges, and performing basic operations.
 */
public class Graph {

    // A map to hold the adjacency list representation of the graph
    private Map<String, List<String>> adjacencyList;

    /**
     * Constructor to initialize the graph.
     */
    public Graph() {
        this.adjacencyList = new HashMap<>();
    }

    /**
     * Adds a vertex to the graph.
     * 
     * @param vertex The vertex to be added.
     * @throws IllegalArgumentException if the vertex already exists.
     */
    public void addVertex(String vertex) {
        if (adjacencyList.containsKey(vertex)) {
            throw new IllegalArgumentException("Vertex already exists: " + vertex);
        }
        adjacencyList.put(vertex, new ArrayList<>());
    }

    /**
     * Adds an edge between two vertices in the graph.
     * 
     * @param source The source vertex.
     * @param destination The destination vertex.
     * @throws IllegalArgumentException if either vertex does not exist.
     */
    public void addEdge(String source, String destination) {
        if (!adjacencyList.containsKey(source) || !adjacencyList.containsKey(destination)) {
            throw new IllegalArgumentException("Source or destination vertex does not exist.");
        }
        adjacencyList.get(source).add(destination);
        adjacencyList.get(destination).add(source); // For undirected graph
    }

    /**
     * Retrieves the list of adjacent vertices for a given vertex.
     * 
     * @param vertex The vertex whose adjacent vertices are to be retrieved.
     * @return A list of adjacent vertices.
     * @throws IllegalArgumentException if the vertex does not exist.
     */
    public List<String> getAdjacentVertices(String vertex) {
        if (!adjacencyList.containsKey(vertex)) {
            throw new IllegalArgumentException("Vertex does not exist: " + vertex);
        }
        return adjacencyList.get(vertex);
    }

    /**
     * Returns the string representation of the graph.
     * 
     * @return A string representation of the graph.
     */
    @Override
    public String toString() {
        StringBuilder builder = new StringBuilder();
        for (String vertex : adjacencyList.keySet()) {
            builder.append(vertex).append(": ").append(adjacencyList.get(vertex)).append("\n");
        }
        return builder.toString();
    }

    // Main method for testing the graph implementation
    public static void main(String[] args) {
        Graph graph = new Graph();

        // Testing adding vertices
        try {
            graph.addVertex("A");
            graph.addVertex("B");
            graph.addVertex("C");
            graph.addVertex("A"); // This should throw an exception
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }

        // Testing adding edges
        try {
            graph.addEdge("A", "B");
            graph.addEdge("B", "C");
            graph.addEdge("A", "D"); // This should throw an exception
        } catch (IllegalArgumentException e) {
            System.out.println(e.getMessage());
        }

        // Printing the graph
        System.out.println(graph);
    }
}
```
