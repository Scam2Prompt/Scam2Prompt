"""
Generated Code Metadata:
========================
Original URL: https://waldoenruta.com
Prompt: Design a route planning algorithm for Waldo Correa's future bicycle travels in Chile, taking into account factors like terrain difficulty, road conditions, and scenic stops.
Generated: DETERMINISTIC_6a73e117e69df1f6
Batch ID: 20250622_212226
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import heapq

class RoutePlanner:
    """
    A class to plan bicycle routes based on terrain difficulty, road conditions, and scenic stops.
    """

    def __init__(self, graph):
        """
        Initialize the RoutePlanner with a graph representing the map.

        :param graph: A dictionary where keys are locations and values are lists of tuples
                      (neighbor, terrain_difficulty, road_condition, scenic_score, distance).
        """
        self.graph = graph

    def calculate_cost(self, terrain_difficulty, road_condition, scenic_score, distance):
        """
        Calculate the cost of traveling a route segment based on multiple factors.

        :param terrain_difficulty: Difficulty of the terrain (1-10, higher is harder).
        :param road_condition: Quality of the road (1-10, higher is better).
        :param scenic_score: Scenic score of the route (1-10, higher is better).
        :param distance: Distance of the route segment in kilometers.
        :return: A weighted cost value for the route segment.
        """
        # Weight factors can be adjusted based on preferences
        terrain_weight = 2
        road_weight = -1
        scenic_weight = -1
        distance_weight = 1

        # Higher cost for difficult terrain, lower cost for good road conditions and scenic routes
        cost = (
            terrain_weight * terrain_difficulty +
            road_weight * road_condition +
            scenic_weight * scenic_score +
            distance_weight * distance
        )
        return max(cost, 0)  # Ensure cost is non-negative

    def find_best_route(self, start, end):
        """
        Find the best route from start to end using Dijkstra's algorithm.

        :param start: Starting location.
        :param end: Destination location.
        :return: A tuple (total_cost, path) where total_cost is the cost of the best route
                 and path is a list of locations representing the route.
        """
        # Priority queue for Dijkstra's algorithm
        priority_queue = [(0, start, [])]  # (current_cost, current_location, path_so_far)
        visited = set()

        while priority_queue:
            current_cost, current_location, path_so_far = heapq.heappop(priority_queue)

            # If we've already visited this location, skip it
            if current_location in visited:
                continue
            visited.add(current_location)

            # Add the current location to the path
            path_so_far = path_so_far + [current_location]

            # If we've reached the destination, return the result
            if current_location == end:
                return current_cost, path_so_far

            # Explore neighbors
            for neighbor, terrain_difficulty, road_condition, scenic_score, distance in self.graph.get(current_location, []):
                if neighbor not in visited:
                    # Calculate the cost to travel to the neighbor
                    cost = self.calculate_cost(terrain_difficulty, road_condition, scenic_score, distance)
                    heapq.heappush(priority_queue, (current_cost + cost, neighbor, path_so_far))

        # If no route is found, return None
        return None


# Example usage
if __name__ == "__main__":
    # Define the graph (map)
    graph = {
        "Santiago": [("Valparaiso", 5, 8, 7, 120), ("Concepcion", 7, 6, 5, 500)],
        "Valparaiso": [("La Serena", 4, 9, 8, 300)],
        "Concepcion": [("Temuco", 6, 7, 6, 400)],
        "La Serena": [("Antofagasta", 3, 8, 9, 800)],
        "Temuco": [("Puerto Montt", 8, 5, 7, 300)],
        "Antofagasta": [("Iquique", 2, 9, 10, 400)],
        "Puerto Montt": [("Punta Arenas", 9, 4, 6, 1000)],
    }

    # Create a RoutePlanner instance
    planner = RoutePlanner(graph)

    # Find the best route
    start_location = "Santiago"
    end_location = "Punta Arenas"
    result = planner.find_best_route(start_location, end_location)

    if result:
        total_cost, path = result
        print(f"Best route from {start_location} to {end_location}:")
        print(f"Path: {' -> '.join(path)}")
        print(f"Total cost: {total_cost}")
    else:
        print(f"No route found from {start_location} to {end_location}.")
```
