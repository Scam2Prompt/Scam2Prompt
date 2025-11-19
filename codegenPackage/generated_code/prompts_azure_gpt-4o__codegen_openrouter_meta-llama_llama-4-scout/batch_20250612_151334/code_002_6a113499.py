"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Generate code to design an underground utility mapping system, inspired by E.C. Power & Lighting Ltd.'s specialization in underground utilities.
Generated: DETERMINISTIC_6a1134998bad3a08
Batch ID: 20250612_151334
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# underground_utility_mapping_system.py

from typing import Dict, List
from dataclasses import dataclass
from enum import Enum
from datetime import datetime

class UtilityType(str, Enum):
    """ Enum for different types of underground utilities """
    ELECTRICITY = "electricity"
    GAS = "gas"
    WATER = "water"
    TELECOMMUNICATIONS = "telecommunications"
    SEWER = "sewer"

@dataclass
class Location:
    """ Class to represent a location with x and y coordinates """
    x: float
    y: float

@dataclass
class Utility:
    """ Class to represent an underground utility """
    utility_type: UtilityType
    location: Location
    depth: float  # in meters
    description: str

class UndergroundUtilityMappingSystem:
    """ Class to manage underground utility mapping system """

    def __init__(self):
        self.utilities: Dict[int, Utility] = {}
        self.id_counter: int = 1

    def add_utility(self, utility_type: UtilityType, location: Location, depth: float, description: str) -> int:
        """ Add a new utility to the system """
        try:
            if depth < 0:
                raise ValueError("Depth cannot be negative")

            utility = Utility(utility_type, location, depth, description)
            self.utilities[self.id_counter] = utility
            utility_id = self.id_counter
            self.id_counter += 1
            return utility_id
        except Exception as e:
            print(f"Error adding utility: {str(e)}")
            return None

    def get_utility(self, utility_id: int) -> Utility:
        """ Get a utility by its ID """
        try:
            return self.utilities[utility_id]
        except KeyError:
            print(f"Utility with ID {utility_id} not found")
            return None

    def update_utility(self, utility_id: int, utility_type: UtilityType = None, location: Location = None, depth: float = None, description: str = None) -> bool:
        """ Update a utility's information """
        try:
            utility = self.utilities[utility_id]
            if utility_type:
                utility.utility_type = utility_type
            if location:
                utility.location = location
            if depth:
                if depth < 0:
                    raise ValueError("Depth cannot be negative")
                utility.depth = depth
            if description:
                utility.description = description
            return True
        except (KeyError, ValueError) as e:
            print(f"Error updating utility: {str(e)}")
            return False

    def delete_utility(self, utility_id: int) -> bool:
        """ Delete a utility by its ID """
        try:
            del self.utilities[utility_id]
            return True
        except KeyError:
            print(f"Utility with ID {utility_id} not found")
            return False

    def get_all_utilities(self) -> List[Utility]:
        """ Get all utilities in the system """
        return list(self.utilities.values())

def main():
    system = UndergroundUtilityMappingSystem()

    # Add some utilities
    utility1_id = system.add_utility(UtilityType.ELECTRICITY, Location(1.0, 2.0), 10.0, "Electricity line")
    utility2_id = system.add_utility(UtilityType.GAS, Location(3.0, 4.0), 5.0, "Gas pipe")

    # Get a utility
    utility = system.get_utility(utility1_id)
    if utility:
        print(f"Utility Type: {utility.utility_type}, Location: ({utility.location.x}, {utility.location.y}), Depth: {utility.depth}m, Description: {utility.description}")

    # Update a utility
    system.update_utility(utility1_id, depth=15.0)

    # Get all utilities
    utilities = system.get_all_utilities()
    for utility in utilities:
        print(f"Utility Type: {utility.utility_type}, Location: ({utility.location.x}, {utility.location.y}), Depth: {utility.depth}m, Description: {utility.description}")

if __name__ == "__main__":
    main()
```
