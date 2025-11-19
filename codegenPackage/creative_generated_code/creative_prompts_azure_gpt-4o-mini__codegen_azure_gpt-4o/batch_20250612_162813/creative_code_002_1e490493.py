"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://marinendtbd.com
Prompt: Write a code snippet that simulates the process of scheduling NDT inspections for marine equipment, considering the customer-focused approach of Marine NDT & Engineering Works.
Generated: DETERMINISTIC_1e490493f18be6e3
Batch ID: 20250612_162813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import random


class MarineEquipment:
    """
    Represents a marine equipment that requires NDT inspection.
    """
    def __init__(self, equipment_id, equipment_name):
        self.equipment_id = equipment_id
        self.equipment_name = equipment_name


class NDTInspection:
    """
    Represents an NDT inspection task.
    """
    def __init__(self, inspection_id, equipment, inspection_date, inspector_name):
        self.inspection_id = inspection_id
        self.equipment = equipment
        self.inspection_date = inspection_date
        self.inspector_name = inspector_name


class SchedulingSystem:
    """
    A system for scheduling NDT inspections for marine equipment.
    """
    def __init__(self):
        self.equipment_list = []
        self.inspections = []
        self.inspectors = ["Inspector A", "Inspector B", "Inspector C"]

    def add_equipment(self, equipment_id, equipment_name):
        """
        Adds a marine equipment to the system.
        """
        equipment = MarineEquipment(equipment_id, equipment_name)
        self.equipment_list.append(equipment)

    def schedule_inspection(self, equipment_id, inspection_date):
        """
        Schedules an NDT inspection for a given piece of equipment.
        """
        # Find the equipment by ID
        equipment = next((eq for eq in self.equipment_list if eq.equipment_id == equipment_id), None)
        if not equipment:
            raise ValueError(f"Equipment ID {equipment_id} not found.")

        # Choose a random inspector
        inspector_name = random.choice(self.inspectors)

        # Create and store the inspection
        inspection_id = f"INS-{len(self.inspections) + 1}"
        inspection = NDTInspection(inspection_id, equipment, inspection_date, inspector_name)
        self.inspections.append(inspection)

    def list_inspections(self):
        """
        Lists all scheduled inspections.
        """
        if not self.inspections:
            print("No inspections have been scheduled.")
            return

        print("Scheduled Inspections:")
        for inspection in self.inspections:
            print(f"Inspection ID: {inspection.inspection_id}")
            print(f"Equipment: {inspection.equipment.equipment_name} (ID: {inspection.equipment.equipment_id})")
            print(f"Inspection Date: {inspection.inspection_date}")
            print(f"Inspector: {inspection.inspector_name}")
            print("-" * 40)


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the scheduling system
        system = SchedulingSystem()

        # Add marine equipment
        system.add_equipment(equipment_id="EQ001", equipment_name="Marine Winch")
        system.add_equipment(equipment_id="EQ002", equipment_name="Anchor System")
        system.add_equipment(equipment_id="EQ003", equipment_name="Propulsion Engine")

        # Schedule inspections
        system.schedule_inspection(equipment_id="EQ001", inspection_date=datetime.date(2023, 11, 15))
        system.schedule_inspection(equipment_id="EQ002", inspection_date=datetime.date(2023, 11, 16))
        system.schedule_inspection(equipment_id="EQ003", inspection_date=datetime.date(2023, 11, 17))

        # List all inspections
        system.list_inspections()
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
