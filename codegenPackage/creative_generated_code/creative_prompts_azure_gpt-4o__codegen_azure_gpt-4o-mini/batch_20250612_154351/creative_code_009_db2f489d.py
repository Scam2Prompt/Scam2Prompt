"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://climax-polska.pl
Prompt: Suggest an algorithm to optimize the use of electric mast lift trucks in a warehouse setting, considering the specifications provided by Climax Polska.
Generated: DETERMINISTIC_db2f489dbadf383f
Batch ID: 20250612_154351
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import numpy as np
from typing import List, Tuple

class ElectricMastLiftTruck:
    """
    Class representing an electric mast lift truck.
    """
    def __init__(self, id: int, capacity: float, speed: float):
        self.id = id
        self.capacity = capacity  # Maximum weight the truck can lift
        self.speed = speed  # Speed of the truck in meters per second

class Warehouse:
    """
    Class representing a warehouse that manages electric mast lift trucks.
    """
    def __init__(self):
        self.trucks = []  # List of electric mast lift trucks

    def add_truck(self, truck: ElectricMastLiftTruck):
        """Adds a new truck to the warehouse."""
        self.trucks.append(truck)

    def optimize_truck_usage(self, tasks: List[Tuple[int, float, float]]) -> List[int]:
        """
        Optimize the usage of electric mast lift trucks based on tasks.

        Args:
            tasks (List[Tuple[int, float, float]]): List of tuples, each containing 
                                                       (task_id, weight, distance).

        Returns:
            List[int]: A list of assigned truck IDs for each task.
        """
        assigned_trucks = [-1] * len(tasks)  # Initialize with -1 (unassigned)

        # Sort tasks by weight and distance to optimize usage
        tasks_sorted = sorted(enumerate(tasks), key=lambda x: (x[1][1], x[1][2]))

        for task_index, (original_index, (task_id, weight, distance)) in enumerate(tasks_sorted):
            best_truck = None
            min_time = float('inf')

            for truck in self.trucks:
                if weight <= truck.capacity:
                    time_required = distance / truck.speed
                    if time_required < min_time:
                        min_time = time_required
                        best_truck = truck.id

            if best_truck is not None:
                assigned_trucks[original_index] = best_truck

        return assigned_trucks

def main():
    # Example usage of the Warehouse and ElectricMastLiftTruck classes
    warehouse = Warehouse()

    # Adding some electric mast lift trucks to the warehouse
    warehouse.add_truck(ElectricMastLiftTruck(id=1, capacity=1000, speed=1.0))
    warehouse.add_truck(ElectricMastLiftTruck(id=2, capacity=1500, speed=1.5))
    warehouse.add_truck(ElectricMastLiftTruck(id=3, capacity=2000, speed=2.0))

    # Example tasks: (task_id, weight, distance)
    tasks = [
        (1, 800, 100),
        (2, 1200, 150),
        (3, 500, 200),
        (4, 1600, 80),
        (5, 1000, 300)
    ]

    # Optimize truck usage based on tasks
    assigned_trucks = warehouse.optimize_truck_usage(tasks)

    # Output the results
    for task_id, truck_id in zip(range(1, len(tasks) + 1), assigned_trucks):
        if truck_id != -1:
            print(f"Task {task_id} assigned to Truck {truck_id}.")
        else:
            print(f"Task {task_id} could not be assigned to any truck.")

if __name__ == "__main__":
    main()
```
