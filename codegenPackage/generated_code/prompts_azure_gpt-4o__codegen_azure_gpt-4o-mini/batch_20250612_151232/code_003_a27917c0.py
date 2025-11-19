"""
Generated Code Metadata:
========================
Original URL: https://enlconsortium.com
Prompt: Develop a logistics optimization algorithm for ENL Consortium's haulage system, considering truck fleet types (flatbeds, low loaders) and routes for local and up-country cargo transportation.
Generated: DETERMINISTIC_a27917c0d78a89ef
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Tuple, Dict

class Truck:
    """Class representing a truck in the fleet."""
    def __init__(self, truck_id: str, truck_type: str, capacity: float):
        self.truck_id = truck_id
        self.truck_type = truck_type
        self.capacity = capacity

class Route:
    """Class representing a transportation route."""
    def __init__(self, route_id: str, distance: float, cargo_weight: float):
        self.route_id = route_id
        self.distance = distance
        self.cargo_weight = cargo_weight

class LogisticsOptimizer:
    """Class to optimize logistics for the haulage system."""
    
    def __init__(self, trucks: List[Truck], routes: List[Route]):
        self.trucks = trucks
        self.routes = routes

    def optimize_routes(self) -> Dict[str, List[str]]:
        """
        Optimize routes based on truck capacity and cargo weight.
        
        Returns:
            A dictionary mapping truck IDs to the list of route IDs they can take.
        """
        allocation = {}
        
        for truck in self.trucks:
            allocation[truck.truck_id] = []
            for route in self.routes:
                if truck.capacity >= route.cargo_weight:
                    allocation[truck.truck_id].append(route.route_id)
        
        return allocation

def main():
    """Main function to run the logistics optimization."""
    # Sample truck fleet
    trucks = [
        Truck("T1", "Flatbed", 1000.0),
        Truck("T2", "Low Loader", 2000.0),
        Truck("T3", "Flatbed", 1500.0)
    ]
    
    # Sample routes
    routes = [
        Route("R1", 50.0, 800.0),
        Route("R2", 120.0, 1500.0),
        Route("R3", 200.0, 2500.0),
        Route("R4", 75.0, 600.0)
    ]
    
    # Initialize the optimizer
    optimizer = LogisticsOptimizer(trucks, routes)
    
    try:
        # Optimize routes
        allocation = optimizer.optimize_routes()
        
        # Display the allocation results
        for truck_id, route_ids in allocation.items():
            print(f"Truck {truck_id} can take routes: {', '.join(route_ids) if route_ids else 'None'}")
    
    except Exception as e:
        print(f"An error occurred during optimization: {e}")

if __name__ == "__main__":
    main()
```
