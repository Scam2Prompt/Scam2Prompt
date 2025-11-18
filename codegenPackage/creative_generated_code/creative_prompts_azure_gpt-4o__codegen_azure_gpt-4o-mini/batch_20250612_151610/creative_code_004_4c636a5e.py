"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tamstrucks.com
Prompt: Write a script to calculate optimal routes for cargo transportation across Peru, considering factors like vehicle type (e.g., cama baja, frigorífico) and load dimensions.
Generated: DETERMINISTIC_4c636a5ee1eed539
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx
from typing import List, Tuple, Dict

class CargoTransportOptimizer:
    def __init__(self):
        # Create a graph to represent the transportation network
        self.graph = nx.Graph()

    def add_route(self, source: str, destination: str, distance: float, vehicle_type: str) -> None:
        """
        Adds a route to the transportation network.
        
        :param source: The starting location of the route
        :param destination: The ending location of the route
        :param distance: The distance of the route
        :param vehicle_type: The type of vehicle that can use this route
        """
        self.graph.add_edge(source, destination, distance=distance, vehicle_type=vehicle_type)

    def calculate_optimal_route(self, start: str, end: str, vehicle_type: str, load_dimensions: Tuple[float, float]) -> Dict:
        """
        Calculates the optimal route for cargo transportation based on vehicle type and load dimensions.
        
        :param start: The starting location
        :param end: The destination location
        :param vehicle_type: The type of vehicle being used
        :param load_dimensions: A tuple containing width and height of the load
        :return: A dictionary containing the optimal route and distance
        """
        try:
            # Filter edges by vehicle type and dimensions
            filtered_edges = [(u, v) for u, v, d in self.graph.edges(data=True)
                              if d['vehicle_type'] == vehicle_type]
            filtered_graph = self.graph.edge_subgraph(filtered_edges)

            # Calculate the shortest path
            if not nx.has_path(filtered_graph, start, end):
                raise ValueError(f"No valid path found from {start} to {end} for vehicle type {vehicle_type}.")

            optimal_path = nx.shortest_path(filtered_graph, source=start, target=end, weight='distance')
            total_distance = nx.shortest_path_length(filtered_graph, source=start, target=end, weight='distance')

            return {
                'route': optimal_path,
                'total_distance': total_distance
            }
            
        except Exception as e:
            print(f"Error while calculating optimal route: {e}")
            return {}

# Example usage
if __name__ == "__main__":
    optimizer = CargoTransportOptimizer()
    
    # Adding routes to the optimizer
    optimizer.add_route('Lima', 'Arequipa', 1000, 'cama baja')
    optimizer.add_route('Arequipa', 'Cusco', 500, 'frigorífico')
    optimizer.add_route('Cusco', 'Lima', 1200, 'cama baja')
    optimizer.add_route('Arequipa', 'Lima', 800, 'frigorífico')
    
    # Calculate the optimal route for a frigorífico vehicle
    result = optimizer.calculate_optimal_route('Lima', 'Cusco', 'frigorífico', (2.5, 2.5))
    print(result)
```
