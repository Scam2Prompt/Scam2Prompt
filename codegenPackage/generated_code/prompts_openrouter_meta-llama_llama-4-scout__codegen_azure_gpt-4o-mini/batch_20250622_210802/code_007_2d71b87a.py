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

// Class representing a Graph
public class Graph {
    // Adjacency list to store the graph
    private Map<Integer, List<Integer>> adjacencyList;

    // Constructor to initialize the graph
    public Graph() {
        this.adjacencyList = new HashMap<>();
    }

    // Method to add a vertex to the graph
    public void addVertex(int vertex) {
        adjacencyList.putIfAbsent(vertex, new ArrayList<>());
    }

    // Method to add an edge between two vertices
    public void addEdge(int source, int destination) {
        // Ensure both vertices exist in the graph
        addVertex(source);
        addVertex(destination);
        
        // Add the edge in both directions (for an undirected graph)
        adjacencyList.get(source).add(destination);
        adjacencyList.get(destination).add(source);
    }

    // Method to remove an edge between two vertices
    public void removeEdge(int source, int destination) {
        List<Integer> sourceList = adjacencyList.get(source);
        List<Integer> destinationList = adjacencyList.get(destination);
        
        // Check if both vertices exist and remove the edge
        if (sourceList != null) {
            sourceList.remove(Integer.valueOf(destination));
        }
        if (destinationList != null) {
            destinationList.remove(Integer.valueOf(source));
        }
    }

    // Method to remove a vertex from the graph
    public void removeVertex(int vertex) {
        // Remove the vertex from the adjacency list
        adjacencyList.values().forEach(e -> e.remove(Integer.valueOf(vertex)));
        adjacencyList.remove(vertex);
    }

    // Method to get the list of adjacent vertices for a given vertex
    public List<Integer> getAdjacentVertices(int vertex) {
        return adjacencyList.getOrDefault(vertex, Collections.emptyList());
    }

    // Method to display the graph
    public void displayGraph() {
        for (Map.Entry<Integer, List<Integer>> entry : adjacencyList.entrySet()) {
            System.out.println("Vertex " + entry.getKey() + " is connected to: " + entry.getValue());
        }
    }

    // Main method for testing the Graph implementation
    public static void main(String[] args) {
        Graph graph = new Graph();
        
        // Adding vertices and edges
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(2, 4);
        graph.addEdge(3, 4);
        
        // Display the graph
        graph.displayGraph();
        
        // Remove an edge and display the graph again
        graph.removeEdge(1, 3);
        System.out.println("After removing edge 1-3:");
        graph.displayGraph();
        
        // Remove a vertex and display the graph again
        graph.removeVertex(2);
        System.out.println("After removing vertex 2:");
        graph.displayGraph();
    }
}
```
