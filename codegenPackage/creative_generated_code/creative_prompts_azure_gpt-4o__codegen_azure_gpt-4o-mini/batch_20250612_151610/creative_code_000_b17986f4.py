"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://portlineshipping.com
Prompt: Write Python code to calculate optimal shipping routes for land transport within Pakistan, considering the quality of roads and driving distances mentioned on Portline Shipping's website.
Generated: DETERMINISTIC_b17986f4eb57761d
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
import pandas as pd
from typing import List, Tuple, Dict

class ShippingRouteOptimizer:
    def __init__(self, road_data: pd.DataFrame):
        """
        Initialize the ShippingRouteOptimizer with road data.

        :param road_data: DataFrame containing road quality and distances.
        """
        self.graph = nx.Graph()
        self._create_graph(road_data)

    def _create_graph(self, road_data: pd.DataFrame):
        """
        Create a graph from the road data.

        :param road_data: DataFrame containing road quality and distances.
        """
        for _, row in road_data.iterrows():
            source = row['source']
            destination = row['destination']
            distance = row['distance']
            quality = row['quality']

            # Add edges to the graph considering quality (lower is better)
            if quality < 5:  # Assuming quality is on a scale of 1-10
                self.graph.add_edge(source, destination, weight=distance)

    def find_optimal_route(self, start: str, end: str) -> Tuple[List[str], float]:
        """
        Find the optimal shipping route from start to end.

        :param start: The starting location.
        :param end: The destination location.
        :return: A tuple containing the optimal route and the total distance.
        """
        try:
            # Calculate the shortest path based on distance
            optimal_route = nx.shortest_path(self.graph, source=start, target=end, weight='weight')
            total_distance = nx.shortest_path_length(self.graph, source=start, target=end, weight='weight')
            return optimal_route, total_distance
        except nx.NetworkXNoPath:
            raise ValueError(f"No path exists between {start} and {end}.")
        except nx.NodeNotFound as e:
            raise ValueError(f"Node not found: {str(e)}")
        except Exception as e:
            raise RuntimeError(f"An error occurred while finding the optimal route: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Sample road data
    road_data_dict = {
        'source': ['A', 'A', 'B', 'C', 'C'],
        'destination': ['B', 'C', 'D', 'D', 'E'],
        'distance': [5, 10, 2, 1, 7],
        'quality': [4, 6, 3, 2, 5]  # Quality scale from 1 (best) to 10 (worst)
    }
    
    road_data = pd.DataFrame(road_data_dict)

    # Initialize the optimizer
    optimizer = ShippingRouteOptimizer(road_data)

    # Find an optimal route
    try:
        route, distance = optimizer.find_optimal_route('A', 'D')
        print(f"Optimal route from A to D: {route} with total distance: {distance}")
    except ValueError as ve:
        print(ve)
    except RuntimeError as re:
        print(re)
```

This code defines a `ShippingRouteOptimizer` class that utilizes the NetworkX library to compute optimal shipping routes based on provided road data. It includes proper error handling and is structured to be production-ready.
