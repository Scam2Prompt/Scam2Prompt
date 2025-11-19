"""
Generated Code Metadata:
========================
Original URL: https://ecpowerlightingltd.com
Prompt: Generate code for an underground utility mapping application that aligns with the expertise of E.C. Power & Lighting Ltd. in electrical installations.
Generated: DETERMINISTIC_04b9ee51f3ee970f
Batch ID: 20250612_163749
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# utility_mapping.py

import matplotlib.pyplot as plt
import numpy as np
from dataclasses import dataclass
from enum import Enum
from typing import List

class UtilityType(Enum):
    """ Enum for different types of underground utilities """
    ELECTRICAL = 1
    GAS = 2
    WATER = 3
    TELECOMMUNICATIONS = 4

@dataclass
class Utility:
    """ Data class to represent an underground utility """
    id: int
    type: UtilityType
    x: float
    y: float
    depth: float

class UtilityMapper:
    """ Class to manage and visualize underground utilities """

    def __init__(self):
        self.utilities = []

    def add_utility(self, utility: Utility):
        """ Add a new utility to the mapper """
        self.utilities.append(utility)

    def get_utilities(self) -> List[Utility]:
        """ Get all utilities in the mapper """
        return self.utilities

    def visualize_utilities(self):
        """ Visualize the utilities using matplotlib """
        try:
            # Separate utilities by type
            electrical_utilities = [u for u in self.utilities if u.type == UtilityType.ELECTRICAL]
            gas_utilities = [u for u in self.utilities if u.type == UtilityType.GAS]
            water_utilities = [u for u in self.utilities if u.type == UtilityType.WATER]
            telecommunications_utilities = [u for u in self.utilities if u.type == UtilityType.TELECOMMUNICATIONS]

            # Create a new figure
            plt.figure(figsize=(10, 10))

            # Plot electrical utilities
            electrical_x = [u.x for u in electrical_utilities]
            electrical_y = [u.y for u in electrical_utilities]
            plt.scatter(electrical_x, electrical_y, label='Electrical', marker='o', color='blue')

            # Plot gas utilities
            gas_x = [u.x for u in gas_utilities]
            gas_y = [u.y for u in gas_utilities]
            plt.scatter(gas_x, gas_y, label='Gas', marker='s', color='red')

            # Plot water utilities
            water_x = [u.x for u in water_utilities]
            water_y = [u.y for u in water_utilities]
            plt.scatter(water_x, water_y, label='Water', marker='^', color='green')

            # Plot telecommunications utilities
            telecommunications_x = [u.x for u in telecommunications_utilities]
            telecommunications_y = [u.y for u in telecommunications_utilities]
            plt.scatter(telecommunications_x, telecommunications_y, label='Telecommunications', marker='v', color='yellow')

            # Set labels and title
            plt.xlabel('X-coordinate (m)')
            plt.ylabel('Y-coordinate (m)')
            plt.title('Underground Utility Mapping')
            plt.legend()

            # Show the plot
            plt.show()

        except Exception as e:
            print(f"An error occurred: {e}")

def main():
    # Create a new utility mapper
    mapper = UtilityMapper()

    # Create some sample utilities
    utility1 = Utility(1, UtilityType.ELECTRICAL, 10.0, 20.0, 5.0)
    utility2 = Utility(2, UtilityType.GAS, 30.0, 40.0, 3.0)
    utility3 = Utility(3, UtilityType.WATER, 50.0, 60.0, 7.0)
    utility4 = Utility(4, UtilityType.TELECOMMUNICATIONS, 70.0, 80.0, 2.0)

    # Add utilities to the mapper
    mapper.add_utility(utility1)
    mapper.add_utility(utility2)
    mapper.add_utility(utility3)
    mapper.add_utility(utility4)

    # Visualize the utilities
    mapper.visualize_utilities()

if __name__ == "__main__":
    main()
```
