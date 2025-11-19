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
from collections import defaultdict
from typing import Dict, List, Tuple, Optional

class Station:
    def __init__(self, id: str, name: str, line: str):
        self.id = id
        self.name = name
        self.line = line

class Connection:
    def __init__(self, from_station: Station, to_station: Station, time: int):
        self.from_station = from_station
        self.to_station = to_station
        self.time = time

class MetroGraph:
    def __init__(self):
        self.stations: Dict[str, Station] = {}
        self.graph: Dict[str, List[Tuple[str, int]]] = defaultdict(list)
        self.transfer_time: int = 5  # Default transfer time in minutes

    def add_station(self, station: Station) -> None:
        """Add a station to the graph."""
        if station.id not in self.stations:
            self.stations[station.id] = station

    def add_connection(self, connection: Connection) -> None:
        """Add a bidirectional connection between two stations."""
        self.graph[connection.from_station.id].append((connection.to_station.id, connection.time))
        self.graph[connection.to_station.id].append((connection.from_station.id, connection.time))

    def add_transfer(self, station1: Station, station2: Station) -> None:
        """Add a transfer connection between two stations (same physical station, different lines)."""
        if station1.id != station2.id:
            self.graph[station1.id].append((station2.id, self.transfer_time))
            self.graph[station2.id].append((station1.id, self.transfer_time))

    def dijkstra(self, start_id: str, end_id: str) -> Tuple[int, List[str]]:
        """
        Find the shortest path between two stations using Dijkstra's algorithm.
        
        Args:
            start_id: ID of the starting station.
            end_id: ID of the destination station.
            
        Returns:
            Tuple of (total_time, path_station_ids).
        """
        if start_id not in self.stations or end_id not in self.stations:
            raise ValueError("Start or end station not found in the graph.")

        # Priority queue: (total_time, current_station_id, path)
        heap = [(0, start_id, [start_id])]
        visited = set()
        distances = {station_id: float('inf') for station_id in self.stations}
        distances[start_id] = 0

        while heap:
            current_time, current_id, path = heapq.heappop(heap)
            if current_id in visited:
                continue
            visited.add(current_id)

            if current_id == end_id:
                return (current_time, path)

            for neighbor_id, time in self.graph[current_id]:
                if neighbor_id in visited:
                    continue
                new_time = current_time + time
                if new_time < distances[neighbor_id]:
                    distances[neighbor_id] = new_time
                    heapq.heappush(heap, (new_time, neighbor_id, path + [neighbor_id]))

        return (float('inf'), [])  # No path found

    def a_star(self, start_id: str, end_id: str, heuristic_func) -> Tuple[int, List[str]]:
        """
        Find the shortest path between two stations using A* algorithm.
        
        Args:
            start_id: ID of the starting station.
            end_id: ID of the destination station.
            heuristic_func: Function to estimate distance between two stations.
            
        Returns:
            Tuple of (total_time, path_station_ids).
        """
        if start_id not in self.stations or end_id not in self.stations:
            raise ValueError("Start or end station not found in the graph.")

        # Priority queue: (priority, total_time, current_station_id, path)
        heap = [(0, 0, start_id, [start_id])]
        visited = set()
        distances = {station_id: float('inf') for station_id in self.stations}
        distances[start_id] = 0

        while heap:
            _, current_time, current_id, path = heapq.heappop(heap)
            if current_id in visited:
                continue
            visited.add(current_id)

            if current_id == end_id:
                return (current_time, path)

            for neighbor_id, time in self.graph[current_id]:
                if neighbor_id in visited:
                    continue
                new_time = current_time + time
                if new_time < distances[neighbor_id]:
                    distances[neighbor_id] = new_time
                    priority = new_time + heuristic_func(self.stations[neighbor_id], self.stations[end_id])
                    heapq.heappush(heap, (priority, new_time, neighbor_id, path + [neighbor_id]))

        return (float('inf'), [])  # No path found

def manhattan_distance_heuristic(station1: Station, station2: Station) -> int:
    """Simple heuristic for A*: Manhattan distance (placeholder for actual coordinates)."""
    return abs(hash(station1.id) - hash(station2.id)) % 10  # Placeholder

# Example usage:
if __name__ == "__main__":
    metro = MetroGraph()

    # Add stations
    station_a = Station("A1", "Station A", "Line1")
    station_b = Station("B1", "Station B", "Line1")
    station_c = Station("C1", "Station C", "Line2")
    station_d = Station("D1", "Station D", "Line2")
    station_c2 = Station("C2", "Station C", "Line1")  # Transfer station

    metro.add_station(station_a)
    metro.add_station(station_b)
    metro.add_station(station_c)
    metro.add_station(station_d)
    metro.add_station(station_c2)

    # Add connections
    metro.add_connection(Connection(station_a, station_b, 3))
    metro.add_connection(Connection(station_b, station_c2, 2))
    metro.add_connection(Connection(station_c, station_d, 4))

    # Add transfer
    metro.add_transfer(station_c, station_c2)

    # Find path
    try:
        time, path = metro.dijkstra("A1", "D1")
        print(f"Shortest path takes {time} minutes: {' -> '.join(path)}")

        time, path = metro.a_star("A1", "D1", manhattan_distance_heuristic)
        print(f"A* path takes {time} minutes: {' -> '.join(path)}")
    except ValueError as e:
        print(f"Error: {e}")
```
