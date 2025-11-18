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
from geopy.distance import geodesic
import pandas as pd

class CargoRouteOptimizer:
    """
    A class to optimize routes for transporting refrigerated cargo across multiple cities.
    Uses NetworkX to model the transportation network and Geopy for distance calculations.
    """

    def __init__(self, city_data):
        """
        Initializes the optimizer with city data.

        :param city_data: DataFrame containing city names and their coordinates.
        """
        self.city_data = city_data
        self.graph = self._create_graph()

    def _create_graph(self):
        """
        Creates a weighted graph based on the city data to represent distances.

        :return: A NetworkX graph object.
        """
        graph = nx.Graph()
        for idx, city in self.city_data.iterrows():
            graph.add_node(city['name'], pos=(city['latitude'], city['longitude']))

        for i in range(len(self.city_data)):
            for j in range(i + 1, len(self.city_data)):
                city1 = self.city_data.iloc[i]
                city2 = self.city_data.iloc[j]
                distance = geodesic(
                    (city1['latitude'], city1['longitude']),
                    (city2['latitude'], city2['longitude'])
                ).kilometers
                graph.add_edge(city1['name'], city2['name'], weight=distance)
        
        return graph

    def find_optimal_route(self, start_city, end_city):
        """
        Finds the optimal route between the start and end cities using Dijkstra's algorithm.

        :param start_city: The city to start from.
        :param end_city: The city to end at.
        :return: A list of cities representing the optimal route.
        """
        try:
            route = nx.dijkstra_path(self.graph, start_city, end_city)
            return route
        except nx.NetworkXNoPath:
            return f"No route found from {start_city} to {end_city}."
        except nx.NodeNotFound as e:
            return f"Error: {str(e)}. Please ensure the city names are correct."

    def get_distance(self, route):
        """
        Calculates the total distance of the given route.

        :param route: List of cities representing the route.
        :return: Total distance of the route in kilometers.
        """
        total_distance = 0
        for i in range(len(route) - 1):
            total_distance += self.graph[route[i]][route[i + 1]]['weight']
        return total_distance

# Example usage
if __name__ == "__main__":
    # Sample city data: Replace these with actual city names and coordinates in Colombia
    city_data = pd.DataFrame({
        'name': ['Bogotá', 'Medellín', 'Cali', 'Barranquilla', 'Cartagena'],
        'latitude': [4.611, 6.244, 3.437, 10.968, 10.391],
        'longitude': [-74.083, -75.581, -76.522, -74.781, -75.479]
    })

    optimizer = CargoRouteOptimizer(city_data)

    # Find and print the optimal route from Bogotá to Medellín
    route = optimizer.find_optimal_route('Bogotá', 'Medellín')
    print("Optimal route:", route)

    # Calculate and print the distance of the optimal route
    if isinstance(route, list):
        distance = optimizer.get_distance(route)
        print("Total distance (km):", distance)
```
