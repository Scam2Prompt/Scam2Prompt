"""
Generated Code Metadata:
========================
Original URL: https://waldoenruta.com
Prompt: Design a route planning algorithm for Waldo Correa's future bicycle travels in Chile, taking into account factors like terrain difficulty, road conditions, and scenic stops.
Generated: DETERMINISTIC_6a73e117e69df1f6
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import networkx as nx
import numpy as np
from typing import List, Tuple, Dict

class RoutePlanner:
    def __init__(self):
        # Initialize a directed graph to represent the road network
        self.graph = nx.DiGraph()

    def add_route(self, start: str, end: str, distance: float, terrain_difficulty: float, road_condition: float, scenic_value: float):
        """
        Add a route to the graph with associated attributes.
        
        :param start: Starting point of the route
        :param end: Ending point of the route
        :param distance: Distance of the route in kilometers
        :param terrain_difficulty: Difficulty of the terrain (scale 1-10)
        :param road_condition: Condition of the road (scale 1-10)
        :param scenic_value: Scenic value of the route (scale 1-10)
        """
        self.graph.add_edge(start, end, distance=distance, terrain_difficulty=terrain_difficulty,
                             road_condition=road_condition, scenic_value=scenic_value)

    def calculate_route_score(self, route: List[str]) -> float:
        """
        Calculate a score for a given route based on its attributes.
        
        :param route: List of points representing the route
        :return: Calculated score for the route
        """
        score = 0
        for i in range(len(route) - 1):
            edge_data = self.graph[route[i]][route[i + 1]]
            # Score calculation based on attributes
            score += (10 - edge_data['terrain_difficulty']) + edge_data['road_condition'] + edge_data['scenic_value']
        return score

    def find_best_route(self, start: str, end: str) -> Tuple[List[str], float]:
        """
        Find the best route from start to end based on the highest score.
        
        :param start: Starting point
        :param end: Ending point
        :return: Tuple containing the best route and its score
        """
        try:
            # Get all paths from start to end
            all_paths = list(nx.all_simple_paths(self.graph, source=start, target=end))
            best_route = []
            best_score = float('-inf')

            for path in all_paths:
                score = self.calculate_route_score(path)
                if score > best_score:
                    best_score = score
                    best_route = path

            if not best_route:
                raise ValueError("No route found from {} to {}".format(start, end))

            return best_route, best_score

        except Exception as e:
            print(f"Error finding best route: {e}")
            return [], 0.0

# Example usage
if __name__ == "__main__":
    planner = RoutePlanner()
    
    # Adding routes (example data)
    planner.add_route("Santiago", "Valparaiso", 120, 5, 8, 9)
    planner.add_route("Santiago", "Rancagua", 90, 4, 7, 6)
    planner.add_route("Rancagua", "Valparaiso", 100, 6, 6, 8)
    planner.add_route("Valparaiso", "La Serena", 400, 7, 5, 10)

    # Finding the best route
    best_route, best_score = planner.find_best_route("Santiago", "Valparaiso")
    print(f"Best route: {best_route} with score: {best_score}")
```
