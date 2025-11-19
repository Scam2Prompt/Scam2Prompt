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
 * A class representing a graph using an adjacency list.
 * This implementation supports both directed and undirected graphs.
 */
public class Graph {
    private final Map<Integer, List<Integer>> adjacencyList;
    private final boolean isDirected;

    /**
     * Constructor to initialize the graph.
     *
     * @param isDirected true if the graph is directed, false if undirected.
     */
    public Graph(boolean isDirected) {
        this.adjacencyList = new HashMap<>();
        this.isDirected = isDirected;
    }

    /**
     * Adds a vertex to the graph.
     *
     * @param vertex The vertex to be added.
     */
    public void addVertex(int vertex) {
        adjacencyList.putIfAbsent(vertex, new ArrayList<>());
    }

    /**
     * Adds an edge between two vertices.
     *
     * @param source      The source vertex.
     * @param destination The destination vertex.
     * @throws IllegalArgumentException if either vertex does not exist.
     */
    public void addEdge(int source, int destination) {
        if (!adjacencyList.containsKey(source) || !adjacencyList.containsKey(destination)) {
            throw new IllegalArgumentException("Both vertices must exist in the graph.");
        }

        adjacencyList.get(source).add(destination);

        // If the graph is undirected, add the reverse edge as well.
        if (!isDirected) {
            adjacencyList.get(destination).add(source);
        }
    }

    /**
     * Removes an edge between two vertices.
     *
     * @param source      The source vertex.
     * @param destination The destination vertex.
     * @throws IllegalArgumentException if either vertex does not exist.
     */
    public void removeEdge(int source, int destination) {
        if (!adjacencyList.containsKey(source) || !adjacencyList.containsKey(destination)) {
            throw new IllegalArgumentException("Both vertices must exist in the graph.");
        }

        adjacencyList.get(source).remove(Integer.valueOf(destination));

        // If the graph is undirected, remove the reverse edge as well.
        if (!isDirected) {
            adjacencyList.get(destination).remove(Integer.valueOf(source));
        }
    }

    /**
     * Removes a vertex and all its associated edges from the graph.
     *
     * @param vertex The vertex to be removed.
     * @throws IllegalArgumentException if the vertex does not exist.
     */
    public void removeVertex(int vertex) {
        if (!adjacencyList.containsKey(vertex)) {
            throw new IllegalArgumentException("Vertex does not exist in the graph.");
        }

        // Remove all edges pointing to this vertex.
        adjacencyList.values().forEach(list -> list.remove(Integer.valueOf(vertex)));

        // Remove the vertex itself.
        adjacencyList.remove(vertex);
    }

    /**
     * Retrieves the neighbors of a given vertex.
     *
     * @param vertex The vertex whose neighbors are to be retrieved.
     * @return A list of neighboring vertices.
     * @throws IllegalArgumentException if the vertex does not exist.
     */
    public List<Integer> getNeighbors(int vertex) {
        if (!adjacencyList.containsKey(vertex)) {
            throw new IllegalArgumentException("Vertex does not exist in the graph.");
        }

        return Collections.unmodifiableList(adjacencyList.get(vertex));
    }

    /**
     * Checks if there is an edge between two vertices.
     *
     * @param source      The source vertex.
     * @param destination The destination vertex.
     * @return true if an edge exists, false otherwise.
     * @throws IllegalArgumentException if either vertex does not exist.
     */
    public boolean hasEdge(int source, int destination) {
        if (!adjacencyList.containsKey(source) || !adjacencyList.containsKey(destination)) {
            throw new IllegalArgumentException("Both vertices must exist in the graph.");
        }

        return adjacencyList.get(source).contains(destination);
    }

    /**
     * Prints the graph in adjacency list format.
     */
    public void printGraph() {
        for (Map.Entry<Integer, List<Integer>> entry : adjacencyList.entrySet()) {
            System.out.println(entry.getKey() + " -> " + entry.getValue());
        }
    }

    /**
     * Main method for testing the Graph class.
     */
    public static void main(String[] args) {
        Graph graph = new Graph(false); // Create an undirected graph.

        // Add vertices.
        graph.addVertex(1);
        graph.addVertex(2);
        graph.addVertex(3);
        graph.addVertex(4);

        // Add edges.
        graph.addEdge(1, 2);
        graph.addEdge(1, 3);
        graph.addEdge(2, 4);

        // Print the graph.
        System.out.println("Graph:");
        graph.printGraph();

        // Check neighbors.
        System.out.println("Neighbors of vertex 1: " + graph.getNeighbors(1));

        // Check edge existence.
        System.out.println("Edge between 1 and 2: " + graph.hasEdge(1, 2));
        System.out.println("Edge between 1 and 4: " + graph.hasEdge(1, 4));

        // Remove an edge.
        graph.removeEdge(1, 2);
        System.out.println("Graph after removing edge between 1 and 2:");
        graph.printGraph();

        // Remove a vertex.
        graph.removeVertex(3);
        System.out.println("Graph after removing vertex 3:");
        graph.printGraph();
    }
}
```
