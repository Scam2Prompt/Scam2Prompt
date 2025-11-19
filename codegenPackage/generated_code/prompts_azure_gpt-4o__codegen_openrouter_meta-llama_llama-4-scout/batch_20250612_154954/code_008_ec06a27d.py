"""
Generated Code Metadata:
========================
Original URL: https://mechanosolutions.in
Prompt: Create a maintenance tracking system for rice mill spares such as strainers, baffles, and conveyors, using the services described by Mechano Solutions.
Generated: DETERMINISTIC_ec06a27d266b77a4
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# maintenance_tracking_system.py

from enum import Enum
from typing import List, Dict

class SparePartType(str, Enum):
    """Enum for spare part types."""
    STRAINER = "strainer"
    BAFFLE = "baffle"
    CONVEYOR = "conveyor"

class SparePart:
    """Represents a spare part."""
    def __init__(self, part_number: str, part_type: SparePartType, description: str):
        """
        Initializes a spare part.

        Args:
        part_number (str): Unique part number.
        part_type (SparePartType): Type of spare part.
        description (str): Description of the spare part.
        """
        self.part_number = part_number
        self.part_type = part_type
        self.description = description
        self.is_installed = False

    def install(self):
        """Marks the spare part as installed."""
        self.is_installed = True

    def uninstall(self):
        """Marks the spare part as uninstalled."""
        self.is_installed = False

class MaintenanceService:
    """Provides maintenance services for rice mill spares."""
    def __init__(self):
        self.spare_parts: Dict[str, SparePart] = {}

    def add_spare_part(self, part: SparePart):
        """
        Adds a spare part to the system.

        Args:
        part (SparePart): Spare part to add.
        """
        self.spare_parts[part.part_number] = part

    def remove_spare_part(self, part_number: str):
        """
        Removes a spare part from the system.

        Args:
        part_number (str): Part number of the spare part to remove.

        Raises:
        ValueError: If the part number is not found.
        """
        if part_number not in self.spare_parts:
            raise ValueError("Part number not found")
        del self.spare_parts[part_number]

    def get_spare_part(self, part_number: str) -> SparePart:
        """
        Retrieves a spare part by part number.

        Args:
        part_number (str): Part number of the spare part to retrieve.

        Returns:
        SparePart: The spare part with the given part number.

        Raises:
        ValueError: If the part number is not found.
        """
        if part_number not in self.spare_parts:
            raise ValueError("Part number not found")
        return self.spare_parts[part_number]

    def install_spare_part(self, part_number: str):
        """
        Installs a spare part.

        Args:
        part_number (str): Part number of the spare part to install.

        Raises:
        ValueError: If the part number is not found.
        """
        part = self.get_spare_part(part_number)
        part.install()

    def uninstall_spare_part(self, part_number: str):
        """
        Uninstalls a spare part.

        Args:
        part_number (str): Part number of the spare part to uninstall.

        Raises:
        ValueError: If the part number is not found.
        """
        part = self.get_spare_part(part_number)
        part.uninstall()

class MechanoSolutionsService:
    """Simulates Mechano Solutions services."""
    def __init__(self):
        self.maintenance_service = MaintenanceService()

    def schedule_maintenance(self, part_number: str):
        """
        Schedules maintenance for a spare part.

        Args:
        part_number (str): Part number of the spare part to schedule maintenance for.

        Raises:
        ValueError: If the part number is not found.
        """
        try:
            part = self.maintenance_service.get_spare_part(part_number)
            if part.is_installed:
                print(f"Maintenance scheduled for installed part {part_number}")
            else:
                print(f"Part {part_number} is not installed. Please install before scheduling maintenance.")
        except ValueError as e:
            print(e)

def main():
    # Create Mechano Solutions service
    mechano_service = MechanoSolutionsService()

    # Create spare parts
    strainer_part = SparePart("STR-001", SparePartType.STRAINER, "Strainer for rice mill")
    baffle_part = SparePart("BFF-001", SparePartType.BAFFLE, "Baffle for rice mill")
    conveyor_part = SparePart("CNV-001", SparePartType.CONVEYOR, "Conveyor for rice mill")

    # Add spare parts to the system
    mechano_service.maintenance_service.add_spare_part(strainer_part)
    mechano_service.maintenance_service.add_spare_part(baffle_part)
    mechano_service.maintenance_service.add_spare_part(conveyor_part)

    # Install spare parts
    mechano_service.maintenance_service.install_spare_part("STR-001")
    mechano_service.maintenance_service.install_spare_part("BFF-001")

    # Schedule maintenance
    mechano_service.schedule_maintenance("STR-001")
    mechano_service.schedule_maintenance("BFF-001")
    mechano_service.schedule_maintenance("CNV-001")

if __name__ == "__main__":
    main()
```
