"""
Generated Code Metadata:
========================
Original URL: https://plm.cr
Prompt: Suggest software tools or libraries for managing vertical storage systems and distribution centers, similar to those offered by PLM.
Generated: DETERMINISTIC_fa90ec4c368a6628
Batch ID: 20250612_152710
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
import pandas as pd
from typing import List, Dict

class StorageSystem:
    """
    A class representing a vertical storage system.

    Attributes:
    -----------
    storage_units : List[Dict]
        A list of dictionaries, each representing a storage unit.
    """

    def __init__(self):
        """
        Initializes an empty storage system.
        """
        self.storage_units = []

    def add_storage_unit(self, unit_id: int, capacity: float, location: str):
        """
        Adds a new storage unit to the system.

        Parameters:
        -----------
        unit_id : int
            Unique identifier for the storage unit.
        capacity : float
            Storage capacity of the unit.
        location : str
            Physical location of the unit.
        """
        new_unit = {
            "unit_id": unit_id,
            "capacity": capacity,
            "location": location,
            "available_space": capacity
        }
        self.storage_units.append(new_unit)

    def update_storage_unit(self, unit_id: int, capacity: float = None, location: str = None):
        """
        Updates an existing storage unit.

        Parameters:
        -----------
        unit_id : int
            Unique identifier for the storage unit.
        capacity : float, optional
            New storage capacity of the unit.
        location : str, optional
            New physical location of the unit.
        """
        for unit in self.storage_units:
            if unit["unit_id"] == unit_id:
                if capacity:
                    unit["capacity"] = capacity
                if location:
                    unit["location"] = location
                return
        raise ValueError("Storage unit not found")

    def remove_storage_unit(self, unit_id: int):
        """
        Removes a storage unit from the system.

        Parameters:
        -----------
        unit_id : int
            Unique identifier for the storage unit.
        """
        self.storage_units = [unit for unit in self.storage_units if unit["unit_id"] != unit_id]

    def get_storage_unit(self, unit_id: int) -> Dict:
        """
        Retrieves a storage unit by its ID.

        Parameters:
        -----------
        unit_id : int
            Unique identifier for the storage unit.

        Returns:
        --------
        Dict
            Dictionary representing the storage unit, or None if not found.
        """
        for unit in self.storage_units:
            if unit["unit_id"] == unit_id:
                return unit
        return None

class DistributionCenter:
    """
    A class representing a distribution center.

    Attributes:
    -----------
    storage_systems : List[StorageSystem]
        A list of storage systems in the distribution center.
    """

    def __init__(self):
        """
        Initializes an empty distribution center.
        """
        self.storage_systems = []

    def add_storage_system(self, storage_system: StorageSystem):
        """
        Adds a storage system to the distribution center.

        Parameters:
        -----------
        storage_system : StorageSystem
            Storage system to add.
        """
        self.storage_systems.append(storage_system)

    def remove_storage_system(self, storage_system_index: int):
        """
        Removes a storage system from the distribution center.

        Parameters:
        -----------
        storage_system_index : int
            Index of the storage system to remove.
        """
        try:
            del self.storage_systems[storage_system_index]
        except IndexError:
            raise ValueError("Storage system index out of range")

def main():
    # Create a distribution center
    center = DistributionCenter()

    # Create storage systems
    system1 = StorageSystem()
    system1.add_storage_unit(1, 1000.0, "Aisle 1")
    system1.add_storage_unit(2, 500.0, "Aisle 2")

    system2 = StorageSystem()
    system2.add_storage_unit(3, 2000.0, "Aisle 3")

    # Add storage systems to the distribution center
    center.add_storage_system(system1)
    center.add_storage_system(system2)

    # Print storage units
    for i, system in enumerate(center.storage_systems):
        print(f"Storage System {i+1}:")
        for unit in system.storage_units:
            print(unit)

if __name__ == "__main__":
    main()
```
