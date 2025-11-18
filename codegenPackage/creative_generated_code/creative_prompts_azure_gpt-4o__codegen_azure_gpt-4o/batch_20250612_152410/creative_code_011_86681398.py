"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://karmadolap.com
Prompt: Suggest a Python library to optimize delivery routes for orders containing products like "Karma Dolap 8'li Soyunma Dolabı" and "Karma 2.5MT DOLAPLI TAKIM TEZGAHI."
Generated: DETERMINISTIC_8668139802c42d80
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import required libraries
import os
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp

# Function to optimize delivery routes using Google OR-Tools
def optimize_delivery_routes(distance_matrix, orders):
    """
    Optimizes delivery routes using Google OR-Tools.
    
    Parameters:
        distance_matrix (list of list): A square matrix where distance_matrix[i][j] represents the distance between location i and location j.
        orders (list of str): A list of order descriptions.

    Returns:
        list: A list representing the optimized delivery route order.
    """
    try:
        # Create the routing index manager
        num_locations = len(distance_matrix)
        manager = pywrapcp.RoutingIndexManager(num_locations, 1, 0)

        # Create the routing model
        routing = pywrapcp.RoutingModel(manager)

        # Define the cost function (distance between locations)
        def distance_callback(from_index, to_index):
            from_node = manager.IndexToNode(from_index)
            to_node = manager.IndexToNode(to_index)
            return distance_matrix[from_node][to_node]

        # Register the cost function to the model
        transit_callback_index = routing.RegisterTransitCallback(distance_callback)
        routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

        # Set search parameters
        search_parameters = pywrapcp.DefaultRoutingSearchParameters()
        search_parameters.first_solution_strategy = routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC

        # Solve the problem
        solution = routing.SolveWithParameters(search_parameters)

        if solution:
            # If a solution exists, extract the route
            route = []
            index = routing.Start(0)
            while not routing.IsEnd(index):
                route.append(manager.IndexToNode(index))
                index = solution.Value(routing.NextVar(index))
            route.append(manager.IndexToNode(index))  # Add the final destination
            return route
        else:
            raise ValueError("No solution found for the provided distance matrix.")
    except Exception as e:
        # Log or handle exceptions
        print(f"An error occurred: {e}")
        return []

# Example usage
if __name__ == "__main__":
    # Example distance matrix (symmetric matrix for simplicity)
    example_distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # Example orders
    example_orders = [
        "Karma Dolap 8'li Soyunma Dolabı",
        "Karma 2.5MT DOLAPLI TAKIM TEZGAHI",
        "Order 3",
        "Order 4"
    ]

    # Compute optimized route
    optimized_route = optimize_delivery_routes(example_distance_matrix, example_orders)

    # Print the results
    if optimized_route:
        print("Optimized delivery route (order indices):", optimized_route)
        print("Delivery order descriptions:")
        for index in optimized_route:
            if index < len(example_orders):
                print(f"- {example_orders[index]}")
            else:
                print("- Depot")
```
