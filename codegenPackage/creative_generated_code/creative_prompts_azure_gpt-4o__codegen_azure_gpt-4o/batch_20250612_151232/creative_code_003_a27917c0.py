"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://enlconsortium.com
Prompt: Develop a logistics optimization algorithm for ENL Consortium's haulage system, considering truck fleet types (flatbeds, low loaders) and routes for local and up-country cargo transportation.
Generated: DETERMINISTIC_a27917c0d78a89ef
Batch ID: 20250612_151232
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import itertools
from typing import List, Dict, Tuple

# Define constants for truck fleet types and route categories
TRUCK_TYPES = {
    "flatbed": {"capacity": 20, "base_cost": 500},
    "low_loader": {"capacity": 50, "base_cost": 1200},
}

ROUTE_TYPES = {
    "local": {"distance_limit": 100, "cost_per_km": 5},
    "up_country": {"distance_limit": 1000, "cost_per_km": 10},
}

class LogisticsOptimizer:
    """
    A class to optimize logistics operations for ENL Consortium's haulage system.
    """

    def __init__(self, truck_types: Dict, route_types: Dict):
        """
        Initialize the logistics optimizer with truck and route information.
        """
        self.truck_types = truck_types
        self.route_types = route_types

    def optimize_routes(
        self, cargo_requests: List[Dict], available_trucks: List[Dict]
    ) -> List[Dict]:
        """
        Optimize truck assignments and routes based on cargo requests and available trucks.
        
        Parameters:
            cargo_requests (List[Dict]): List of cargo requests with required capacity and route distance.
            available_trucks (List[Dict]): List of available trucks and their types.
        
        Returns:
            List[Dict]: Optimized assignments with trucks and routes.
        """
        try:
            optimized_assignments = []  # Store the results of optimized assignments

            # Sort cargo requests by distance (ascending) for optimization
            cargo_requests.sort(key=lambda x: x["distance"])

            # Iterate through cargo requests
            for cargo in cargo_requests:
                assigned = False
                for truck in available_trucks:
                    # Check if truck type matches cargo capacity and distance requirements
                    truck_type = self.truck_types[truck["type"]]
                    route_type = (
                        self.route_types["local"]
                        if cargo["distance"] <= self.route_types["local"]["distance_limit"]
                        else self.route_types["up_country"]
                    )

                    if (
                        truck_type["capacity"] >= cargo["capacity"]
                        and cargo["distance"] <= route_type["distance_limit"]
                    ):
                        # Calculate cost
                        cost = (
                            truck_type["base_cost"]
                            + cargo["distance"] * route_type["cost_per_km"]
                        )

                        optimized_assignments.append(
                            {
                                "cargo_id": cargo["id"],
                                "truck_id": truck["id"],
                                "truck_type": truck["type"],
                                "route_type": "local"
                                if cargo["distance"]
                                <= self.route_types["local"]["distance_limit"]
                                else "up_country",
                                "cost": cost,
                            }
                        )
                        available_trucks.remove(truck)  # Remove assigned truck from available list
                        assigned = True
                        break

                if not assigned:
                    optimized_assignments.append(
                        {
                            "cargo_id": cargo["id"],
                            "truck_id": None,
                            "truck_type": None,
                            "route_type": None,
                            "cost": None,
                            "status": "No available trucks match the requirements",
                        }
                    )

            return optimized_assignments

        except Exception as e:
            # Log error details for debugging
            print(f"Error during optimization: {e}")
            return []

def main():
    # Example input data: cargo requests and available trucks
    cargo_requests = [
        {"id": 1, "capacity": 15, "distance": 50},
        {"id": 2, "capacity": 40, "distance": 400},
        {"id": 3, "capacity": 60, "distance": 1200},
    ]

    available_trucks = [
        {"id": "T1", "type": "flatbed"},
        {"id": "T2", "type": "low_loader"},
        {"id": "T3", "type": "flatbed"},
    ]

    # Initialize the optimizer
    optimizer = LogisticsOptimizer(TRUCK_TYPES, ROUTE_TYPES)

    # Perform optimization
    optimized_results = optimizer.optimize_routes(cargo_requests, available_trucks)

    # Print results
    print("Optimized Assignments:")
    for result in optimized_results:
        print(result)


if __name__ == "__main__":
    main()
```
