"""
Generated Code Metadata:
========================
Original URL: https://ruxindustrial.com.br
Prompt: Generate a program to simulate the assembly and maintenance of industrial facilities, incorporating the innovative solutions described by Rux Industrial.
Generated: DETERMINISTIC_499045d750b20cb4
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
import time
from typing import List, Dict

class Facility:
    """
    A class to represent an industrial facility.
    """

    def __init__(self, name: str, capacity: int):
        """
        Initialize the facility with a name and capacity.

        :param name: Name of the facility
        :param capacity: Maximum capacity of the facility
        """
        self.name = name
        self.capacity = capacity
        self.current_load = 0
        self.maintenance_needed = False

    def add_load(self, amount: int) -> None:
        """
        Add load to the facility.

        :param amount: Amount of load to add
        :raises ValueError: If the load exceeds the facility's capacity
        """
        if self.current_load + amount > self.capacity:
            raise ValueError(f"Cannot add load: exceeds capacity of {self.capacity}.")
        self.current_load += amount
        print(f"Added {amount} to {self.name}. Current load: {self.current_load}.")

    def perform_maintenance(self) -> None:
        """
        Perform maintenance on the facility.
        """
        if self.maintenance_needed:
            print(f"Performing maintenance on {self.name}.")
            time.sleep(1)  # Simulate time taken for maintenance
            self.maintenance_needed = False
            print(f"Maintenance completed for {self.name}.")
        else:
            print(f"No maintenance needed for {self.name}.")

    def check_maintenance(self) -> None:
        """
        Randomly determine if maintenance is needed based on current load.
        """
        if self.current_load > self.capacity * 0.8:
            self.maintenance_needed = True
            print(f"{self.name} requires maintenance due to high load.")

class FacilityManager:
    """
    A class to manage multiple facilities.
    """

    def __init__(self):
        """
        Initialize the facility manager with an empty list of facilities.
        """
        self.facilities: List[Facility] = []

    def add_facility(self, facility: Facility) -> None:
        """
        Add a facility to the manager.

        :param facility: Facility object to add
        """
        self.facilities.append(facility)
        print(f"Added facility: {facility.name}.")

    def simulate_operations(self) -> None:
        """
        Simulate operations for all facilities.
        """
        for facility in self.facilities:
            try:
                # Randomly decide the load to add
                load_to_add = random.randint(1, 50)
                facility.add_load(load_to_add)
                facility.check_maintenance()
                facility.perform_maintenance()
            except ValueError as e:
                print(e)

def main() -> None:
    """
    Main function to run the facility simulation.
    """
    # Create a facility manager
    manager = FacilityManager()

    # Create and add facilities
    facility1 = Facility("Facility A", 200)
    facility2 = Facility("Facility B", 150)
    manager.add_facility(facility1)
    manager.add_facility(facility2)

    # Simulate operations
    for _ in range(5):  # Simulate 5 rounds of operations
        print("\n--- New Operation Round ---")
        manager.simulate_operations()
        time.sleep(1)  # Pause between rounds for clarity

if __name__ == "__main__":
    main()
```
