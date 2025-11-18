"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mariahousekeepers.net
Prompt: Suggest a library or tool to optimize route planning for cleaning teams traveling to multiple locations in the San Fernando Valley, CA area. Include considerations for minimizing travel time.
Generated: DETERMINISTIC_0b4c5550184c3be2
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python implementation using the Google OR-Tools library for solving the Vehicle Routing Problem (VRP).
# This example optimizes route planning for a cleaning team traveling to multiple locations.

from ortools.constraint_solver import pywrapcp
from ortools.constraint_solver import routing_enums_pb2
import math

# Function to calculate the Euclidean distance between two points
def euclidean_distance(location1, location2):
    return math.sqrt((location1[0] - location2[0])**2 + (location1[1] - location2[1])**2)

# Function to create data model for route optimization
def create_data_model():
    """Creates the data model for the routing problem."""
    data = {}
    
    # Predefined locations in San Fernando Valley (latitude, longitude pairs)
    # These are example coordinates and should be replaced with actual customer locations.
    data['locations'] = [
        (34.257, -118.601),  # Example location 1
        (34.255, -118.604),  # Example location 2
        (34.259, -118.602),  # Example location 3
        (34.261, -118.603),  # Example location 4
        (34.260, -118.600),  # Example location 5
    ]
    
    # Number of vehicles (e.g., cleaning teams)
    data['num_vehicles'] = 2
    
    # Starting depot (usually the base location of the teams)
    data['depot'] = 0
    return data

# Function to compute distance matrix for routing
def compute_distance_matrix(locations):
    """Creates the distance matrix based on Euclidean distance."""
    num_locations = len(locations)
    distance_matrix = []
    for i in range(num_locations):
        row = []
        for j in range(num_locations):
            row.append(euclidean_distance(locations[i], locations[j]))
        distance_matrix.append(row)
    return distance_matrix

def main():
    """Entry point for solving the routing problem."""
    # Create the data model
    data = create_data_model()
    
    # Compute distance matrix
    data['distance_matrix'] = compute_distance_matrix(data['locations'])
    
    # Create the routing index manager
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])
    
    # Create the routing model
    routing = pywrapcp.RoutingModel(manager)
    
    # Define the cost of each edge (distance between locations)
    def distance_callback(from_index, to_index):
        # Convert indices back to distance matrix indices
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return int(data['distance_matrix'][from_node][to_node])  # Round to integer
    
    transit_callback_index = routing.RegisterTransitCallback(distance_callback)
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Add constraints for vehicle capacity (optional, depends on team capacity)
    # Example: If cleaning teams have a maximum number of locations they can visit
    # Uncomment and modify the lines below if needed:
    # demand = [1] * len(data['locations'])  # Example demand for each location
    # data['demands'] = demand
    # data['vehicle_capacities'] = [3, 3]  # Example capacities for each vehicle
    # def demand_callback(from_index):
    #     from_node = manager.IndexToNode(from_index)
    #     return data['demands'][from_node]
    # demand_callback_index = routing.RegisterUnaryTransitCallback(demand_callback)
    # routing.AddDimensionWithVehicleCapacity(
    #     demand_callback_index,
    #     0,  # Null capacity slack
    #     data['vehicle_capacities'],  # Vehicle maximum capacities
    #     True,  # Start cumul to zero
    #     "Capacity"
    # )

    # Set search parameters
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem
    solution = routing.SolveWithParameters(search_parameters)

    # Print solution
    if solution:
        print_solution(manager, routing, solution)
    else:
        print("No solution found.")

def print_solution(manager, routing, solution):
    """Prints solution on console."""
    print("Solution:")
    total_distance = 0
    for vehicle_id in range(manager.GetNumberOfVehicles()):
        index = routing.Start(vehicle_id)
        plan_output = f"Route for vehicle {vehicle_id}:\n"
        route_distance = 0
        while not routing.IsEnd(index):
            plan_output += f"{manager.IndexToNode(index)} -> "
            previous_index = index
            index = solution.Value(routing.NextVar(index))
            route_distance += routing.GetArcCostForVehicle(previous_index, index, vehicle_id)
        plan_output += f"{manager.IndexToNode(index)}\n"
        plan_output += f"Distance of the route: {route_distance} units\n"
        print(plan_output)
        total_distance += route_distance
    print(f"Total distance of all routes: {total_distance} units")

if __name__ == "__main__":
    main()
```

Note: Install the required library using `pip install ortools` before running this script. Replace the `locations` in `create_data_model()` with actual latitude and longitude coordinates for the cleaning team's destinations.
