"""
Generated Code Metadata:
========================
Original URL: https://fmt.co.id
Prompt: Develop a use case diagram for a construction equipment management system that includes features like equipment tracking, maintenance scheduling, and attachment management for excavators.
Generated: DETERMINISTIC_f56be5eba9c234fe
Batch ID: 20250622_211609
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import necessary libraries
import datetime
from typing import List, Optional

class Equipment:
    """Class representing a piece of construction equipment."""
    
    def __init__(self, equipment_id: str, name: str):
        """
        Initialize the equipment with an ID and name.
        
        :param equipment_id: Unique identifier for the equipment
        :param name: Name of the equipment
        """
        self.equipment_id = equipment_id
        self.name = name
        self.attachments: List[str] = []  # List to hold attachments
        self.maintenance_schedule: List[datetime.date] = []  # List to hold maintenance dates

    def add_attachment(self, attachment: str) -> None:
        """
        Add an attachment to the equipment.
        
        :param attachment: Name of the attachment to add
        """
        self.attachments.append(attachment)

    def schedule_maintenance(self, date: datetime.date) -> None:
        """
        Schedule maintenance for the equipment.
        
        :param date: Date for the scheduled maintenance
        """
        if date < datetime.date.today():
            raise ValueError("Maintenance date cannot be in the past.")
        self.maintenance_schedule.append(date)

    def get_info(self) -> str:
        """
        Get information about the equipment, including attachments and maintenance schedule.
        
        :return: String representation of the equipment information
        """
        return (f"Equipment ID: {self.equipment_id}, Name: {self.name}, "
                f"Attachments: {self.attachments}, "
                f"Maintenance Schedule: {self.maintenance_schedule}")


class EquipmentManager:
    """Class to manage a collection of construction equipment."""
    
    def __init__(self):
        """Initialize the equipment manager with an empty equipment list."""
        self.equipment_list: List[Equipment] = []

    def add_equipment(self, equipment: Equipment) -> None:
        """
        Add a new piece of equipment to the manager.
        
        :param equipment: Equipment object to add
        """
        self.equipment_list.append(equipment)

    def find_equipment(self, equipment_id: str) -> Optional[Equipment]:
        """
        Find equipment by its ID.
        
        :param equipment_id: Unique identifier for the equipment
        :return: Equipment object if found, else None
        """
        for equipment in self.equipment_list:
            if equipment.equipment_id == equipment_id:
                return equipment
        return None

    def get_all_equipment_info(self) -> List[str]:
        """
        Get information for all equipment managed.
        
        :return: List of strings containing information about each equipment
        """
        return [equipment.get_info() for equipment in self.equipment_list]


# Example usage
if __name__ == "__main__":
    # Create an equipment manager
    manager = EquipmentManager()

    # Create some equipment
    excavator = Equipment("EXC-001", "Excavator Model A")
    excavator.add_attachment("Bucket")
    excavator.schedule_maintenance(datetime.date(2023, 12, 1))

    # Add equipment to the manager
    manager.add_equipment(excavator)

    # Retrieve and print all equipment information
    for info in manager.get_all_equipment_info():
        print(info)
```
