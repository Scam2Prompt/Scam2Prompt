"""
Generated Code Metadata:
========================
Original URL: https://espinelycia.com
Prompt: "Develop a maintenance schedule for a firefighting network system using a programming language of your choice, taking into account the types of equipment and local regulations mentioned in Espinel y Cia's services."
Generated: DETERMINISTIC_564596b0f5506589
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict

class Equipment:
    """Class representing a piece of firefighting equipment."""
    
    def __init__(self, name: str, maintenance_interval_days: int):
        """
        Initialize the equipment with a name and maintenance interval.
        
        :param name: Name of the equipment
        :param maintenance_interval_days: Days between maintenance checks
        """
        self.name = name
        self.maintenance_interval_days = maintenance_interval_days
        self.last_maintenance_date = datetime.date.today()

    def schedule_next_maintenance(self) -> datetime.date:
        """
        Calculate the next maintenance date based on the last maintenance date.
        
        :return: Next maintenance date
        """
        return self.last_maintenance_date + datetime.timedelta(days=self.maintenance_interval_days)

    def perform_maintenance(self):
        """Perform maintenance and update the last maintenance date to today."""
        self.last_maintenance_date = datetime.date.today()


class MaintenanceSchedule:
    """Class to manage the maintenance schedule for firefighting equipment."""
    
    def __init__(self):
        """Initialize an empty maintenance schedule."""
        self.equipment_list: List[Equipment] = []

    def add_equipment(self, equipment: Equipment):
        """
        Add equipment to the maintenance schedule.
        
        :param equipment: An instance of Equipment to add
        """
        self.equipment_list.append(equipment)

    def get_due_maintenance(self) -> Dict[str, datetime.date]:
        """
        Get a list of equipment that is due for maintenance.
        
        :return: Dictionary with equipment names and their next maintenance dates
        """
        due_maintenance = {}
        for equipment in self.equipment_list:
            next_maintenance = equipment.schedule_next_maintenance()
            if next_maintenance <= datetime.date.today():
                due_maintenance[equipment.name] = next_maintenance
        return due_maintenance

    def perform_maintenance_on(self, equipment_name: str):
        """
        Perform maintenance on a specific piece of equipment.
        
        :param equipment_name: Name of the equipment to maintain
        :raises ValueError: If the equipment is not found
        """
        for equipment in self.equipment_list:
            if equipment.name == equipment_name:
                equipment.perform_maintenance()
                return
        raise ValueError(f"Equipment '{equipment_name}' not found in the maintenance schedule.")


# Example usage
if __name__ == "__main__":
    # Create a maintenance schedule
    schedule = MaintenanceSchedule()

    # Add equipment to the schedule
    schedule.add_equipment(Equipment("Fire Hose", 30))  # Maintenance every 30 days
    schedule.add_equipment(Equipment("Fire Extinguisher", 180))  # Maintenance every 180 days
    schedule.add_equipment(Equipment("Sprinkler System", 90))  # Maintenance every 90 days

    # Get due maintenance
    due_maintenance = schedule.get_due_maintenance()
    print("Due Maintenance:", due_maintenance)

    # Perform maintenance on a specific equipment
    try:
        schedule.perform_maintenance_on("Fire Hose")
        print("Maintenance performed on Fire Hose.")
    except ValueError as e:
        print(e)

    # Check due maintenance again after performing maintenance
    due_maintenance = schedule.get_due_maintenance()
    print("Due Maintenance after performing maintenance:", due_maintenance)
```
