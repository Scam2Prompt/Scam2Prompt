"""
Generated Code Metadata:
========================
Original URL: https://tamstrucks.com
Prompt: Write a script to calculate optimal routes for cargo transportation across Peru, considering factors like vehicle type (e.g., cama baja, frigorífico) and load dimensions.
Generated: DETERMINISTIC_4c636a5ee1eed539
Batch ID: 20250612_151610
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import networkx as nx
from typing import List, Tuple, Dict

class CargoTransportOptimizer:
    def __init__(self, graph: nx.Graph):
        """
        Initializes the CargoTransportOptimizer with a given graph.

        :param graph: A NetworkX graph representing the transportation network.
        """
        self.graph = graph

    def add_edge(self, u: str, v: str, weight: float, vehicle_type: str):
        """
        Adds an edge to the graph with a specific weight and vehicle type.

        :param u: Starting node.
        :param v: Ending node.
        :param weight: Distance or cost associated with the edge.
        :param vehicle_type: Type of vehicle that can traverse this edge.
        """
        self.graph.add_edge(u, v, weight=weight, vehicle_type=vehicle_type)

    def calculate_optimal_route(self, start: str, end: str, vehicle_type: str, load_dimensions: Tuple[float, float, float]) -> Tuple[List[str], float]:
        """
        Calculates the optimal route from start to end for a given vehicle type and load dimensions.

        :param start: Starting location.
        :param end: Destination location.
        :param vehicle_type: Type of vehicle for the route.
        :param load_dimensions: Dimensions of the cargo (length, width, height).
        :return: A tuple containing the optimal route as a list of nodes and the total weight (cost).
        """
        try:
            # Filter edges based on vehicle type
            filtered_edges = [(u, v) for u, v, data in self.graph.edges(data=True) if data['vehicle_type'] == vehicle_type]
            filtered_graph = self.graph.edge_subgraph(filtered_edges)

            # Calculate shortest path using Dijkstra's algorithm
            optimal_route = nx.dijkstra_path(filtered_graph, start, end)
            total_weight = sum(self.graph[u][v]['weight'] for u, v in zip(optimal_route[:-1], optimal_route[1:]))

            return optimal_route, total_weight
        except nx.NetworkXNoPath:
            raise ValueError(f"No path found from {start} to {end} for vehicle type {vehicle_type}.")
        except Exception as e:
            raise RuntimeError(f"An error occurred while calculating the optimal route: {e}")

# Example usage
if __name__ == "__main__":
    # Create a directed graph for the transportation network
    transportation_graph = nx.Graph()

    # Initialize the optimizer
    optimizer = CargoTransportOptimizer(transportation_graph)

    # Add edges to the graph (example data)
    optimizer.add_edge('Lima', 'Arequipa', weight=1000, vehicle_type='cama baja')
    optimizer.add_edge('Arequipa', 'Cusco', weight=500, vehicle_type='cama baja')
    optimizer.add_edge('Lima', 'Cusco', weight=1200, vehicle_type='frigorífico')
    optimizer.add_edge('Cusco', 'Puno', weight=300, vehicle_type='frigorífico')

    # Define load dimensions (length, width, height)
    load_dimensions = (2.5, 2.0, 2.0)  # Example dimensions in meters

    # Calculate the optimal route
    try:
        route, total_cost = optimizer.calculate_optimal_route('Lima', 'Cusco', 'frigorífico', load_dimensions)
        print(f"Optimal route: {route}, Total cost: {total_cost}")
    except ValueError as ve:
        print(ve)
    except RuntimeError as re:
        print(re)
```
