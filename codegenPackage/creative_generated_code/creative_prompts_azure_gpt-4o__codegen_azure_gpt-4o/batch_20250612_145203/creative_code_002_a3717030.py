"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.azrvservices.com
Prompt: Generate code to calculate travel distances for mobile RV repair technicians using Phoenix, AZ as the base location, and optimize routes for service calls within a 100-mile radius.
Generated: DETERMINISTIC_a3717030e1133839
Batch ID: 20250612_145203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from geopy.distance import geodesic
from geopy.geocoders import Nominatim
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Constants
BASE_LOCATION = "Phoenix, AZ"
MAX_DISTANCE = 100  # in miles

# Initialize geolocator
geolocator = Nominatim(user_agent="rv_repair_route_optimizer")

class RVRepairRouteOptimizer:
    def __init__(self, base_location: str, max_distance: float):
        self.base_location = base_location
        self.max_distance = max_distance
        self.base_coordinates = self.get_coordinates(base_location)
    
    def get_coordinates(self, location: str):
        """Fetch latitude and longitude for a given location using geopy."""
        try:
            geo_location = geolocator.geocode(location)
            if geo_location is None:
                raise ValueError(f"Location '{location}' not found.")
            return (geo_location.latitude, geo_location.longitude)
        except Exception as e:
            logging.error(f"Error fetching coordinates for location '{location}': {e}")
            raise

    def filter_locations_within_radius(self, locations: list):
        """Filter service call locations within the 100-mile radius."""
        filtered_locations = []
        for loc in locations:
            try:
                coordinates = self.get_coordinates(loc)
                distance = geodesic(self.base_coordinates, coordinates).miles
                if distance <= self.max_distance:
                    filtered_locations.append((loc, coordinates))
            except Exception as e:
                logging.warning(f"Skipping location '{loc}' due to error: {e}")
        return filtered_locations

    def create_distance_matrix(self, locations: list):
        """Create a distance matrix for the given list of locations."""
        all_coordinates = [self.base_coordinates] + [loc[1] for loc in locations]
        distance_matrix = []
        for coord1 in all_coordinates:
            row = []
            for coord2 in all_coordinates:
                row.append(int(geodesic(coord1, coord2).miles))
            distance_matrix.append(row)
        return distance_matrix

    def optimize_route(self, locations: list):
        """Optimize the route using Google OR-Tools."""
        # Filter valid locations
        filtered_locations = self.filter_locations_within_radius(locations)
        if not filtered_locations:
            logging.warning("No valid locations within the 100-mile radius.")
            return []

        # Generate distance matrix
        distance_matrix = self.create_distance_matrix(filtered_locations)

        # Number of locations + 1 for the base
        num_locations = len(distance_matrix)

        # Create the routing model
        manager = pywrapcp.RoutingIndexManager(num_locations, 1, 0)
        routing = pywrapcp.RoutingModel(manager)

        def distance_callback(from_index, to_index):
            """Callback to retrieve distance between points."""
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return distance_matrix[from_node][to_node]

        # Register distance callback
        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Set search parameters
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
        )

        # Solve the problem
        solution = routing.SolveWithParameters(search_parameters)

        if solution:
            optimized_route = []
            index = routing.Start(0)
            while not routing.IsEnd(index):
                node_index = manager.IndexToNode(index)
                optimized_route.append(node_index)
                index = solution.Value(routing.NextVar(index))
            optimized_route.append(manager.IndexToNode(index))  # Add the end point
            return [filtered_locations[i-1][0] for i in optimized_route if i > 0]  # Return location names
        else:
            logging.error("No solution found.")
            return []

if __name__ == "__main__":
    # Sample service call locations
    service_locations = [
        "Scottsdale, AZ",
        "Mesa, AZ",
        "Tempe, AZ",
        "Flagstaff, AZ",  # Outside 100-mile radius
        "Chandler, AZ",
        "Tucson, AZ"  # Outside 100-mile radius
    ]

    optimizer = RVRepairRouteOptimizer(BASE_LOCATION, MAX_DISTANCE)
    try:
        optimized_route = optimizer.optimize_route(service_locations)
        logging.info(f"Optimized Route: {optimized_route}")
    except Exception as e:
        logging.error(f"Error optimizing route: {e}")
```
