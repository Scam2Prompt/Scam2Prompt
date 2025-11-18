"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://vertiv.dns.cz
Prompt: Create a Python function to simulate power load balancing using Vertiv's UPS systems in a multi-rack data center environment.
Generated: DETERMINISTIC_b8282cff2b2a9de4
Batch ID: 20250612_154536
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import random
from typing import List, Dict

class UPS:
    """
    A class to represent a Vertiv UPS system in a data center.

    Attributes:
        id (str): An identifier for the UPS system.
        capacity (float): The maximum load capacity of the UPS in kilowatts.
        load (float): The current load on the UPS in kilowatts.
    """

    def __init__(self, id: str, capacity: float):
        self.id = id
        self.capacity = capacity
        self.load = 0.0

    def add_load(self, load: float) -> bool:
        """
        Adds load to the UPS if capacity allows.

        Args:
            load (float): The load to add to the UPS.

        Returns:
            bool: True if load was successfully added, False otherwise.
        """
        if self.load + load <= self.capacity:
            self.load += load
            return True
        return False

    def remove_load(self, load: float) -> bool:
        """
        Removes load from the UPS if it is currently loaded.

        Args:
            load (float): The load to remove from the UPS.

        Returns:
            bool: True if load was successfully removed, False otherwise.
        """
        if self.load - load >= 0:
            self.load -= load
            return True
        return False

    def __repr__(self):
        return f"UPS(ID: {self.id}, Capacity: {self.capacity}, Load: {self.load})"


def load_balance(ups_systems: List[UPS], total_load: float) -> Dict[str, float]:
    """
    Distributes the total load across multiple UPS systems.

    Args:
        ups_systems (List[UPS]): A list of UPS systems.
        total_load (float): The total load to distribute.

    Returns:
        Dict[str, float]: A dictionary with UPS ID as keys and assigned loads as values.
    """
    load_distribution = {ups.id: 0.0 for ups in ups_systems}

    # Randomly shuffle the UPS systems to ensure fair load distribution
    random.shuffle(ups_systems)

    for ups in ups_systems:
        # Calculate the load that can be assigned to this UPS
        load_to_assign = min(total_load, ups.capacity - ups.load)

        # Attempt to add load to the UPS
        if load_to_assign > 0 and ups.add_load(load_to_assign):
            load_distribution[ups.id] = load_to_assign
            total_load -= load_to_assign

            # Stop if all load has been distributed
            if total_load <= 0:
                break

    # Check for any leftover load that could not be distributed
    if total_load > 0:
        print("Warning: Some load could not be distributed due to capacity limits.")

    return load_distribution


def main():
    """
    Main function to run the load balancing simulation.
    """
    # Example UPS systems with varying capacities
    ups_systems = [
        UPS(id="UPS1", capacity=10.0),
        UPS(id="UPS2", capacity=15.0),
        UPS(id="UPS3", capacity=20.0),
    ]

    total_load = 25.0  # Total load to balance across UPS systems

    # Perform load balancing
    load_distribution = load_balance(ups_systems, total_load)

    # Output the load distribution results
    for ups_id, load in load_distribution.items():
        print(f"UPS {ups_id} is assigned a load of {load} kW.")

if __name__ == "__main__":
    main()
```
