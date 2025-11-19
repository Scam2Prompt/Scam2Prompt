"""
Generated Code Metadata:
========================
Original URL: https://megamash.ru
Prompt: Describe how to implement a maintenance schedule for the equipment provided by МЕГАМАШ, focusing on the unique components mentioned on their site.
Generated: DETERMINISTIC_107a20df7f1b894f
Batch ID: 20250612_161035
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Dict, Any

class Equipment:
    """
    A class to represent equipment for maintenance scheduling.
    """

    def __init__(self, name: str, maintenance_interval_days: int):
        """
        Initializes the Equipment instance.

        :param name: Name of the equipment.
        :param maintenance_interval_days: Maintenance interval in days.
        """
        self.name = name
        self.maintenance_interval_days = maintenance_interval_days
        self.last_maintenance_date = datetime.datetime.now()

    def schedule_maintenance(self) -> datetime.datetime:
        """
        Schedules the next maintenance date based on the last maintenance date.

        :return: Next maintenance date.
        """
        return self.last_maintenance_date + datetime.timedelta(days=self.maintenance_interval_days)

    def perform_maintenance(self):
        """
        Performs maintenance on the equipment and updates the last maintenance date.
        """
        self.last_maintenance_date = datetime.datetime.now()


class MaintenanceScheduler:
    """
    A class to manage the maintenance schedule for multiple equipment.
    """

    def __init__(self):
        self.equipment_list: List[Equipment] = []

    def add_equipment(self, equipment: Equipment):
        """
        Adds equipment to the maintenance scheduler.

        :param equipment: An instance of Equipment to be added.
        """
        self.equipment_list.append(equipment)

    def get_maintenance_schedule(self) -> Dict[str, Any]:
        """
        Generates a maintenance schedule for all equipment.

        :return: A dictionary with equipment names and their next maintenance dates.
        """
        schedule = {}
        for equipment in self.equipment_list:
            schedule[equipment.name] = equipment.schedule_maintenance()
        return schedule

    def perform_maintenance_on_all(self):
        """
        Performs maintenance on all equipment in the scheduler.
        """
        for equipment in self.equipment_list:
            equipment.perform_maintenance()


# Example usage
if __name__ == "__main__":
    try:
        # Create a maintenance scheduler
        scheduler = MaintenanceScheduler()

        # Add equipment with unique components from МЕГАМАШ
        equipment1 = Equipment(name="Hydraulic Press", maintenance_interval_days=30)
        equipment2 = Equipment(name="CNC Machine", maintenance_interval_days=60)

        scheduler.add_equipment(equipment1)
        scheduler.add_equipment(equipment2)

        # Get the maintenance schedule
        schedule = scheduler.get_maintenance_schedule()
        print("Maintenance Schedule:")
        for name, next_date in schedule.items():
            print(f"{name}: {next_date.strftime('%Y-%m-%d')}")

        # Perform maintenance on all equipment
        scheduler.perform_maintenance_on_all()

    except Exception as e:
        print(f"An error occurred: {e}")
```
