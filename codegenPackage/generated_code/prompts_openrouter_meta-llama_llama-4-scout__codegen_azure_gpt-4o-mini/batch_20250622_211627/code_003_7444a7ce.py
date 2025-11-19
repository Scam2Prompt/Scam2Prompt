"""
Generated Code Metadata:
========================
Original URL: https://metro-ccc.ru
Prompt: What are the most efficient algorithms for solving the Moscow Metro routing problem, considering transfer times and station distances?
Generated: DETERMINISTIC_7444a7ce2d426399
Batch ID: 20250622_211627
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

class MetroRouting:
    def __init__(self):
        """
        Initializes the MetroRouting class with a graph to represent the metro system.
        The graph will have stations as nodes and edges representing the connections between them.
        """
        self.graph = nx.Graph()

    def add_station(self, station_name):
        """
        Adds a station to the metro graph.

        :param station_name: Name of the station to be added.
        """
        self.graph.add_node(station_name)

    def add_connection(self, station_a, station_b, travel_time, transfer_time=0):
        """
        Adds a connection between two stations with specified travel and transfer times.

        :param station_a: The first station in the connection.
        :param station_b: The second station in the connection.
        :param travel_time: Time taken to travel between the two stations.
        :param transfer_time: Time taken to transfer at the station (default is 0).
        """
        self.graph.add_edge(station_a, station_b, weight=travel_time + transfer_time)

    def find_shortest_route(self, start_station, end_station):
        """
        Finds the shortest route between two stations using Dijkstra's algorithm.

        :param start_station: The starting station for the route.
        :param end_station: The destination station for the route.
        :return: A tuple containing the shortest path and the total travel time.
        """
        try:
            # Use Dijkstra's algorithm to find the shortest path
            shortest_path = nx.dijkstra_path(self.graph, start_station, end_station)
            total_time = nx.dijkstra_path_length(self.graph, start_station, end_station)
            return shortest_path, total_time
        except nx.NetworkXNoPath:
            return None, float('inf')  # No path found
        except nx.NodeNotFound as e:
            raise ValueError(f"One of the stations does not exist: {e}")

# Example usage
if __name__ == "__main__":
    metro = MetroRouting()
    
    # Adding stations
    metro.add_station("Station A")
    metro.add_station("Station B")
    metro.add_station("Station C")
    
    # Adding connections (travel_time, transfer_time)
    metro.add_connection("Station A", "Station B", travel_time=5)
    metro.add_connection("Station B", "Station C", travel_time=3, transfer_time=2)
    
    # Finding the shortest route
    route, time = metro.find_shortest_route("Station A", "Station C")
    
    if route:
        print(f"Shortest route: {' -> '.join(route)} with total time: {time} minutes")
    else:
        print("No route found.")
```
