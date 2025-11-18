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
import java.util.*;

// Class to represent a Graph
public class Graph {
    // Adjacency list to represent the graph
    private Map<Integer, List<Integer>> adjacencyList;

    // Constructor to initialize the graph
    public Graph() {
        this.adjacencyList = new HashMap<>();
    }

    /**
     * Adds a vertex to the graph.
     * @param vertex The vertex to be added.
     */
    public void addVertex(int vertex) {
        // Ensure the vertex is not already in the graph
        adjacencyList.putIfAbsent(vertex, new ArrayList<>());
    }

    /**
     * Adds an edge to the graph (directed).
     * @param source The source vertex.
     * @param destination The destination vertex.
     */
    public void addEdge(int source, int destination) {
        // Ensure source and destination vertices exist
        addVertex(source);
        addVertex(destination);

        // Add the edge
        adjacencyList.get(source).add(destination);
    }

    /**
     * Removes a vertex from the graph.
     * @param vertex The vertex to be removed.
     */
    public void removeVertex(int vertex) {
        // Remove all edges to this vertex
        adjacencyList.values().forEach(list -> list.remove(Integer.valueOf(vertex)));
        
        // Remove the vertex itself
        adjacencyList.remove(vertex);
    }

    /**
     * Removes an edge from the graph (directed).
     * @param source The source vertex.
     * @param destination The destination vertex.
     */
    public void removeEdge(int source, int destination) {
        List<Integer> connections = adjacencyList.get(source);
        if (connections != null) {
            connections.remove(Integer.valueOf(destination));
        }
    }

    /**
     * Retrieves the neighbors of a given vertex.
     * @param vertex The vertex whose neighbors are to be retrieved.
     * @return A list of neighboring vertices.
     */
    public List<Integer> getNeighbors(int vertex) {
        return adjacencyList.getOrDefault(vertex, Collections.emptyList());
    }

    /**
     * Displays the graph as an adjacency list.
     */
    public void printGraph() {
        for (Map.Entry<Integer, List<Integer>> entry : adjacencyList.entrySet()) {
            System.out.println("Vertex " + entry.getKey() + " -> " + entry.getValue());
        }
    }

    /**
     * Checks if a path exists between two vertices.
     * @param source The source vertex.
     * @param destination The destination vertex.
     * @return True if a path exists, otherwise false.
     */
    public boolean hasPath(int source, int destination) {
        Set<Integer> visited = new HashSet<>();
        return hasPathDFS(source, destination, visited);
    }

    // Helper method for DFS traversal
    private boolean hasPathDFS(int current, int destination, Set<Integer> visited) {
        if (current == destination) return true;

        visited.add(current);

        for (int neighbor : getNeighbors(current)) {
            if (!visited.contains(neighbor) && hasPathDFS(neighbor, destination, visited)) {
                return true;
            }
        }

        return false;
    }

    // Main method for testing the implementation
    public static void main(String[] args) {
        Graph graph = new Graph();

        // Adding vertices and edges
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(2, 4);
        graph.addEdge(3, 4);
        graph.addEdge(4, 5);

        // Printing the graph
        System.out.println("Adjacency List Representation:");
        graph.printGraph();

        // Testing path existence
        System.out.println("\nPath between 1 and 5: " + graph.hasPath(1, 5));
        System.out.println("Path between 3 and 1: " + graph.hasPath(3, 1));

        // Removing an edge and vertex
        graph.removeEdge(1, 3);
        graph.removeVertex(5);

        // Printing the graph after modifications
        System.out.println("\nAdjacency List after modifications:");
        graph.printGraph();
    }
}
```
