"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Write a function in Python to calculate the optimal routes for recycling collection trucks within the City of York, minimizing fuel consumption and time.
Generated: DETERMINISTIC_9a32b6c89264c9ef
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx
from typing import List, Tuple

class RecyclingRouteOptimizer:
    def __init__(self, graph: nx.Graph):
        """
        Initializes the RecyclingRouteOptimizer with a graph representing the city.

        :param graph: A networkx Graph representing the streets and distances of the city.
        """
        if not isinstance(graph, nx.Graph):
            raise ValueError("The provided graph must be a networkx Graph.")
        self.graph = graph

    def calculate_optimal_route(self, start: str, locations: List[str]) -> Tuple[List[str], float]:
        """
        Calculates the optimal route for recycling collection trucks.

        :param start: The starting point for the route.
        :param locations: A list of locations to visit.
        :return: A tuple containing the optimal route as a list of locations and the total distance.
        """
        if start not in self.graph:
            raise ValueError(f"Start location '{start}' is not in the graph.")
        for location in locations:
            if location not in self.graph:
                raise ValueError(f"Location '{location}' is not in the graph.")

        # Initialize the best route and minimum distance
        best_route = []
        min_distance = float('inf')

        # Generate all permutations of the locations to find the optimal route
        from itertools import permutations
        for perm in permutations(locations):
            # Calculate the total distance for the current permutation
            total_distance = self.calculate_total_distance(start, perm)

            # Update best route if the current one is shorter
            if total_distance < min_distance:
                min_distance = total_distance
                best_route = [start] + list(perm)

        return best_route, min_distance

    def calculate_total_distance(self, start: str, route: List[str]) -> float:
        """
        Calculates the total distance of a given route.

        :param start: The starting point of the route.
        :param route: The route as a list of locations.
        :return: The total distance of the route.
        """
        total_distance = 0.0
        current_location = start

        for next_location in route:
            try:
                distance = self.graph[current_location][next_location]['weight']
                total_distance += distance
                current_location = next_location
            except KeyError:
                raise ValueError(f"No path exists between {current_location} and {next_location}.")

        return total_distance

# Example Usage
if __name__ == "__main__":
    # Create a graph representing the City of York streets and distances
    G = nx.Graph()
    # Add edges with weights representing distances (in kilometers)
    G.add_edge('A', 'B', weight=5)
    G.add_edge('A', 'C', weight=10)
    G.add_edge('B', 'C', weight=2)
    G.add_edge('B', 'D', weight=3)
    G.add_edge('C', 'D', weight=1)

    # Instantiate the optimizer
    optimizer = RecyclingRouteOptimizer(G)

    # Calculate the optimal route starting from 'A' and visiting 'B', 'C', 'D'
    try:
        route, distance = optimizer.calculate_optimal_route('A', ['B', 'C', 'D'])
        print(f"Optimal route: {route} with total distance: {distance} km")
    except ValueError as e:
        print(f"Error: {e}")
```
