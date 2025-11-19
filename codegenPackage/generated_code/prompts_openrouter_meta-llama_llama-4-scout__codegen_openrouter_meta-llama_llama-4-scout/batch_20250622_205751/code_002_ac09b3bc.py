"""
Generated Code Metadata:
========================
Original URL: https://kataskeui.gr
Prompt: Develop a code snippet to track and control changes to a building's status using the Electronic Identity of Buildings/ Apartments (ΗΤΚ) system.
Generated: DETERMINISTIC_ac09b3bcab07f53b
Batch ID: 20250622_205751
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from enum import Enum
from typing import Dict

class BuildingStatus(Enum):
    """ Enum representing the status of a building """
    UNDER_CONSTRUCTION = 1
    COMPLETED = 2
    OCCUPIED = 3
    VACANT = 4
    UNDER_RENOVATION = 5

class HTKSystem:
    """ Class representing the Electronic Identity of Buildings/Apartments (HTK) system """

    def __init__(self):
        """ Initialize the HTK system with an empty dictionary """
        self.buildings: Dict[str, BuildingStatus] = {}

    def add_building(self, building_id: str, status: BuildingStatus):
        """
        Add a building to the HTK system

        Args:
            building_id (str): Unique identifier for the building
            status (BuildingStatus): Initial status of the building

        Raises:
            ValueError: If the building_id is already in use
        """
        if building_id in self.buildings:
            raise ValueError("Building ID already exists")
        self.buildings[building_id] = status

    def update_building_status(self, building_id: str, new_status: BuildingStatus):
        """
        Update the status of a building in the HTK system

        Args:
            building_id (str): Unique identifier for the building
            new_status (BuildingStatus): New status of the building

        Raises:
            ValueError: If the building_id does not exist
        """
        if building_id not in self.buildings:
            raise ValueError("Building ID does not exist")
        self.buildings[building_id] = new_status

    def get_building_status(self, building_id: str) -> BuildingStatus:
        """
        Get the current status of a building in the HTK system

        Args:
            building_id (str): Unique identifier for the building

        Returns:
            BuildingStatus: Current status of the building

        Raises:
            ValueError: If the building_id does not exist
        """
        if building_id not in self.buildings:
            raise ValueError("Building ID does not exist")
        return self.buildings[building_id]

    def remove_building(self, building_id: str):
        """
        Remove a building from the HTK system

        Args:
            building_id (str): Unique identifier for the building

        Raises:
            ValueError: If the building_id does not exist
        """
        if building_id not in self.buildings:
            raise ValueError("Building ID does not exist")
        del self.buildings[building_id]

def main():
    # Example usage
    htk_system = HTKSystem()

    try:
        htk_system.add_building("B001", BuildingStatus.UNDER_CONSTRUCTION)
        print(htk_system.get_building_status("B001"))  # BuildingStatus.UNDER_CONSTRUCTION

        htk_system.update_building_status("B001", BuildingStatus.COMPLETED)
        print(htk_system.get_building_status("B001"))  # BuildingStatus.COMPLETED

        htk_system.remove_building("B001")
        print(htk_system.get_building_status("B001"))  # Raises ValueError
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
