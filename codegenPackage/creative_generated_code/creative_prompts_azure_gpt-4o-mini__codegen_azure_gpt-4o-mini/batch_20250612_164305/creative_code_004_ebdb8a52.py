"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://atlasnavi.pages.dev
Prompt: Create a function that calculates the most efficient multi-stop route for a navigation app, taking cues from Atlas Navi's routing algorithms.
Generated: DETERMINISTIC_ebdb8a52654bbe56
Batch ID: 20250612_164305
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import itertools
from typing import List, Tuple, Dict

class RouteOptimizer:
    def __init__(self, graph: Dict[str, Dict[str, float]]):
        """
        Initializes the RouteOptimizer with a graph representation of the roads.
        
        :param graph: A dictionary where keys are node names, and values are dictionaries
                      with neighboring node names as keys and distances as values.
        """
        self.graph = graph

    def calculate_route_distance(self, route: List[str]) -> float:
        """
        Calculates the total distance of a given route.
        
        :param route: A list of nodes representing the route.
        :return: The total distance of the route.
        """
        distance = 0.0
        for i in range(len(route) - 1):
            from_node = route[i]
            to_node = route[i + 1]
            # Check for direct route between nodes
            if to_node in self.graph.get(from_node, {}):
                distance += self.graph[from_node][to_node]
            else:
                raise ValueError(f"No route between {from_node} and {to_node}.")
        return distance

    def find_optimal_route(self, start: str, stops: List[str]) -> Tuple[List[str], float]:
        """
        Finds the most efficient route visiting all specified stops starting from a given node.
        
        :param start: The starting node for the route.
        :param stops: A list of nodes to visit.
        :return: A tuple containing the optimal route and its total distance.
        """
        # Generate all permutations of the stops
        min_distance = float('inf')
        optimal_route = []
        
        for perm in itertools.permutations(stops):
            # Create a full route including start and end at the starting point
            current_route = [start] + list(perm) + [start]
            try:
                current_distance = self.calculate_route_distance(current_route)
                if current_distance < min_distance:
                    min_distance = current_distance
                    optimal_route = current_route
            except ValueError as e:
                # Skip this permutation if a route is not available
                continue
        
        if not optimal_route:
            raise RuntimeError("No valid route found for the given stops.")
        
        return optimal_route, min_distance

# Example usage
if __name__ == "__main__":
    # Define a simple graph with distances
    road_graph = {
        'A': {'B': 10, 'C': 15},
        'B': {'A': 10, 'C': 35, 'D': 25},
        'C': {'A': 15, 'B': 35, 'D': 30},
        'D': {'B': 25, 'C': 30}
    }
    
    optimizer = RouteOptimizer(road_graph)
    
    try:
        route, distance = optimizer.find_optimal_route('A', ['B', 'C', 'D'])
        print(f"Optimal Route: {route}, Total Distance: {distance}")
    except (RuntimeError, ValueError) as e:
        print(f"Error occurred: {e}")
```
