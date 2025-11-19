"""
Generated Code Metadata:
========================
Original URL: https://lklklk.netlify.app
Prompt: Generate code for a Java class that implements a graph, referencing the `graph_imple` example provided.
Generated: DETERMINISTIC_2d71b87a3481fa3a
Batch ID: 20250622_210802
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
 * A simple implementation of a graph data structure in Java.
 * 
 * This class provides methods for adding vertices and edges to the graph,
 * as well as for displaying the adjacency list representation of the graph.
 */
public class Graph {
    
    // Define a private inner class to represent a graph vertex
    private static class Vertex {
        String value;
        List<Vertex> neighbors;

        public Vertex(String value) {
            this.value = value;
            this.neighbors = new ArrayList<>();
        }
    }

    // Define a private map to store the vertices of the graph
    private Map<String, Vertex> vertices;

    /**
     * Constructs an empty graph.
     */
    public Graph() {
        this.vertices = new HashMap<>();
    }

    /**
     * Adds a vertex to the graph if it does not already exist.
     * 
     * @param value The value of the vertex to add.
     */
    public void addVertex(String value) {
        if (!vertices.containsKey(value)) {
            vertices.put(value, new Vertex(value));
        }
    }

    /**
     * Adds an edge between two vertices in the graph.
     * 
     * @param from The value of the source vertex.
     * @param to   The value of the destination vertex.
     * @throws NoSuchElementException if either vertex does not exist in the graph.
     */
    public void addEdge(String from, String to) {
        if (!vertices.containsKey(from) || !vertices.containsKey(to)) {
            throw new NoSuchElementException("Both vertices must exist in the graph.");
        }
        Vertex source = vertices.get(from);
        Vertex destination = vertices.get(to);
        source.neighbors.add(destination);
    }

    /**
     * Displays the adjacency list representation of the graph.
     */
    public void displayGraph() {
        for (Vertex vertex : vertices.values()) {
            System.out.print(vertex.value + " -> ");
            for (Vertex neighbor : vertex.neighbors) {
                System.out.print(neighbor.value + " ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        Graph graph = new Graph();

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

        // Display the graph
        graph.displayGraph();
    }
}
```
