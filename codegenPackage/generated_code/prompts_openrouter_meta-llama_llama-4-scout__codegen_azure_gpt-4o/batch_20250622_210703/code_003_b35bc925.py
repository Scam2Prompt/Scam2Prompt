"""
Generated Code Metadata:
========================
Original URL: https://enyakinvidanjor.com
Prompt: Create a Java program to calculate the optimal route for a vidanjör truck to take when servicing multiple locations across Istanbul, minimizing travel time and distance.
Generated: DETERMINISTIC_b35bc925e02a23e6
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```java
import java.util.ArrayList;
import java.util.List;
import java.util.PriorityQueue;

/**
 * A Java program to calculate the optimal route for a vidanjör truck
 * servicing multiple locations using Dijkstra's algorithm for shortest path.
 * This program assumes a graph representation of Istanbul's locations.
 */
public class OptimalRouteCalculator {

    // Class to represent a location in the graph
    static class Location {
        int id;
        String name;

        Location(int id, String name) {
            this.id = id;
            this.name = name;
        }
    }

    // Class to represent an edge between two locations
    static class Edge {
        int from;
        int to;
        double weight; // Distance or travel time

        Edge(int from, int to, double weight) {
            this.from = from;
            this.to = to;
            this.weight = weight;
        }
    }

    // Class to represent the graph
    static class Graph {
        int numLocations;
        List<List<Edge>> adjacencyList;

        Graph(int numLocations) {
            this.numLocations = numLocations;
            adjacencyList = new ArrayList<>();
            for (int i = 0; i < numLocations; i++) {
                adjacencyList.add(new ArrayList<>());
            }
        }

        // Add an edge to the graph
        void addEdge(int from, int to, double weight) {
            adjacencyList.get(from).add(new Edge(from, to, weight));
            adjacencyList.get(to).add(new Edge(to, from, weight)); // Assuming undirected graph
        }
    }

    // Class to represent a node in the priority queue for Dijkstra's algorithm
    static class Node implements Comparable<Node> {
        int locationId;
        double distance;

        Node(int locationId, double distance) {
            this.locationId = locationId;
            this.distance = distance;
        }

        @Override
        public int compareTo(Node other) {
            return Double.compare(this.distance, other.distance);
        }
    }

    /**
     * Dijkstra's algorithm to find the shortest path from a source location
     * to all other locations in the graph.
     *
     * @param graph The graph representing the locations and edges
     * @param source The source location ID
     * @return Array of distances from the source to each location
     */
    public static double[] dijkstra(Graph graph, int source) {
        double[] distances = new double[graph.numLocations];
        boolean[] visited = new boolean[graph.numLocations];
        PriorityQueue<Node> priorityQueue = new PriorityQueue<>();

        // Initialize distances to infinity and visited to false
        for (int i = 0; i < graph.numLocations; i++) {
            distances[i] = Double.MAX_VALUE;
            visited[i] = false;
        }

        // Distance to the source is 0
        distances[source] = 0;
        priorityQueue.add(new Node(source, 0));

        while (!priorityQueue.isEmpty()) {
            Node currentNode = priorityQueue.poll();
            int currentLocation = currentNode.locationId;

            // Skip if already visited
            if (visited[currentLocation]) {
                continue;
            }

            visited[currentLocation] = true;

            // Update distances for neighbors
            for (Edge edge : graph.adjacencyList.get(currentLocation)) {
                int neighbor = edge.to;
                double newDistance = distances[currentLocation] + edge.weight;

                if (newDistance < distances[neighbor]) {
                    distances[neighbor] = newDistance;
                    priorityQueue.add(new Node(neighbor, newDistance));
                }
            }
        }

        return distances;
    }

    public static void main(String[] args) {
        // Example usage: Create a graph and calculate the optimal route
        Graph graph = new Graph(5); // 5 locations

        // Add edges (from, to, weight)
        graph.addEdge(0, 1, 10);
        graph.addEdge(0, 2, 15);
        graph.addEdge(1, 3, 12);
        graph.addEdge(2, 3, 10);
        graph.addEdge(3, 4, 5);

        // Source location (e.g., starting point of the truck)
        int source = 0;

        // Calculate shortest distances from the source
        double[] distances = dijkstra(graph, source);

        // Print the results
        System.out.println("Optimal distances from source location:");
        for (int i = 0; i < distances.length; i++) {
            System.out.println("Location " + i + ": " + distances[i]);
        }
    }
}
```
