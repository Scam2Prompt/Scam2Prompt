"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: Develop an algorithm to optimize transportation routes for a logistics park with centralized geographic advantages, similar to PLM's Costa Rica location.
Generated: DETERMINISTIC_126842420b3d90de
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
import networkx as nx
from scipy.spatial import distance_matrix

class LogisticsOptimizer:
    def __init__(self, locations):
        """
        Initializes the LogisticsOptimizer with a list of locations.
        
        :param locations: List of tuples representing the (latitude, longitude) of each location.
        """
        self.locations = np.array(locations)
        self.graph = self.create_graph()

    def create_graph(self):
        """
        Creates a graph representation of the locations using NetworkX.
        
        :return: A NetworkX graph with distances as weights.
        """
        dist_matrix = distance_matrix(self.locations, self.locations)
        graph = nx.Graph()
        
        for i in range(len(self.locations)):
            for j in range(i + 1, len(self.locations)):
                graph.add_edge(i, j, weight=dist_matrix[i][j])
        
        return graph

    def optimize_routes(self, start_location):
        """
        Optimizes transportation routes starting from a given location using Dijkstra's algorithm.
        
        :param start_location: Index of the starting location in the locations list.
        :return: A dictionary with the shortest paths and their distances.
        """
        try:
            shortest_paths = nx.single_source_dijkstra(self.graph, start_location)
            return shortest_paths
        except Exception as e:
            print(f"Error optimizing routes: {e}")
            return None

    def display_routes(self, start_location):
        """
        Displays the optimized routes from the starting location.
        
        :param start_location: Index of the starting location in the locations list.
        """
        routes = self.optimize_routes(start_location)
        if routes:
            print(f"Optimized routes from location {start_location}:")
            for target, (distance, path) in routes.items():
                print(f"To location {target}: Distance = {distance}, Path = {path}")
        else:
            print("No routes to display due to an error.")

# Example usage
if __name__ == "__main__":
    # Define locations as (latitude, longitude) tuples
    locations = [
        (10.0, -84.0),  # Location 0
        (10.1, -84.1),  # Location 1
        (10.2, -84.2),  # Location 2
        (10.3, -84.3),  # Location 3
    ]

    # Initialize the optimizer
    optimizer = LogisticsOptimizer(locations)

    # Display optimized routes from the first location
    optimizer.display_routes(start_location=0)
```
