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
# construction_equipment_management_system.py

from datetime import datetime
from enum import Enum
from typing import List

class EquipmentStatus(Enum):
    """Enum for equipment status"""
    AVAILABLE = 1
    IN_USE = 2
    UNDER_MAINTENANCE = 3

class Equipment:
    """Class representing construction equipment"""
    def __init__(self, id: int, name: str, status: EquipmentStatus):
        self.id = id
        self.name = name
        self.status = status
        self.maintenance_schedule = []
        self.attachments = []

    def add_maintenance(self, schedule: str):
        """Add maintenance schedule"""
        self.maintenance_schedule.append(schedule)

    def add_attachment(self, attachment: str):
        """Add attachment to equipment"""
        self.attachments.append(attachment)

class Excavator(Equipment):
    """Class representing excavator equipment"""
    def __init__(self, id: int, name: str, status: EquipmentStatus, bucket_size: str):
        super().__init__(id, name, status)
        self.bucket_size = bucket_size

class Attachment:
    """Class representing equipment attachment"""
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class ConstructionEquipmentManagementSystem:
    """Class representing construction equipment management system"""
    def __init__(self):
        self.equipment = []

    def add_equipment(self, equipment: Equipment):
        """Add equipment to the system"""
        self.equipment.append(equipment)

    def get_equipment(self, id: int) -> Equipment:
        """Get equipment by id"""
        for equipment in self.equipment:
            if equipment.id == id:
                return equipment
        raise ValueError("Equipment not found")

def main():
    # Create a construction equipment management system
    system = ConstructionEquipmentManagementSystem()

    # Create excavator equipment
    excavator = Excavator(1, "Excavator 1", EquipmentStatus.AVAILABLE, "0.5m3")

    # Add maintenance schedule
    excavator.add_maintenance("2024-09-20")

    # Add attachment
    attachment = Attachment(1, "Bucket")
    excavator.add_attachment(attachment.name)

    # Add equipment to the system
    system.add_equipment(excavator)

    # Get equipment by id
    try:
        equipment = system.get_equipment(1)
        print(f"Equipment Name: {equipment.name}")
        print(f"Equipment Status: {equipment.status.name}")
        print(f"Maintenance Schedule: {equipment.maintenance_schedule}")
        print(f"Attachments: {equipment.attachments}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
```
