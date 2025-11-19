"""
Generated Code Metadata:
========================
Original URL: https://mail.dexodoor.com
Prompt: Provide a Python function to model sliding and casement door mechanisms, using the types of doors mentioned on the Dexodoor site.
Generated: DETERMINISTIC_f617747ce7768ab4
Batch ID: 20250612_152441
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from abc import ABC, abstractmethod
from enum import Enum

# Define an enumeration for door types
class DoorType(Enum):
    """Enumeration for door types."""
    SLIDING = 1
    CASEMENT = 2

# Abstract base class for doors
class Door(ABC):
    """Abstract base class for doors."""

    def __init__(self, door_type, material, size):
        """
        Initialize a door.

        Args:
            door_type (DoorType): The type of door.
            material (str): The material of the door.
            size (str): The size of the door.
        """
        self.door_type = door_type
        self.material = material
        self.size = size

    @abstractmethod
    def open(self):
        """Open the door."""
        pass

    @abstractmethod
    def close(self):
        """Close the door."""
        pass

# Sliding door class
class SlidingDoor(Door):
    """Class for sliding doors."""

    def __init__(self, material, size, num_panels):
        """
        Initialize a sliding door.

        Args:
            material (str): The material of the door.
            size (str): The size of the door.
            num_panels (int): The number of panels.
        """
        super().__init__(DoorType.SLIDING, material, size)
        self.num_panels = num_panels
        self.is_open = False

    def open(self):
        """Open the sliding door."""
        if not self.is_open:
            print(f"The {self.material} sliding door with {self.num_panels} panels is opening.")
            self.is_open = True
        else:
            print("The sliding door is already open.")

    def close(self):
        """Close the sliding door."""
        if self.is_open:
            print(f"The {self.material} sliding door with {self.num_panels} panels is closing.")
            self.is_open = False
        else:
            print("The sliding door is already closed.")

# Casement door class
class CasementDoor(Door):
    """Class for casement doors."""

    def __init__(self, material, size, hinge_side):
        """
        Initialize a casement door.

        Args:
            material (str): The material of the door.
            size (str): The size of the door.
            hinge_side (str): The side of the hinge.
        """
        super().__init__(DoorType.CASEMENT, material, size)
        self.hinge_side = hinge_side
        self.is_open = False

    def open(self):
        """Open the casement door."""
        if not self.is_open:
            print(f"The {self.material} casement door with {self.hinge_side} hinge is opening.")
            self.is_open = True
        else:
            print("The casement door is already open.")

    def close(self):
        """Close the casement door."""
        if self.is_open:
            print(f"The {self.material} casement door with {self.hinge_side} hinge is closing.")
            self.is_open = False
        else:
            print("The casement door is already closed.")

# Door factory class
class DoorFactory:
    """Class for creating doors."""

    @staticmethod
    def create_door(door_type, material, size, **kwargs):
        """
        Create a door.

        Args:
            door_type (DoorType): The type of door.
            material (str): The material of the door.
            size (str): The size of the door.
            **kwargs: Additional keyword arguments.

        Returns:
            Door: The created door.

        Raises:
            ValueError: If the door type is not supported.
        """
        if door_type == DoorType.SLIDING:
            if 'num_panels' not in kwargs:
                raise ValueError("Number of panels is required for sliding doors.")
            return SlidingDoor(material, size, kwargs['num_panels'])
        elif door_type == DoorType.CASEMENT:
            if 'hinge_side' not in kwargs:
                raise ValueError("Hinge side is required for casement doors.")
            return CasementDoor(material, size, kwargs['hinge_side'])
        else:
            raise ValueError("Unsupported door type.")

# Example usage
if __name__ == "__main__":
    try:
        sliding_door = DoorFactory.create_door(DoorType.SLIDING, "Aluminum", "80x200", num_panels=2)
        sliding_door.open()
        sliding_door.close()

        casement_door = DoorFactory.create_door(DoorType.CASEMENT, "Wood", "60x180", hinge_side="left")
        casement_door.open()
        casement_door.close()
    except ValueError as e:
        print(f"Error: {e}")
```
