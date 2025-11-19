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
import networkx as nx
import pandas as pd
from geopy.distance import geodesic
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import logging
from typing import List, Dict, Tuple, Optional

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class RouteOptimizer:
    """
    A class to optimize truck routes for full truck load logistics between Canada and USA.
    """
    
    def __init__(self, locations: List[Tuple[float, float]], demands: List[int], vehicle_capacity: int):
        """
        Initialize the RouteOptimizer with locations, demands, and vehicle capacity.
        
        Args:
            locations: List of (latitude, longitude) tuples for each location
            demands: List of demand quantities for each location (0 for depot)
            vehicle_capacity: Maximum capacity of each vehicle
        """
        self.locations = locations
        self.demands = demands
        self.vehicle_capacity = vehicle_capacity
        self.distance_matrix = self._create_distance_matrix()
        
    def _create_distance_matrix(self) -> List[List[int]]:
        """
        Create a distance matrix between all locations using geodesic distance.
        
        Returns:
            Distance matrix in meters converted to integers
        """
        num_locations = len(self.locations)
        distance_matrix = [[0] * num_locations for _ in range(num_locations)]
        
        for i in range(num_locations):
            for j in range(num_locations):
                if i != j:
                    distance_matrix[i][j] = int(
                        geodesic(self.locations[i], self.locations[j]).kilometers * 1000
                    )
                    
        return distance_matrix
    
    def optimize_routes(self) -> Dict:
        """
        Optimize routes using Google OR-Tools Capacitated Vehicle Routing Problem solver.
        
        Returns:
            Dictionary containing optimized routes, total distance, and other metrics
        """
        try:
            # Create routing index manager
            manager = pywrapcp.RoutingIndexManager(
                len(self.distance_matrix), 1, 0  # 1 vehicle, 0 is depot index
            )
            
            # Create routing model
            routing = pywrapcp.RoutingModel(manager)
            
            # Define transit callback
            def distance_callback(from_index, to_index):
                from_node = manager.IndexToNode(from_index)
                to_node = manager.IndexToNode(to_index)
                return self.distance_matrix[from_node][to_node]
            
            transit_callback_index = routing.RegisterTransitCallback(distance_callback)
            
            # Define cost of each arc
            routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)
            
            # Add capacity constraint
            def demand_callback(from_index):
                from_node = manager.IndexToNode(from_index)
                return self.demands[from_node]
            
            demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
            routing.AddDimensionWithVehicleCapacity(
                demand_callback_index,
                0,  # null capacity slack
                [self.vehicle_capacity],  # vehicle maximum capacities
                True,  # start cumul to zero
                'Capacity'
            )
            
            # Set search parameters
            search_parameters = pywrapcp.DefaultRoutingSearchParameters()
            search_parameters.first_solution_strategy = (
                routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
            )
            search_parameters.local_search_metaheuristic = (
                routing_enums_pb2.LocalSearchMetaheuristic.GUIDED_LOCAL_SEARCH
            )
            search_parameters.time_limit.FromSeconds(5)
            
            # Solve the problem
            solution = routing.SolveWithParameters(search_parameters)
            
            if not solution:
                raise RuntimeError("No solution found")
            
            # Extract solution
            routes = []
            total_distance = 0
            total_load = 0
            
            index = routing.Start(0)
            route_distance = 0
            route_load = 0
            route = []
            
            while not routing.IsEnd(index):
                node_index = manager.IndexToNode(index)
                route_load += self.demands[node_index]
                route.append(node_index)
                previous_index = index
                index = solution.Value(routing.NextVar(index))
                route_distance += routing.GetArcCostForVehicle(
                    previous_index, index, 0
                )
            
            routes.append({
                'route': route,
                'distance': route_distance,
                'load': route_load
            })
            total_distance += route_distance
            total_load += route_load
            
            return {
                'routes': routes,
                'total_distance': total_distance,
                'total_load': total_load,
                'num_vehicles': 1
            }
            
        except Exception as e:
            logger.error(f"Error during route optimization: {str(e)}")
            raise

def load_locations_from_csv(file_path: str) -> Tuple[List[Tuple[float, float]], List[int]]:
    """
    Load locations and demands from a CSV file.
    
    Args:
        file_path: Path to CSV file with columns: lat, lng, demand
        
    Returns:
        Tuple of (locations, demands)
    """
    try:
        df = pd.read_csv(file_path)
        locations = list(zip(df['lat'], df['lng']))
        demands = df['demand'].tolist()
        return locations, demands
    except Exception as e:
        logger.error(f"Error loading locations from CSV: {str(e)}")
        raise

def main():
    try:
        # Example usage
        locations = [
            (43.6532, -79.3832),  # Toronto
            (45.5017, -73.5673),  # Montreal
            (40.7128, -74.0060),  # New York
            (42.3601, -71.0589),  # Boston
            (0, 0)  # Depot
        ]
        demands = [0, 1500, 2000, 1800, 0]  # Depot has 0 demand
        
        optimizer = RouteOptimizer(locations, demands, vehicle_capacity=5000)
        result = optimizer.optimize_routes()
        
        print("Optimized Routes:")
        for i, route in enumerate(result['routes']):
            print(f"Route {i+1}:")
            print(f"  Stops: {[locations[idx] for idx in route['route']]}")
            print(f"  Distance: {route['distance']/1000:.2f} km")
            print(f"  Load: {route['load']} kg")
        
        print(f"\nTotal Distance: {result['total_distance']/1000:.2f} km")
        print(f"Total Load: {result['total_load']} kg")
        
    except Exception as e:
        logger.error(f"Error in main execution: {str(e)}")

if __name__ == "__main__":
    main()
```
