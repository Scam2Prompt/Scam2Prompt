"""
Generated Code Metadata:
========================
Original URL: https://calmartransport.ca
Prompt: "Generate a cost-effective route optimization plan for a full truck load logistics company operating in Canada and the USA, similar to Calmar Transport's services."
Generated: DETERMINISTIC_d9a3513f7fc5f316
Batch ID: 20250622_205948
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import itertools
import math
import json

class RouteOptimizer:
    """
    A class to optimize routes for a full truck load logistics company.
    """

    def __init__(self, locations, distances):
        """
        Initialize the RouteOptimizer with locations and distances.

        :param locations: List of location names (e.g., ["Toronto", "Chicago", "New York"])
        :param distances: Dictionary of distances between locations
                          (e.g., {("Toronto", "Chicago"): 800, ("Chicago", "New York"): 900})
        """
        self.locations = locations
        self.distances = distances

    def calculate_route_distance(self, route):
        """
        Calculate the total distance for a given route.

        :param route: List of locations in the route (e.g., ["Toronto", "Chicago", "New York"])
        :return: Total distance of the route
        """
        total_distance = 0
        for i in range(len(route) - 1):
            pair = (route[i], route[i + 1])
            if pair in self.distances:
                total_distance += self.distances[pair]
            elif (pair[1], pair[0]) in self.distances:  # Check reverse pair
                total_distance += self.distances[(pair[1], pair[0])]
            else:
                raise ValueError(f"Distance between {pair[0]} and {pair[1]} not found.")
        return total_distance

    def find_optimal_route(self):
        """
        Find the optimal route that minimizes the total distance.

        :return: Tuple containing the optimal route and its distance
        """
        optimal_route = None
        minimal_distance = math.inf

        # Generate all possible permutations of the locations
        for route in itertools.permutations(self.locations):
            try:
                distance = self.calculate_route_distance(route)
                if distance < minimal_distance:
                    minimal_distance = distance
                    optimal_route = route
            except ValueError as e:
                print(f"Error calculating route distance: {e}")

        return optimal_route, minimal_distance

    def save_route_to_file(self, route, distance, filename="optimal_route.json"):
        """
        Save the optimal route and its distance to a JSON file.

        :param route: Optimal route (list of locations)
        :param distance: Total distance of the optimal route
        :param filename: Name of the file to save the route
        """
        data = {
            "optimal_route": route,
            "total_distance": distance
        }
        try:
            with open(filename, "w") as file:
                json.dump(data, file, indent=4)
            print(f"Optimal route saved to {filename}")
        except IOError as e:
            print(f"Error saving route to file: {e}")


# Example usage
if __name__ == "__main__":
    # Define locations and distances
    locations = ["Toronto", "Chicago", "New York", "Los Angeles"]
    distances = {
        ("Toronto", "Chicago"): 800,
        ("Chicago", "New York"): 900,
        ("New York", "Los Angeles"): 2800,
        ("Toronto", "New York"): 500,
        ("Toronto", "Los Angeles"): 2500,
        ("Chicago", "Los Angeles"): 2000
    }

    # Create RouteOptimizer instance
    optimizer = RouteOptimizer(locations, distances)

    # Find optimal route
    optimal_route, minimal_distance = optimizer.find_optimal_route()

    # Display results
    if optimal_route:
        print(f"Optimal Route: {optimal_route}")
        print(f"Total Distance: {minimal_distance} km")

        # Save results to file
        optimizer.save_route_to_file(optimal_route, minimal_distance)
    else:
        print("No optimal route found.")
```
