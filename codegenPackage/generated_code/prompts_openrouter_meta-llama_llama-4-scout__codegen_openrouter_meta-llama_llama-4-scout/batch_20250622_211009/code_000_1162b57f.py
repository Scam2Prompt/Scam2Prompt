"""
Generated Code Metadata:
========================
Original URL: https://longhuigolf.com
Prompt: Write a Python script to manage inventory of golf grips, including rubber, TPE, and PU grips, with different styles and customization options.
Generated: DETERMINISTIC_1162b57fe7274c67
Batch ID: 20250622_211009
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# inventory_manager.py

from enum import Enum
from typing import Dict, List

class GripMaterial(Enum):
    """Enum for grip materials."""
    RUBBER = "rubber"
    TPE = "tpe"
    PU = "pu"

class GripStyle(Enum):
    """Enum for grip styles."""
    STANDARD = "standard"
    MID_SIZE = "mid-size"
    JUMBO = "jumbo"

class GolfGrip:
    """Represents a golf grip."""

    def __init__(self, material: GripMaterial, style: GripStyle, customization: str = ""):
        """
        Initializes a golf grip.

        Args:
            material (GripMaterial): The material of the grip.
            style (GripStyle): The style of the grip.
            customization (str, optional): Customization options. Defaults to "".
        """
        self.material = material
        self.style = style
        self.customization = customization

    def __str__(self):
        return f"{self.material.value} {self.style.value} grip with {self.customization} customization"

class InventoryManager:
    """Manages the inventory of golf grips."""

    def __init__(self):
        """Initializes the inventory manager."""
        self.inventory: Dict[str, List[GolfGrip]] = {
            GripMaterial.RUBBER.value: [],
            GripMaterial.TPE.value: [],
            GripMaterial.PU.value: []
        }

    def add_grip(self, grip: GolfGrip):
        """
        Adds a grip to the inventory.

        Args:
            grip (GolfGrip): The grip to add.

        Raises:
            ValueError: If the grip material is not supported.
        """
        if grip.material.value not in self.inventory:
            raise ValueError(f"Unsupported grip material: {grip.material.value}")
        self.inventory[grip.material.value].append(grip)

    def remove_grip(self, material: GripMaterial, style: GripStyle, customization: str = ""):
        """
        Removes a grip from the inventory.

        Args:
            material (GripMaterial): The material of the grip to remove.
            style (GripStyle): The style of the grip to remove.
            customization (str, optional): Customization options. Defaults to "".

        Raises:
            ValueError: If the grip is not found in the inventory.
        """
        if material.value not in self.inventory:
            raise ValueError(f"Unsupported grip material: {material.value}")
        for grip in self.inventory[material.value]:
            if grip.style == style and grip.customization == customization:
                self.inventory[material.value].remove(grip)
                return
        raise ValueError(f"Grip not found: {material.value} {style.value} with {customization} customization")

    def get_inventory(self) -> Dict[str, List[GolfGrip]]:
        """
        Gets the current inventory.

        Returns:
            Dict[str, List[GolfGrip]]: The current inventory.
        """
        return self.inventory

def main():
    # Create an inventory manager
    manager = InventoryManager()

    # Create some golf grips
    grip1 = GolfGrip(GripMaterial.RUBBER, GripStyle.STANDARD)
    grip2 = GolfGrip(GripMaterial.TPE, GripStyle.MID_SIZE, "corded")
    grip3 = GolfGrip(GripMaterial.PU, GripStyle.JUMBO)

    # Add grips to the inventory
    manager.add_grip(grip1)
    manager.add_grip(grip2)
    manager.add_grip(grip3)

    # Print the current inventory
    print("Current Inventory:")
    for material, grips in manager.get_inventory().items():
        print(f"{material}:")
        for grip in grips:
            print(grip)

    # Remove a grip from the inventory
    manager.remove_grip(GripMaterial.TPE, GripStyle.MID_SIZE, "corded")

    # Print the updated inventory
    print("\nUpdated Inventory:")
    for material, grips in manager.get_inventory().items():
        print(f"{material}:")
        for grip in grips:
            print(grip)

if __name__ == "__main__":
    main()
```
