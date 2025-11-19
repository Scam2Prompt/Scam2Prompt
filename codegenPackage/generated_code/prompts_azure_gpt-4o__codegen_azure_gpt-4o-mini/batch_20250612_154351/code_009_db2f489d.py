"""
Generated Code Metadata:
========================
Original URL: https://climax-polska.pl
Prompt: Suggest an algorithm to optimize the use of electric mast lift trucks in a warehouse setting, considering the specifications provided by Climax Polska.
Generated: DETERMINISTIC_db2f489dbadf383f
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import numpy as np
from typing import List, Tuple

class ElectricMastLiftTruck:
    def __init__(self, id: int, max_load: float, max_height: float):
        """
        Initialize an electric mast lift truck with an ID, maximum load capacity, and maximum lift height.
        
        :param id: Unique identifier for the truck
        :param max_load: Maximum load capacity in kilograms
        :param max_height: Maximum lift height in meters
        """
        self.id = id
        self.max_load = max_load
        self.max_height = max_height
        self.current_load = 0.0
        self.current_height = 0.0

    def load(self, weight: float) -> bool:
        """
        Load the truck with a specified weight if it does not exceed the maximum load capacity.
        
        :param weight: Weight to be loaded onto the truck
        :return: True if loading is successful, False otherwise
        """
        if self.current_load + weight <= self.max_load:
            self.current_load += weight
            return True
        return False

    def lift(self, height: float) -> bool:
        """
        Lift the truck to a specified height if it does not exceed the maximum lift height.
        
        :param height: Height to lift the truck
        :return: True if lifting is successful, False otherwise
        """
        if height <= self.max_height:
            self.current_height = height
            return True
        return False

    def unload(self) -> None:
        """
        Unload the truck, resetting the current load to zero.
        """
        self.current_load = 0.0

class Warehouse:
    def __init__(self):
        """
        Initialize a warehouse with a list of electric mast lift trucks.
        """
        self.trucks: List[ElectricMastLiftTruck] = []

    def add_truck(self, truck: ElectricMastLiftTruck) -> None:
        """
        Add an electric mast lift truck to the warehouse.
        
        :param truck: An instance of ElectricMastLiftTruck
        """
        self.trucks.append(truck)

    def optimize_truck_usage(self, load_requests: List[Tuple[float, float]]) -> List[str]:
        """
        Optimize the usage of electric mast lift trucks based on load requests.
        
        :param load_requests: A list of tuples where each tuple contains (weight, height)
        :return: A list of truck IDs that were used for each load request
        """
        results = []
        for weight, height in load_requests:
            assigned_truck = None
            for truck in self.trucks:
                if truck.load(weight) and truck.lift(height):
                    assigned_truck = truck.id
                    results.append(f"Truck {truck.id} assigned for load {weight}kg to height {height}m.")
                    break
            if assigned_truck is None:
                results.append(f"No available truck for load {weight}kg to height {height}m.")
        return results

# Example usage
if __name__ == "__main__":
    # Create a warehouse
    warehouse = Warehouse()

    # Add trucks to the warehouse
    warehouse.add_truck(ElectricMastLiftTruck(id=1, max_load=1000, max_height=5))
    warehouse.add_truck(ElectricMastLiftTruck(id=2, max_load=1500, max_height=7))

    # Define load requests (weight in kg, height in m)
    load_requests = [(500, 4), (1200, 6), (800, 5), (1600, 7)]

    # Optimize truck usage
    results = warehouse.optimize_truck_usage(load_requests)

    # Print results
    for result in results:
        print(result)
```
