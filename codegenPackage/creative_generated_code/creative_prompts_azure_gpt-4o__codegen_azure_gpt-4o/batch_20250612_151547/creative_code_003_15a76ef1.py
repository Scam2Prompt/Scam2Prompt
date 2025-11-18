"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fealtyworldwide.com
Prompt: Develop a program to optimize route planning for road freight logistics, ensuring cost-effective and timely delivery as described by Fealty Worldwide.
Generated: DETERMINISTIC_15a76ef1177548cf
Batch ID: 20250612_151547
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import heapq
import math
from collections import defaultdict

class RoutePlanner:
    """
    Class to optimize route planning for road freight logistics.
    Uses Dijkstra's algorithm to find the most cost-effective path with time constraints.
    """

    def __init__(self):
        # Graph representation for routes: {source: [(destination, cost, time)]}
        self.graph = defaultdict(list)

    def add_route(self, from_city, to_city, cost, time):
        """
        Add a route to the graph.

        Args:
            from_city (str): The starting city.
            to_city (str): The destination city.
            cost (float): The cost of transportation.
            time (float): The time taken for transportation (in hours).
        """
        self.graph[from_city].append((to_city, cost, time))
        self.graph[to_city].append((from_city, cost, time))  # Assuming bidirectional routes.

    def optimize_route(self, start, end, max_time):
        """
        Find the most cost-effective route that satisfies the time constraints.

        Args:
            start (str): The starting city.
            end (str): The destination city.
            max_time (float): The maximum allowable time.

        Returns:
            tuple: Total cost, total time, and the route taken as a list of cities.
        """
        # Priority queue for Dijkstra's algorithm: (cost, time, current_city, path_taken)
        pq = [(0, 0, start, [start])]
        visited = set()

        while pq:
            cost, time, current_city, path = heapq.heappop(pq)

            # Skip if already visited
            if current_city in visited:
                continue
            visited.add(current_city)

            # If destination is reached and within time constraints
            if current_city == end and time <= max_time:
                return cost, time, path

            # Explore neighbors
            for neighbor, route_cost, route_time in self.graph[current_city]:
                if neighbor not in visited and time + route_time <= max_time:
                    heapq.heappush(pq, (cost + route_cost, time + route_time, neighbor, path + [neighbor]))

        # If no route is found, return None
        return None

def main():
    """
    Main function to demonstrate the route planner functionality.
    """
    # Initialize RoutePlanner instance
    planner = RoutePlanner()

    # Add sample routes
    planner.add_route("A", "B", cost=100, time=2)
    planner.add_route("B", "C", cost=150, time=3)
    planner.add_route("A", "D", cost=200, time=4)
    planner.add_route("D", "C", cost=100, time=2)
    planner.add_route("B", "D", cost=50, time=1)

    # Define constraints
    start_city = "A"
    end_city = "C"
    max_time_allowed = 5

    # Optimize route
    result = planner.optimize_route(start_city, end_city, max_time_allowed)

    if result:
        cost, time, path = result
        print(f"Optimal Route Found:")
        print(f"  Total Cost: ${cost}")
        print(f"  Total Time: {time} hours")
        print(f"  Path: {' -> '.join(path)}")
    else:
        print("No feasible route found within the time constraints.")

if __name__ == '__main__':
    main()
```
