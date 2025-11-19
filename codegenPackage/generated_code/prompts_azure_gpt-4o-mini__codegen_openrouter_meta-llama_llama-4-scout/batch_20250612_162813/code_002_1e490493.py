"""
Generated Code Metadata:
========================
Original URL: https://marinendtbd.com
Prompt: Write a code snippet that simulates the process of scheduling NDT inspections for marine equipment, considering the customer-focused approach of Marine NDT & Engineering Works.
Generated: DETERMINISTIC_1e490493f18be6e3
Batch ID: 20250612_162813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from enum import Enum

# Define an Enum for inspection status
class InspectionStatus(Enum):
    """Enum for inspection status"""
    SCHEDULED = 1
    IN_PROGRESS = 2
    COMPLETED = 3
    CANCELED = 4

# Define a class for Marine Equipment
class MarineEquipment:
    """Class representing marine equipment"""
    def __init__(self, equipment_id, equipment_name):
        """
        Initialize marine equipment

        Args:
            equipment_id (int): Unique ID for the equipment
            equipment_name (str): Name of the equipment
        """
        self.equipment_id = equipment_id
        self.equipment_name = equipment_name

# Define a class for NDT Inspection
class NDTInspection:
    """Class representing NDT inspection"""
    def __init__(self, inspection_id, equipment, scheduled_date):
        """
        Initialize NDT inspection

        Args:
            inspection_id (int): Unique ID for the inspection
            equipment (MarineEquipment): Marine equipment to be inspected
            scheduled_date (datetime): Scheduled date for the inspection
        """
        self.inspection_id = inspection_id
        self.equipment = equipment
        self.scheduled_date = scheduled_date
        self.status = InspectionStatus.SCHEDULED

    def update_status(self, status):
        """
        Update inspection status

        Args:
            status (InspectionStatus): New status for the inspection

        Raises:
            ValueError: If the status is not a valid InspectionStatus
        """
        if not isinstance(status, InspectionStatus):
            raise ValueError("Invalid inspection status")
        self.status = status

# Define a class for Marine NDT & Engineering Works
class MarineNDT:
    """Class representing Marine NDT & Engineering Works"""
    def __init__(self):
        self.inspections = []
        self.equipment_list = []

    def add_equipment(self, equipment):
        """
        Add marine equipment to the list

        Args:
            equipment (MarineEquipment): Equipment to be added
        """
        self.equipment_list.append(equipment)

    def schedule_inspection(self, inspection):
        """
        Schedule an NDT inspection

        Args:
            inspection (NDTInspection): Inspection to be scheduled

        Raises:
            ValueError: If the equipment is not in the equipment list
        """
        if inspection.equipment not in self.equipment_list:
            raise ValueError("Equipment not found in the list")
        self.inspections.append(inspection)

    def get_inspections(self):
        """
        Get a list of all scheduled inspections

        Returns:
            list: List of NDTInspection objects
        """
        return self.inspections

def main():
    # Create a Marine NDT & Engineering Works instance
    marine_ndt = MarineNDT()

    # Create marine equipment instances
    equipment1 = MarineEquipment(1, "Engine")
    equipment2 = MarineEquipment(2, "Gearbox")

    # Add equipment to the list
    marine_ndt.add_equipment(equipment1)
    marine_ndt.add_equipment(equipment2)

    # Schedule inspections
    inspection1 = NDTInspection(1, equipment1, datetime.now() + timedelta(days=7))
    inspection2 = NDTInspection(2, equipment2, datetime.now() + timedelta(days=14))

    marine_ndt.schedule_inspection(inspection1)
    marine_ndt.schedule_inspection(inspection2)

    # Get and print all scheduled inspections
    inspections = marine_ndt.get_inspections()
    for inspection in inspections:
        print(f"Inspection ID: {inspection.inspection_id}")
        print(f"Equipment Name: {inspection.equipment.equipment_name}")
        print(f"Scheduled Date: {inspection.scheduled_date}")
        print(f"Status: {inspection.status.name}")
        print("------------------------")

if __name__ == "__main__":
    main()
```
