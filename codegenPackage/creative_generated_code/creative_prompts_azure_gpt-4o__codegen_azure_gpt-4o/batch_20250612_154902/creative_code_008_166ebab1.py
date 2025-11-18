"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniair.id
Prompt: Write a script to calculate the optimal route for trucking and distribution logistics, incorporating Uniair Cargo's domestic and international networks.
Generated: DETERMINISTIC_166ebab1611ecba9
Batch ID: 20250612_154902
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

Here is a Python script to calculate the optimal route for trucking and distribution logistics using Uniair Cargo's domestic and international networks:

```python
import networkx as nx
import json
from typing import List, Tuple

class LogisticsRouteOptimizer:
    """
    A class to calculate the optimal route for trucking and distribution logistics
    using Uniair Cargo's domestic and international networks.
    """

    def __init__(self):
        """
        Initializes the logistics optimizer with an empty graph.
        """
        self.graph = nx.DiGraph()

    def add_route(self, source: str, destination: str, distance: float, cost: float):
        """
        Adds a route to the logistics network.

        :param source: Starting location of the route.
        :param destination: Destination location of the route.
        :param distance: Distance between source and destination in kilometers.
        :param cost: Transportation cost for the route.
        """
        self.graph.add_edge(source, destination, distance=distance, cost=cost)

    def load_network(self, network_data: List[Tuple[str, str, float, float]]):
        """
        Loads the logistics network from given data.

        :param network_data: A list of tuples containing (source, destination, distance, cost).
        """
        for source, destination, distance, cost in network_data:
            self.add_route(source, destination, distance, cost)

    def find_optimal_route(self, start: str, end: str, optimization_metric: str = "cost"):
        """
        Finds the optimal route between start and end locations based on the given metric.

        :param start: Starting location.
        :param end: Destination location.
        :param optimization_metric: Metric to optimize (either 'cost' or 'distance').
        :return: Optimal route and its total metric value.
        """
        if optimization_metric not in {"cost", "distance"}:
            raise ValueError("Invalid optimization metric. Must be 'cost' or 'distance'.")
        
        try:
            path = nx.shortest_path(self.graph, source=start, target=end, weight=optimization_metric)
            total_metric = nx.shortest_path_length(self.graph, source=start, target=end, weight=optimization_metric)
            return path, total_metric
        except nx.NetworkXNoPath:
            raise ValueError(f"No path found between '{start}' and '{end}' in the network.")

def main():
    """
    Main function to demonstrate the LogisticsRouteOptimizer functionality.
    """
    # Sample data for Uniair Cargo's network (source, destination, distance in km, cost in USD)
    network_data = [
        ("New York", "Chicago", 1200, 500),
        ("Chicago", "Houston", 1500, 600),
        ("Houston", "Los Angeles", 2200, 800),
        ("New York", "Toronto", 800, 300),
        ("Toronto", "Los Angeles", 3500, 1200),
        ("Los Angeles", "Sydney", 12000, 4500),
        ("New York", "London", 5600, 2000),
        ("London", "Sydney", 17000, 6500),
    ]

    optimizer = LogisticsRouteOptimizer()
    optimizer.load_network(network_data)

    # Ask for user input to find routes
    start = input("Enter starting location: ")
    end = input("Enter destination location: ")
    metric = input("Optimize by (cost/distance): ").strip().lower()

    try:
        route, metric_value = optimizer.find_optimal_route(start, end, metric)
        print(f"Optimal route from '{start}' to '{end}': {route}")
        print(f"Total {metric}: {metric_value}")
    except ValueError as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()
```

### Notes on the code:
1. **Dependencies**: The script uses the `networkx` library to create a directed graph representing the logistics network and calculate optimal routes.
2. **Error Handling**: Proper error handling is implemented for invalid inputs and scenarios where no path exists.
3. **Modular Design**: The code is designed to be modular, reusable, and extendable.
4. **Data Loading**: Sample data is included for demonstration, but this can be replaced with real data from Uniair Cargo's logistics network.
