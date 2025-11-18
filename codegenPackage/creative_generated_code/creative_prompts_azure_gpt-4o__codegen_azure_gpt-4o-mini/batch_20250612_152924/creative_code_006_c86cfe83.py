"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://eraengineering.co.in
Prompt: Write code to automate the maintenance scheduling of sewerage systems, incorporating ERA ENGINEERING's recommended techniques for reliability and efficiency.
Generated: DETERMINISTIC_c86cfe83e58ec007
Batch ID: 20250612_152924
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
from typing import List, Dict, Any

class SewerageSystem:
    """
    Class representing a sewerage system for maintenance scheduling.
    """

    def __init__(self, system_id: str, last_maintenance: datetime.date, maintenance_interval: int):
        """
        Initialize a sewerage system.

        :param system_id: Unique identifier for the sewerage system
        :param last_maintenance: Date of the last maintenance performed
        :param maintenance_interval: Interval in days for scheduled maintenance
        """
        self.system_id = system_id
        self.last_maintenance = last_maintenance
        self.maintenance_interval = maintenance_interval

    def schedule_next_maintenance(self) -> datetime.date:
        """
        Schedule the next maintenance date based on the last maintenance date.

        :return: Date of the next scheduled maintenance
        """
        return self.last_maintenance + datetime.timedelta(days=self.maintenance_interval)

class MaintenanceScheduler:
    """
    Class to manage the maintenance scheduling for multiple sewerage systems.
    """

    def __init__(self):
        self.systems: List[SewerageSystem] = []

    def add_system(self, system: SewerageSystem) -> None:
        """
        Add a new sewerage system to the scheduler.

        :param system: SewerageSystem object to be added
        """
        self.systems.append(system)

    def get_due_maintenances(self) -> List[Dict[str, Any]]:
        """
        Get a list of systems that require maintenance.

        :return: List of dictionaries containing system ids and their next maintenance dates
        """
        due_maintenances = []
        today = datetime.date.today()
        
        for system in self.systems:
            next_maintenance = system.schedule_next_maintenance()
            if next_maintenance <= today:
                due_maintenances.append({
                    'system_id': system.system_id,
                    'next_maintenance': next_maintenance
                })
        return due_maintenances

def main():
    """
    Main function to demonstrate the maintenance scheduler functionality.
    """
    try:
        scheduler = MaintenanceScheduler()

        # Adding some sewerage systems with random last maintenance dates
        for i in range(5):
            last_maintenance_date = datetime.date.today() - datetime.timedelta(days=random.randint(30, 365))
            maintenance_interval = random.choice([30, 60, 90])  # in days
            sewer_system = SewerageSystem(system_id=f"SS-{i+1}", last_maintenance=last_maintenance_date, maintenance_interval=maintenance_interval)
            scheduler.add_system(sewer_system)

        # Retrieve due maintenances
        due_maintenances = scheduler.get_due_maintenances()
        
        if due_maintenances:
            print("Due Maintenance Schedule:")
            for maintenance in due_maintenances:
                print(f"System ID: {maintenance['system_id']}, Next Maintenance: {maintenance['next_maintenance']}")
        else:
            print("No systems are due for maintenance.")

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    main()
```
