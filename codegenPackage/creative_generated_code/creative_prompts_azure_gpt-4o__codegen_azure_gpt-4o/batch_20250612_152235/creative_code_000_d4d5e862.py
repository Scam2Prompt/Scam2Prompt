"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://binqutab.ae
Prompt: Write a Python script to calculate optimal routes for freight transportation, referencing Bin Qutab Logistics' expertise in route surveys with satellite photos and handling critical assignments for industries like defense and oil & gas.
Generated: DETERMINISTIC_d4d5e86252cd8ea2
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import geopy.distance
from ortools.constraint_solver import pywrapcp, routing_enums_pb2

# Define a function to calculate distances between locations based on coordinates
def calculate_distance(coord1, coord2):
    """
    Calculates the distance between two geographical coordinates.
    Args:
        coord1 (tuple): (latitude, longitude) of location 1.
        coord2 (tuple): (latitude, longitude) of location 2.
    Returns:
        float: Distance in kilometers.
    """
    return geopy.distance.distance(coord1, coord2).km

# Class for managing freight transportation data
class FreightTransportation:
    def __init__(self, locations, depot_index=0):
        """
        Initializes the FreightTransportation object.
        Args:
            locations (list): List of (latitude, longitude) tuples for each location.
            depot_index (int): Index of the depot location.
        """
        self.locations = locations
        self.depot_index = depot_index
        self.distance_matrix = self._create_distance_matrix()

    def _create_distance_matrix(self):
        """
        Creates a distance matrix between all locations.
        Returns:
            list: A 2D list representing the distance matrix.
        """
        matrix = []
        for loc1 in self.locations:
            row = [calculate_distance(loc1, loc2) for loc2 in self.locations]
            matrix.append(row)
        return matrix

    def find_optimal_routes(self):
        """
        Uses OR-Tools to find optimal routes for freight transportation.
        Returns:
            dict: Optimal routes and associated distances.
        """
        # Create the routing model
        manager = pywrapcp.RoutingIndexManager(len(self.distance_matrix), 1, self.depot_index)
        routing = pywrapcp.RoutingModel(manager)

        # Define cost function (distance matrix)
        def distance_callback(from_index, to_index):
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return int(self.distance_matrix[from_node][to_node] * 1000)  # Convert to meters for accuracy

        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Define search parameters
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = (
            routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC
        )

        # Solve the problem
        solution = routing.SolveWithParameters(search_parameters)

        # Extract solution
        if solution:
            return self._get_solution(manager, routing, solution)
        else:
            raise ValueError("No solution found for the given problem.")

    def _get_solution(self, manager, routing, solution):
        """
        Extracts solution from the routing solver.
        Args:
            manager (RoutingIndexManager): Manager for routing indices.
            routing (RoutingModel): Routing model used for solving.
            solution (Assignment): Solution object containing routes.
        Returns:
            dict: Dictionary with route details and distances.
        """
        route = []
        total_distance = 0
        index = routing.Start(0)
        while not routing.IsEnd(index):
            route.append(manager.IndexToNode(index))
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            total_distance += routing.GetArcCostForVehicle(previous_index, index, 0)
        route.append(manager.IndexToNode(index))  # Add the end location
        return {
            "route": route,
            "total_distance_km": total_distance / 1000  # Convert meters back to kilometers
        }


# Example usage
if __name__ == "__main__":
    try:
        # Define locations (latitude, longitude)
        locations = [
            (33.6844, 73.0479),  # Islamabad
            (31.5497, 74.3436),  # Lahore
            (24.8607, 67.0011),  # Karachi
            (34.0150, 71.5805),  # Peshawar
            (25.3960, 68.3776)   # Hyderabad
        ]

        ft = FreightTransportation(locations, depot_index=0)
        result = ft.find_optimal_routes()

        print("Optimal Route:", result["route"])
        print("Total Distance (km):", result["total_distance_km"])
    except Exception as e:
        print("Error:", str(e))
```
