"""
Generated Code Metadata:
========================
Original URL: https://enyakinvidanjor.com
Prompt: Write a Python script to simulate a sewage system cleaning process using a vidanjör truck, considering various pipe diameters and blockage types.
Generated: DETERMINISTIC_d85d5e2ae5e8c3e1
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import random
from enum import Enum
from typing import List

class BlockageType(Enum):
    """ Enum for blockage types """
    GREASE = 1
    DEBRIS = 2
    ROOT_INTRUSION = 3
    MINERAL_DEPOSIT = 4

class Pipe:
    """ Represents a pipe in the sewage system """
    def __init__(self, diameter: float, blockage_type: BlockageType = None, blockage_severity: float = 0.0):
        """
        Initializes a Pipe object.

        Args:
        diameter (float): The diameter of the pipe.
        blockage_type (BlockageType, optional): The type of blockage. Defaults to None.
        blockage_severity (float, optional): The severity of the blockage (0.0 - 1.0). Defaults to 0.0.
        """
        self.diameter = diameter
        self.blockage_type = blockage_type
        self.blockage_severity = blockage_severity

class VidanjorTruck:
    """ Simulates a vidanjör truck for sewage system cleaning """
    def __init__(self, capacity: float, pressure: float):
        """
        Initializes a VidanjorTruck object.

        Args:
        capacity (float): The capacity of the truck's tank.
        pressure (float): The pressure of the truck's pump.
        """
        self.capacity = capacity
        self.pressure = pressure

    def clean_pipe(self, pipe: Pipe) -> bool:
        """
        Simulates cleaning a pipe.

        Args:
        pipe (Pipe): The pipe to clean.

        Returns:
        bool: True if the pipe was cleaned successfully, False otherwise.
        """
        if pipe.blockage_type is None:
            print(f"Pipe with diameter {pipe.diameter} is already clean.")
            return True

        # Simulate cleaning process
        cleaning_success = self.pressure > (pipe.blockage_severity * 10)
        if cleaning_success:
            print(f"Successfully cleaned pipe with diameter {pipe.diameter} and blockage type {pipe.blockage_type.name}.")
            pipe.blockage_type = None
            pipe.blockage_severity = 0.0
        else:
            print(f"Failed to clean pipe with diameter {pipe.diameter} and blockage type {pipe.blockage_type.name}.")

        return cleaning_success

def simulate_sewage_system_cleaning(truck: VidanjorTruck, pipes: List[Pipe]) -> None:
    """
    Simulates the sewage system cleaning process.

    Args:
    truck (VidanjorTruck): The vidanjör truck used for cleaning.
    pipes (List[Pipe]): The list of pipes to clean.
    """
    for pipe in pipes:
        truck.clean_pipe(pipe)

def main() -> None:
    try:
        # Create a vidanjör truck
        truck = VidanjorTruck(capacity=1000.0, pressure=50.0)

        # Create pipes with various diameters and blockage types
        pipes = [
            Pipe(diameter=20.0, blockage_type=BlockageType.GREASE, blockage_severity=0.5),
            Pipe(diameter=30.0, blockage_type=BlockageType.DEBRIS, blockage_severity=0.8),
            Pipe(diameter=40.0),
            Pipe(diameter=10.0, blockage_type=BlockageType.ROOT_INTRUSION, blockage_severity=0.2),
            Pipe(diameter=25.0, blockage_type=BlockageType.MINERAL_DEPOSIT, blockage_severity=0.6),
        ]

        # Simulate sewage system cleaning
        simulate_sewage_system_cleaning(truck, pipes)

    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
```
