"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Write a program to optimize trucking and distribution routes within Indonesia, using Uniair Cargo’s domestic network capabilities.
Generated: DETERMINISTIC_1da3318a23fcc7e5
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx
import pandas as pd
from typing import List, Dict, Tuple

class TruckingOptimizer:
    def __init__(self, routes: List[Tuple[str, str, float]]):
        """
        Initialize the TruckingOptimizer with route data.
        
        :param routes: A list of tuples containing (source, destination, distance)
        """
        self.graph = nx.DiGraph()  # Create a directed graph for routes
        
        for source, destination, distance in routes:
            # Add edge with distance as weight
            self.graph.add_edge(source, destination, weight=distance)

    def find_optimal_route(self, start: str, end: str) -> Tuple[List[str], float]:
        """
        Find the optimal route from start to end using Dijkstra's algorithm.
        
        :param start: Starting location
        :param end: Ending location
        :return: A tuple containing the optimal route and its total distance
        """
        try:
            # Use Dijkstra's algorithm to find the shortest path
            optimal_route = nx.dijkstra_path(self.graph, start, end)
            total_distance = nx.dijkstra_path_length(self.graph, start, end)
            return optimal_route, total_distance
        except nx.NetworkXNoPath:
            raise ValueError(f"No path exists from {start} to {end}.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while finding the optimal route: {str(e)}")

    def get_all_routes(self) -> Dict[str, List[str]]:
        """
        Get all possible routes and their corresponding distances.
        
        :return: A dictionary with starting locations as keys and a list of possible routes as values
        """
        routes_info = {}
        for source in self.graph.nodes:
            routes_info[source] = []
            for destination in self.graph.successors(source):
                distance = self.graph[source][destination]['weight']
                routes_info[source].append((destination, distance))
        return routes_info

# Sample route data for demonstration purposes
routes_data = [
    ('Jakarta', 'Surabaya', 780),
    ('Jakarta', 'Bandung', 150),
    ('Bandung', 'Surabaya', 650),
    ('Surabaya', 'Bali', 300),
    ('Jakarta', 'Bali', 1200),
]

if __name__ == "__main__":
    # Create an instance of TruckingOptimizer
    optimizer = TruckingOptimizer(routes_data)

    # Find the optimal route
    try:
        route, distance = optimizer.find_optimal_route('Jakarta', 'Surabaya')
        print(f"Optimal Route: {route} with Distance: {distance} km")
    except ValueError as ve:
        print(ve)
    except RuntimeError as re:
        print(re)

    # Get and print all routes
    all_routes = optimizer.get_all_routes()
    print("All Possible Routes:")
    for start, routes in all_routes.items():
        print(f"{start}: {routes}")
```
