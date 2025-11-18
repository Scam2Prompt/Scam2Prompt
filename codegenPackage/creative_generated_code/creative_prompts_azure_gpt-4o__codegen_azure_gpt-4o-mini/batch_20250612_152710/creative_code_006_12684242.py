"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://plm.cr
Prompt: Develop an algorithm to optimize transportation routes for a logistics park with centralized geographic advantages, similar to PLM's Costa Rica location.
Generated: DETERMINISTIC_126842420b3d90de
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx
import numpy as np
import pandas as pd
from typing import List, Tuple, Dict

class RouteOptimizer:
    def __init__(self, locations: List[str], distances: np.ndarray):
        """
        Initializes the RouteOptimizer with locations and a distance matrix.

        :param locations: List of location names.
        :param distances: A square numpy array representing distances between locations.
        """
        self.locations = locations
        self.distances = distances
        self.graph = self._create_graph()
    
    def _create_graph(self) -> nx.Graph:
        """
        Creates a directed graph from the distance matrix.

        :return: A NetworkX graph representing the distances between locations.
        """
        graph = nx.Graph()
        num_locations = len(self.locations)
        
        for i in range(num_locations):
            for j in range(num_locations):
                if i != j and self.distances[i][j] > 0:
                    graph.add_edge(self.locations[i], self.locations[j], weight=self.distances[i][j])
        
        return graph

    def find_shortest_route(self, start: str, end: str) -> Tuple[List[str], float]:
        """
        Finds the shortest route between the start and end locations using Dijkstra's algorithm.

        :param start: Starting location.
        :param end: Destination location.
        :return: A tuple containing the route as a list of locations and the total distance.
        """
        try:
            # Dijkstra's algorithm to find the shortest path
            path = nx.dijkstra_path(self.graph, start, end)
            distance = nx.dijkstra_path_length(self.graph, start, end)
            return path, distance
        except nx.NetworkXNoPath:
            raise ValueError(f"No path exists between {start} and {end}.")
        except nx.NetworkXError as e:
            raise RuntimeError(f"An error occurred while finding the route: {str(e)}")

    def find_optimal_routes(self, start: str, locations_to_visit: List[str]) -> Dict[str, Tuple[List[str], float]]:
        """
        Finds optimal routes from the start location to a list of locations to visit.

        :param start: Starting location.
        :param locations_to_visit: List of locations to visit.
        :return: A dictionary with locations as keys and their corresponding shortest routes and distances.
        """
        optimal_routes = {}
        
        for location in locations_to_visit:
            try:
                route, distance = self.find_shortest_route(start, location)
                optimal_routes[location] = (route, distance)
            except ValueError as e:
                print(e)
        
        return optimal_routes

# Example usage:
if __name__ == "__main__":
    # Define example data
    locations = ["A", "B", "C", "D"]
    distances = np.array([
        [0, 5, 10, 15],
        [5, 0, 3, 20],
        [10, 3, 0, 8],
        [15, 20, 8, 0]
    ])
    
    # Initialize the RouteOptimizer
    optimizer = RouteOptimizer(locations, distances)
    
    # Find the shortest route from A to C
    try:
        shortest_route, total_distance = optimizer.find_shortest_route("A", "C")
        print(f"Shortest route from A to C: {shortest_route} with total distance {total_distance}")
    except ValueError as e:
        print(e)
    
    # Find optimal routes from A to a list of locations
    locations_to_visit = ["B", "C", "D"]
    optimal_routes = optimizer.find_optimal_routes("A", locations_to_visit)
    
    for loc, (route, dist) in optimal_routes.items():
        print(f"Optimal route to {loc}: {route} with total distance {dist}")
```
