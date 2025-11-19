"""
Generated Code Metadata:
========================
Original URL: https://deploy-preview-200--nervous-kare-6f3c45.netlify.app
Prompt: Write a function in Python to calculate the optimal routes for recycling collection trucks within the City of York, minimizing fuel consumption and time.
Generated: DETERMINISTIC_9a32b6c89264c9ef
Batch ID: 20250612_151018
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from scipy.spatial import distance
from typing import List, Tuple

def calculate_optimal_routes(locations: List[Tuple[float, float]], 
                             depot: Tuple[float, float], 
                             num_trucks: int, 
                             truck_capacity: int) -> List[List[Tuple[float, float]]]:
    """
    Calculate the optimal routes for recycling collection trucks.

    Args:
    - locations (List[Tuple[float, float]]): List of (latitude, longitude) locations to visit.
    - depot (Tuple[float, float]): (latitude, longitude) of the depot.
    - num_trucks (int): Number of trucks available.
    - truck_capacity (int): Maximum number of locations each truck can visit.

    Returns:
    - List[List[Tuple[float, float]]]: List of routes, where each route is a list of (latitude, longitude) locations.
    """

    # Add depot to locations and create a distance matrix
    locations.append(depot)
    num_locations = len(locations)
    distance_matrix = np.zeros((num_locations, num_locations))

    for i in range(num_locations):
        for j in range(i+1, num_locations):
            dist = distance.euclidean(locations[i], locations[j])
            distance_matrix[i, j] = dist
            distance_matrix[j, i] = dist

    # Initialize routes and current location of each truck
    routes = [[] for _ in range(num_trucks)]
    current_locations = [depot] * num_trucks

    # Assign locations to trucks using a nearest neighbor approach
    unvisited_locations = set(locations[:-1])  # exclude depot
    while unvisited_locations:
        for truck_id in range(num_trucks):
            if len(routes[truck_id]) < truck_capacity and unvisited_locations:
                nearest_location = None
                min_distance = float('inf')
                for location in unvisited_locations:
                    dist = distance_matrix[locations.index(current_locations[truck_id]), locations.index(location)]
                    if dist < min_distance:
                        min_distance = dist
                        nearest_location = location
                if nearest_location:
                    routes[truck_id].append(nearest_location)
                    unvisited_locations.remove(nearest_location)
                    current_locations[truck_id] = nearest_location

    # Close each route by returning to the depot
    for truck_id in range(num_trucks):
        routes[truck_id].append(depot)

    return routes


def main():
    # Example usage
    locations = [(53.9577, -1.0823), (53.9583, -1.0804), (53.9592, -1.0811), 
                 (53.9601, -1.0795), (53.9611, -1.0829), (53.9622, -1.0818)]
    depot = (53.9585, -1.0813)
    num_trucks = 2
    truck_capacity = 3

    try:
        routes = calculate_optimal_routes(locations, depot, num_trucks, truck_capacity)
        for i, route in enumerate(routes):
            print(f"Route {i+1}: {route}")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
