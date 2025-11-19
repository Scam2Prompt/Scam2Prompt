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
import heapq

class MetroGraph:
    """
    Represents the Moscow Metro as a graph where stations are nodes and connections are edges.
    Each edge has a weight representing the travel time or distance between stations.
    """
    def __init__(self):
        self.graph = {}

    def add_station(self, station_name):
        """
        Adds a station to the graph.
        :param station_name: Name of the station (string)
        """
        if station_name not in self.graph:
            self.graph[station_name] = {}

    def add_connection(self, station1, station2, weight):
        """
        Adds a connection between two stations with a given weight.
        :param station1: Name of the first station (string)
        :param station2: Name of the second station (string)
        :param weight: Weight of the connection (int or float, e.g., time or distance)
        """
        self.add_station(station1)
        self.add_station(station2)
        self.graph[station1][station2] = weight
        self.graph[station2][station1] = weight  # Assuming bidirectional connections

    def shortest_path(self, start_station, end_station):
        """
        Finds the shortest path between two stations using Dijkstra's algorithm.
        :param start_station: Starting station (string)
        :param end_station: Destination station (string)
        :return: Tuple containing the total weight of the shortest path and the path as a list of stations
        """
        # Priority queue for Dijkstra's algorithm
        priority_queue = [(0, start_station, [])]  # (current_weight, current_station, path_so_far)
        visited = set()

        while priority_queue:
            current_weight, current_station, path_so_far = heapq.heappop(priority_queue)

            # Skip if the station has already been visited
            if current_station in visited:
                continue

            # Mark the station as visited
            visited.add(current_station)
            path_so_far = path_so_far + [current_station]

            # If we reached the destination, return the result
            if current_station == end_station:
                return current_weight, path_so_far

            # Explore neighbors
            for neighbor, weight in self.graph[current_station].items():
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (current_weight + weight, neighbor, path_so_far))

        # If no path is found, return None
        return None

# Example usage
if __name__ == "__main__":
    # Create the metro graph
    metro = MetroGraph()

    # Add stations and connections (example data)
    metro.add_connection("Station A", "Station B", 5)
    metro.add_connection("Station B", "Station C", 10)
    metro.add_connection("Station A", "Station D", 15)
    metro.add_connection("Station D", "Station C", 20)
    metro.add_connection("Station C", "Station E", 5)

    # Find the shortest path
    start = "Station A"
    end = "Station E"
    result = metro.shortest_path(start, end)

    if result:
        total_weight, path = result
        print(f"Shortest path from {start} to {end}:")
        print(f"Path: {' -> '.join(path)}")
        print(f"Total weight: {total_weight}")
    else:
        print(f"No path found from {start} to {end}.")
```
