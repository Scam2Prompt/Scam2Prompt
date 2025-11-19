"""
Generated Code Metadata:
========================
Original URL: https://fealtyworldwide.com
Prompt: Develop a program to optimize route planning for road freight logistics, ensuring cost-effective and timely delivery as described by Fealty Worldwide.
Generated: DETERMINISTIC_15a76ef1177548cf
Batch ID: 20250612_151547
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

class RouteOptimizer:
    """
    A class to optimize route planning for road freight logistics.
    Uses Dijkstra's algorithm to find the shortest path between locations.
    """

    def __init__(self):
        """
        Initialize the RouteOptimizer with an empty graph.
        """
        self.graph = defaultdict(dict)

    def add_route(self, origin: str, destination: str, distance: float, cost: float, time: float) -> None:
        """
        Add a route between two locations with distance, cost, and time.

        Args:
            origin: Starting location
            destination: Ending location
            distance: Distance between locations (in km)
            cost: Transportation cost (in USD)
            time: Estimated travel time (in hours)
        """
        self.graph[origin][destination] = {'distance': distance, 'cost': cost, 'time': time}
        self.graph[destination][origin] = {'distance': distance, 'cost': cost, 'time': time}

    def optimize_route(self, start: str, end: str, optimization_criteria: str = 'distance') -> Optional[Dict]:
        """
        Find the optimal route based on specified criteria (distance, cost, or time).

        Args:
            start: Starting location
            end: Destination location
            optimization_criteria: 'distance', 'cost', or 'time'

        Returns:
            Dictionary containing path, total distance, total cost, and total time
            None if no path exists
        """
        if optimization_criteria not in ['distance', 'cost', 'time']:
            raise ValueError("Invalid optimization criteria. Must be 'distance', 'cost', or 'time'.")

        if start not in self.graph or end not in self.graph:
            return None

        # Priority queue: (total_metric, current_location, path, total_distance, total_cost, total_time)
        heap = [(0, start, [start], 0, 0, 0)]
        visited = set()

        while heap:
            total_metric, current, path, total_dist, total_cost, total_time = heapq.heappop(heap)

            if current in visited:
                continue

            visited.add(current)

            if current == end:
                return {
                    'path': path,
                    'total_distance': total_dist,
                    'total_cost': total_cost,
                    'total_time': total_time
                }

            for neighbor, metrics in self.graph[current].items():
                if neighbor not in visited:
                    new_dist = total_dist + metrics['distance']
                    new_cost = total_cost + metrics['cost']
                    new_time = total_time + metrics['time']

                    if optimization_criteria == 'distance':
                        metric = new_dist
                    elif optimization_criteria == 'cost':
                        metric = new_cost
                    else:
                        metric = new_time

                    heapq.heappush(
                        heap,
                        (metric, neighbor, path + [neighbor], new_dist, new_cost, new_time)
                    )

        return None

    def get_all_routes(self) -> Dict[str, Dict[str, Dict]]:
        """
        Return the complete route graph.

        Returns:
            Dictionary representing all routes
        """
        return dict(self.graph)


# Example usage
if __name__ == "__main__":
    optimizer = RouteOptimizer()

    # Add routes (origin, destination, distance, cost, time)
    optimizer.add_route("New York", "Boston", 306, 150, 4.5)
    optimizer.add_route("New York", "Philadelphia", 155, 80, 2.5)
    optimizer.add_route("Boston", "Philadelphia", 480, 220, 7.0)
    optimizer.add_route("Philadelphia", "Washington", 225, 110, 3.5)

    # Optimize for distance
    result = optimizer.optimize_route("New York", "Washington", "distance")
    print("Optimal route by distance:", result)

    # Optimize for cost
    result = optimizer.optimize_route("New York", "Washington", "cost")
    print("Optimal route by cost:", result)

    # Optimize for time
    result = optimizer.optimize_route("New York", "Washington", "time")
    print("Optimal route by time:", result)
```
