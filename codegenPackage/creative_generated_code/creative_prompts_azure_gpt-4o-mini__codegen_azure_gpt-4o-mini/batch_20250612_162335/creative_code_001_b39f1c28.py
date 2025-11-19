"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stelllar.org
Prompt: Write a function that calculates the optimal shipping route based on the services offered by Stelllar Logistics.
Generated: DETERMINISTIC_b39f1c282106f7fe
Batch ID: 20250612_162335
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx
from typing import List, Dict, Tuple, Any

class ShippingRouteOptimizer:
    def __init__(self, services: Dict[str, List[Tuple[str, float]]]) -> None:
        """
        Initializes the ShippingRouteOptimizer with the services provided by Stellar Logistics.

        :param services: A dictionary where keys are service names and values are lists of tuples
                         containing destination and cost.
        """
        self.services = services
        self.graph = self._build_graph()

    def _build_graph(self) -> nx.DiGraph:
        """
        Builds a directed graph from the services dictionary.

        :return: A directed graph with nodes representing locations and edges representing costs.
        """
        graph = nx.DiGraph()
        for service, routes in self.services.items():
            for destination, cost in routes:
                graph.add_edge(service, destination, weight=cost)
        return graph

    def calculate_optimal_route(self, start: str, end: str) -> Tuple[List[str], float]:
        """
        Calculates the optimal shipping route from start to end using Dijkstra's algorithm.

        :param start: The starting location.
        :param end: The destination location.
        :return: A tuple containing the optimal route as a list of locations and the total cost.
        """
        try:
            # Calculate the shortest path using Dijkstra's algorithm
            optimal_route = nx.dijkstra_path(self.graph, start, end)
            total_cost = nx.path_weight(self.graph, optimal_route, weight='weight')
            return optimal_route, total_cost
        except nx.NetworkXNoPath:
            raise ValueError(f"No path found from {start} to {end}.")
        except nx.NodeNotFound as e:
            raise ValueError(f"Node not found: {e}.")
        except Exception as e:
            raise RuntimeError(f"An unexpected error occurred: {e}.")

# Example usage
if __name__ == "__main__":
    services = {
        'Warehouse_A': [('Warehouse_B', 5), ('Warehouse_C', 10)],
        'Warehouse_B': [('Warehouse_C', 2), ('Warehouse_D', 6)],
        'Warehouse_C': [('Warehouse_D', 4)],
        'Warehouse_D': []
    }

    optimizer = ShippingRouteOptimizer(services)
    try:
        route, cost = optimizer.calculate_optimal_route('Warehouse_A', 'Warehouse_D')
        print(f"Optimal route: {route} with total cost: {cost}")
    except ValueError as e:
        print(e)
    except RuntimeError as e:
        print(e)
```
