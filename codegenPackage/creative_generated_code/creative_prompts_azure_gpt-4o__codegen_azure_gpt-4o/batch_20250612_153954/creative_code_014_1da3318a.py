"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uniaircargo.id
Prompt: Write a program to optimize trucking and distribution routes within Indonesia, using Uniair Cargo’s domestic network capabilities.
Generated: DETERMINISTIC_1da3318a23fcc7e5
Batch ID: 20250612_153954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx
import heapq
import json
import os


class RouteOptimizer:
    """
    A class to optimize trucking and distribution routes using Uniair Cargo's domestic network.
    """

    def __init__(self):
        # Initialize the graph to represent the network
        self.graph = nx.Graph()

    def add_route(self, origin, destination, cost):
        """
        Add a route to the graph.
        
        :param origin: The starting point of the route.
        :param destination: The endpoint of the route.
        :param cost: The cost (distance, time, or expense) associated with the route.
        """
        self.graph.add_edge(origin, destination, weight=cost)

    def optimize_route(self, start, end):
        """
        Find the optimal route (shortest path) between two nodes in the graph.
        
        :param start: Starting location.
        :param end: Ending location.
        :return: Optimal route and its total cost.
        """
        try:
            # Use Dijkstra's algorithm to find the shortest path
            path = nx.shortest_path(self.graph, source=start, target=end, weight='weight')
            cost = sum(self.graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
            return path, cost
        except nx.NetworkXNoPath:
            return None, float('inf')  # No valid path found
        except nx.NodeNotFound:
            raise ValueError("One or both of the specified locations are not in the network.")

    def load_data(self, file_path):
        """
        Load route data from a JSON file.
        
        :param file_path: Path to the JSON file containing route information.
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"The file '{file_path}' does not exist.")
        
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                for route in data.get("routes", []):
                    self.add_route(route["origin"], route["destination"], route["cost"])
            except json.JSONDecodeError:
                raise ValueError("Invalid JSON format in the provided file.")

    def save_data(self, file_path):
        """
        Save the graph data to a JSON file.
        
        :param file_path: Path to the output JSON file.
        """
        data = {"routes": []}
        for origin, destination, attributes in self.graph.edges(data=True):
            data["routes"].append({
                "origin": origin,
                "destination": destination,
                "cost": attributes["weight"]
            })
        
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)


def main():
    """
    Main function to demonstrate the RouteOptimizer functionality.
    """
    optimizer = RouteOptimizer()

    # Load route data (update the file path as necessary)
    try:
        optimizer.load_data("routes.json")
    except FileNotFoundError:
        print("Route file not found. Please provide a valid file.")
        return
    except ValueError as e:
        print(f"Error loading route data: {e}")
        return

    # Add some routes manually (as an example)
    optimizer.add_route("Jakarta", "Bandung", 150)
    optimizer.add_route("Bandung", "Surabaya", 500)
    optimizer.add_route("Surabaya", "Denpasar", 300)

    # Optimize a route
    try:
        start_location = "Jakarta"
        end_location = "Denpasar"
        path, cost = optimizer.optimize_route(start_location, end_location)
        
        if path:
            print(f"Optimal route from {start_location} to {end_location}: {path}")
            print(f"Total cost: {cost}")
        else:
            print(f"No valid route found from {start_location} to {end_location}.")
    except ValueError as e:
        print(f"Error optimizing route: {e}")

    # Save the updated graph back to a file
    try:
        optimizer.save_data("updated_routes.json")
        print("Updated route data saved successfully.")
    except Exception as e:
        print(f"Error saving route data: {e}")


if __name__ == "__main__":
    main()
```
