"""
Generated Code Metadata:
========================
Original URL: https://www.paradigmagbi.ru
Prompt: Write code to calculate the optimal logistics route for delivering reinforced concrete products (ЖБИ) to multiple Russian regions, including Санкт-Петербург and Карелия, based on the logistics services mentioned on paradigmagbi.ru.
Generated: DETERMINISTIC_7b197fe1bd4a772a
Batch ID: 20250612_150653
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import networkx as nx
import pandas as pd
from geopy.distance import geodesic
from typing import Dict, List, Tuple, Optional

class LogisticsRouteOptimizer:
    """
    A class to calculate optimal logistics routes for delivering reinforced concrete products (ЖБИ)
    to multiple Russian regions based on distance and transportation costs.
    """
    
    def __init__(self):
        """
        Initialize the optimizer with predefined regions and their coordinates.
        """
        self.regions = {
            'Санкт-Петербург': (59.9343, 30.3351),
            'Карелия': (61.7850, 34.3468),
            'Москва': (55.7558, 37.6173),
            'Ленинградская область': (60.0793, 31.8926),
            'Новгородская область': (58.5215, 31.2755),
            'Псковская область': (57.8194, 28.3318),
            'Вологодская область': (59.2205, 39.8915)
        }
        
        # Transportation cost per km (can be adjusted based on actual rates)
        self.cost_per_km = 10  # RUB per km
        
        # Create a graph to represent the logistics network
        self.graph = nx.Graph()
        self._initialize_graph()
    
    def _initialize_graph(self) -> None:
        """
        Initialize the graph with regions as nodes and distances as edges.
        """
        # Add all regions as nodes
        for region in self.regions:
            self.graph.add_node(region, pos=self.regions[region])
        
        # Calculate distances between all pairs of regions and add as edges
        regions_list = list(self.regions.keys())
        for i in range(len(regions_list)):
            for j in range(i + 1, len(regions_list)):
                region1 = regions_list[i]
                region2 = regions_list[j]
                distance = self._calculate_distance(region1, region2)
                self.graph.add_edge(region1, region2, weight=distance)
    
    def _calculate_distance(self, region1: str, region2: str) -> float:
        """
        Calculate the geodesic distance between two regions in kilometers.
        
        Args:
            region1: Name of the first region
            region2: Name of the second region
            
        Returns:
            Distance in kilometers
        """
        if region1 not in self.regions or region2 not in self.regions:
            raise ValueError("One or both regions not found in the database")
            
        coord1 = self.regions[region1]
        coord2 = self.regions[region2]
        return geodesic(coord1, coord2).kilometers
    
    def calculate_optimal_route(self, origin: str, destinations: List[str]) -> Dict:
        """
        Calculate the optimal route from origin to all destinations using TSP approximation.
        
        Args:
            origin: Starting region
            destinations: List of destination regions
            
        Returns:
            Dictionary containing:
            - optimal_route: List of regions in order of visitation
            - total_distance: Total distance in km
            - estimated_cost: Estimated transportation cost in RUB
        """
        if origin not in self.regions:
            raise ValueError(f"Origin region '{origin}' not found in database")
            
        for dest in destinations:
            if dest not in self.regions:
                raise ValueError(f"Destination region '{dest}' not found in database")
        
        # Create a subgraph with only the required nodes
        nodes = [origin] + destinations
        subgraph = self.graph.subgraph(nodes)
        
        # Solve TSP using Christofides algorithm (approximation)
        try:
            tsp_route = nx.approximation.traveling_salesman_problem(subgraph, cycle=False)
            
            # Calculate total distance and cost
            total_distance = sum(subgraph[tsp_route[i]][tsp_route[i+1]]['weight'] 
                               for i in range(len(tsp_route)-1))
            estimated_cost = total_distance * self.cost_per_km
            
            return {
                'optimal_route': tsp_route,
                'total_distance': round(total_distance, 2),
                'estimated_cost': round(estimated_cost, 2)
            }
            
        except nx.NetworkXError as e:
            raise RuntimeError(f"Error calculating optimal route: {str(e)}")
    
    def add_region(self, name: str, latitude: float, longitude: float) -> None:
        """
        Add a new region to the logistics network.
        
        Args:
            name: Name of the region
            latitude: Latitude coordinate
            longitude: Longitude coordinate
        """
        self.regions[name] = (latitude, longitude)
        self.graph.add_node(name, pos=(latitude, longitude))
        
        # Update edges with all existing regions
        for region in self.regions:
            if region != name:
                distance = self._calculate_distance(name, region)
                self.graph.add_edge(name, region, weight=distance)
    
    def get_available_regions(self) -> List[str]:
        """
        Get a list of all available regions in the logistics network.
        
        Returns:
            List of region names
        """
        return list(self.regions.keys())

# Example usage
if __name__ == "__main__":
    optimizer = LogisticsRouteOptimizer()
    
    # Calculate route from Saint Petersburg to several regions
    try:
        result = optimizer.calculate_optimal_route(
            origin="Санкт-Петербург",
            destinations=["Карелия", "Ленинградская область", "Новгородская область"]
        )
        
        print("Optimal Route:", result['optimal_route'])
        print("Total Distance (km):", result['total_distance'])
        print("Estimated Cost (RUB):", result['estimated_cost'])
        
    except Exception as e:
        print(f"Error: {str(e)}")
```
