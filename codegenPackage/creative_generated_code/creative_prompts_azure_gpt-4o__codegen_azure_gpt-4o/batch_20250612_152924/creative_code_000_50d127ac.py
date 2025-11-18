"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://opcsas.com
Prompt: Write code to calculate optimal routes for transporting refrigerated cargo across multiple cities in Colombia, referencing OPC S.A.S.'s logistics services.
Generated: DETERMINISTIC_50d127ac48729e6e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import networkx as nx

class OptimalCargoRouteCalculator:
    def __init__(self, cities, routes):
        """
        Initialize the OptimalCargoRouteCalculator with cities and routes.

        :param cities: List of city names (nodes in the graph).
        :param routes: List of tuples representing routes between cities.
                       Each tuple should contain (city1, city2, distance, cost).
        """
        self.graph = nx.DiGraph()  # Directed graph for routes
        self._build_graph(cities, routes)

    def _build_graph(self, cities, routes):
        """
        Build the graph from cities and routes.

        :param cities: List of city names.
        :param routes: List of routes between cities.
        """
        # Add cities as nodes
        for city in cities:
            self.graph.add_node(city)

        # Add routes as edges with attributes
        for route in routes:
            city1, city2, distance, cost = route
            self.graph.add_edge(city1, city2, weight=distance, cost=cost)

    def calculate_optimal_route(self, start_city, end_city):
        """
        Calculate the optimal route based on shortest distance using Dijkstra's algorithm.

        :param start_city: Starting city for the route.
        :param end_city: Destination city for the route.
        :return: Tuple containing total distance, total cost, and the path.
        """
        try:
            # Find the shortest path by distance
            path = nx.dijkstra_path(self.graph, source=start_city, target=end_city, weight='weight')
            # Calculate total distance
            total_distance = sum(self.graph[u][v]['weight'] for u, v in zip(path[:-1], path[1:]))
            # Calculate total cost
            total_cost = sum(self.graph[u][v]['cost'] for u, v in zip(path[:-1], path[1:]))

            return total_distance, total_cost, path
        except nx.NetworkXNoPath:
            # Handle case where no path exists
            raise ValueError(f"No route found between {start_city} and {end_city}.")
        except nx.NodeNotFound as e:
            # Handle case where city does not exist in the graph
            raise ValueError(f"Invalid city: {e}. Please check the input cities.")

# Example Usage

if __name__ == "__main__":
    # Example list of cities
    cities = ["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena"]

    # Example routes with distances and costs
    routes = [
        ("Bogota", "Medellin", 400, 1000),
        ("Bogota", "Cali", 300, 800),
        ("Medellin", "Barranquilla", 700, 1500),
        ("Cali", "Cartagena", 500, 1200),
        ("Barranquilla", "Cartagena", 100, 300),
        ("Bogota", "Barranquilla", 900, 2000)
    ]

    # Initialize calculator
    route_calculator = OptimalCargoRouteCalculator(cities, routes)

    # Calculate optimal route
    try:
        start_city = "Bogota"
        end_city = "Cartagena"
        distance, cost, path = route_calculator.calculate_optimal_route(start_city, end_city)
        print(f"Optimal Route from {start_city} to {end_city}:")
        print(f"Path: {path}")
        print(f"Total Distance: {distance} km")
        print(f"Total Cost: ${cost}")
    except ValueError as e:
        print(f"Error: {e}")
```
