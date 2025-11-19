"""
Generated Code Metadata:
========================
Original URL: https://tramsipublicidad.com
Prompt: Design a route planning algorithm for a tram system that incorporates efficient trip mapping and seamless travel experiences.
Generated: DETERMINISTIC_031d14284f57003f
Batch ID: 20250622_204740
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq
from typing import Dict, List, Tuple

class TramRoutePlanner:
    def __init__(self, graph: Dict[str, Dict[str, int]]):
        """
        Initialize the TramRoutePlanner with a graph representing the tram network.

        Args:
        graph: A dictionary representing the tram network, where each key is a station
               and its corresponding value is another dictionary. The inner dictionary's
               keys are the neighboring stations and its values are the travel times.
        """
        self.graph = graph

    def plan_route(self, start: str, end: str) -> Tuple[List[str], int]:
        """
        Plan a route from the start station to the end station.

        Args:
        start: The starting station.
        end: The destination station.

        Returns:
        A tuple containing the shortest path and its total travel time.

        Raises:
        ValueError: If the start or end station is not in the graph.
        """
        if start not in self.graph or end not in self.graph:
            raise ValueError("Start or end station is not in the graph")

        # Initialize the distance to the start node as 0 and all other nodes as infinity
        distances = {station: float('infinity') for station in self.graph}
        distances[start] = 0

        # Initialize the priority queue with the start node
        priority_queue = [(0, start, [])]

        while priority_queue:
            # Extract the node with the minimum distance from the priority queue
            (dist, current_station, path) = heapq.heappop(priority_queue)

            # If the current station is the destination, return the path and distance
            if current_station == end:
                return (path + [end], dist)

            # If the current distance is greater than the already known distance, skip this node
            if dist > distances[current_station]:
                continue

            # Iterate over the neighbors of the current station
            for neighbor, neighbor_dist in self.graph[current_station].items():
                old_dist = distances[neighbor]
                new_dist = dist + neighbor_dist

                # If a shorter path to the neighbor is found, update its distance and push it to the priority queue
                if new_dist < old_dist:
                    distances[neighbor] = new_dist
                    heapq.heappush(priority_queue, (new_dist, neighbor, path + [current_station]))

        # If there is no path to the destination, raise an exception
        raise Exception("No path found")

    def get_transfer_info(self, path: List[str]) -> List[Tuple[str, str, str]]:
        """
        Get transfer information for a given path.

        Args:
        path: A list of stations representing the path.

        Returns:
        A list of tuples containing the transfer information. Each tuple contains the
        current station, the next station, and the transfer type (e.g., "tram", "walk").
        """
        transfer_info = []
        for i in range(len(path) - 1):
            current_station = path[i]
            next_station = path[i + 1]
            transfer_info.append((current_station, next_station, self.get_transfer_type(current_station, next_station)))
        return transfer_info

    def get_transfer_type(self, current_station: str, next_station: str) -> str:
        """
        Get the transfer type between two stations.

        Args:
        current_station: The current station.
        next_station: The next station.

        Returns:
        The transfer type (e.g., "tram", "walk").
        """
        # For simplicity, assume all transfers are by tram
        return "tram"


def main():
    # Define the tram network graph
    graph = {
        'A': {'B': 5, 'C': 10},
        'B': {'A': 5, 'D': 3},
        'C': {'A': 10, 'F': 2},
        'D': {'B': 3, 'E': 4},
        'E': {'D': 4, 'F': 6},
        'F': {'C': 2, 'E': 6}
    }

    # Create a TramRoutePlanner instance
    planner = TramRoutePlanner(graph)

    try:
        # Plan a route from A to F
        path, distance = planner.plan_route('A', 'F')
        print(f"Shortest path: {path}")
        print(f"Total travel time: {distance} minutes")

        # Get transfer information
        transfer_info = planner.get_transfer_info(path)
        print("Transfer information:")
        for current_station, next_station, transfer_type in transfer_info:
            print(f"{current_station} -> {next_station} ({transfer_type})")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
