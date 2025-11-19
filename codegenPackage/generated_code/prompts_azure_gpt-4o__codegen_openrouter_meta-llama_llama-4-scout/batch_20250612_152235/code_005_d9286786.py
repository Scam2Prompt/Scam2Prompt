"""
Generated Code Metadata:
========================
Original URL: https://raid.services
Prompt: Create a function to register new equipment types on RAID Services, including fields for manufacturer, model, and version.
Generated: DETERMINISTIC_d928678649689bd6
Batch ID: 20250612_152235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# equipment_service.py

from typing import Dict
from enum import Enum
from dataclasses import dataclass

class EquipmentType(str, Enum):
    """Enumeration of supported equipment types."""
    STORAGE = "storage"
    SERVER = "server"
    NETWORK = "network"

@dataclass
class Equipment:
    """Dataclass representing equipment."""
    manufacturer: str
    model: str
    version: str

class EquipmentService:
    """Service class for managing equipment types."""

    def __init__(self):
        # Initialize an empty dictionary to store equipment types
        self.equipment_types: Dict[str, Equipment] = {}

    def register_equipment_type(self, equipment_type: str, equipment: Equipment) -> None:
        """
        Register a new equipment type.

        Args:
        - equipment_type (str): The type of equipment.
        - equipment (Equipment): The equipment details.

        Raises:
        - ValueError: If the equipment type is not supported.
        """
        if equipment_type not in [e.value for e in EquipmentType]:
            raise ValueError("Unsupported equipment type")

        # Check if equipment type already exists
        if equipment_type in self.equipment_types:
            raise ValueError("Equipment type already exists")

        # Register the equipment type
        self.equipment_types[equipment_type] = equipment

    def get_equipment_type(self, equipment_type: str) -> Equipment:
        """
        Get an equipment type.

        Args:
        - equipment_type (str): The type of equipment.

        Returns:
        - Equipment: The equipment details.

        Raises:
        - ValueError: If the equipment type does not exist.
        """
        try:
            return self.equipment_types[equipment_type]
        except KeyError:
            raise ValueError("Equipment type does not exist")

def main():
    # Create an instance of EquipmentService
    equipment_service = EquipmentService()

    # Create equipment details
    equipment = Equipment(
        manufacturer="Dell",
        model="PowerEdge R720",
        version="1.0"
    )

    # Register a new equipment type
    equipment_service.register_equipment_type(EquipmentType.STORAGE.value, equipment)

    # Get the registered equipment type
    try:
        registered_equipment = equipment_service.get_equipment_type(EquipmentType.STORAGE.value)
        print(f"Registered Equipment: {registered_equipment}")
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
