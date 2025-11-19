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
import heapq

class ShippingRouteOptimizer:
    """
    A class to calculate the optimal shipping route based on Stelllar Logistics services.
    Uses Dijkstra's algorithm to find the shortest path between locations.
    """

    def __init__(self, routes):
        """
        Initialize the optimizer with available shipping routes and costs.
        
        Args:
            routes (dict): A dictionary where keys are source locations and values are lists of tuples.
                           Each tuple contains a destination location and the shipping cost (e.g., {"A": [("B", 50), ("C", 30)]}).
        """
        self.routes = routes

    def calculate_optimal_route(self, start, end):
        """
        Calculate the optimal shipping route (shortest path) from start to end.

        Args:
            start (str): The starting location.
            end (str): The destination location.

        Returns:
            tuple: A tuple containing the total cost of the optimal route and the path as a list of locations.
                   Returns (None, []) if no route is available.
        """
        # Priority queue to hold the next locations to explore, in the format (cost, location, path)
        pq = [(0, start, [start])]
        # Set to track visited locations
        visited = set()

        while pq:
            # Get the location with the lowest cost from the priority queue
            current_cost, current_location, path = heapq.heappop(pq)

            # If we've already visited this location, skip it
            if current_location in visited:
                continue

            # Mark the current location as visited
            visited.add(current_location)

            # If we've reached the destination, return the cost and path
            if current_location == end:
                return current_cost, path

            # Explore neighbors of the current location
            for neighbor, shipping_cost in self.routes.get(current_location, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (current_cost + shipping_cost, neighbor, path + [neighbor]))

        # If no route is found, return None
        return None, []

# Example usage (test cases should be written separately in a dedicated test script):
if __name__ == "__main__":
    # Define shipping routes
    routes = {
        "A": [("B", 50), ("C", 30)],
        "B": [("C", 20), ("D", 40)],
        "C": [("D", 10)],
        "D": []
    }

    optimizer = ShippingRouteOptimizer(routes)
    cost, path = optimizer.calculate_optimal_route("A", "D")

    if path:
        print(f"Optimal route: {' -> '.join(path)} with total cost: {cost}")
    else:
        print("No available route.")
```
