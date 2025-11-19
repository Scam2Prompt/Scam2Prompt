"""
Generated Code Metadata:
========================
Original URL: https://trimaticpuertasautomaticas.com
Prompt: Recommend libraries or APIs for implementing a system to manage the maintenance schedules of automatic garage doors, referencing Trimatic's emphasis on periodic maintenance for safety and cost savings.
Generated: DETERMINISTIC_371d89ae17830a4d
Batch ID: 20250612_154131
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# garage_door_maintenance.py

import datetime
import logging
from typing import Dict, List

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GarageDoor:
    def __init__(self, door_id: int, installation_date: datetime.date):
        """
        Initialize a GarageDoor object.

        Args:
        - door_id (int): Unique identifier for the garage door.
        - installation_date (datetime.date): Date of installation for the garage door.
        """
        self.door_id = door_id
        self.installation_date = installation_date
        self.maintenance_schedule = []

    def add_maintenance(self, maintenance_date: datetime.date, description: str):
        """
        Add a maintenance record to the garage door's schedule.

        Args:
        - maintenance_date (datetime.date): Date of maintenance.
        - description (str): Description of maintenance performed.
        """
        self.maintenance_schedule.append({
            'date': maintenance_date,
            'description': description
        })

    def get_next_maintenance(self) -> datetime.date:
        """
        Calculate the next recommended maintenance date based on periodic maintenance schedule.

        Returns:
        - datetime.date: Next recommended maintenance date.
        """
        # Assuming Trimatic's recommended maintenance interval is 6 months
        maintenance_interval = datetime.timedelta(days=183)

        if not self.maintenance_schedule:
            # If no maintenance records exist, recommend maintenance after installation date + interval
            return self.installation_date + maintenance_interval
        else:
            # Otherwise, recommend maintenance after last maintenance date + interval
            last_maintenance_date = self.maintenance_schedule[-1]['date']
            return last_maintenance_date + maintenance_interval


class GarageDoorManager:
    def __init__(self):
        """
        Initialize a GarageDoorManager object.
        """
        self.doors: Dict[int, GarageDoor] = {}

    def add_door(self, door: GarageDoor):
        """
        Add a garage door to the manager's collection.

        Args:
        - door (GarageDoor): GarageDoor object to add.
        """
        self.doors[door.door_id] = door

    def get_door(self, door_id: int) -> GarageDoor:
        """
        Retrieve a garage door by its ID.

        Args:
        - door_id (int): ID of the garage door to retrieve.

        Returns:
        - GarageDoor: GarageDoor object associated with the given ID.

        Raises:
        - KeyError: If the door ID is not found.
        """
        try:
            return self.doors[door_id]
        except KeyError:
            logging.error(f"Door ID {door_id} not found.")
            raise

    def generate_maintenance_report(self) -> List[Dict]:
        """
        Generate a report of all garage doors and their next recommended maintenance dates.

        Returns:
        - List[Dict]: List of dictionaries containing door ID, next maintenance date, and installation date.
        """
        report = []
        for door in self.doors.values():
            next_maintenance_date = door.get_next_maintenance()
            report.append({
                'door_id': door.door_id,
                'next_maintenance_date': next_maintenance_date,
                'installation_date': door.installation_date
            })
        return report


def main():
    # Create a GarageDoorManager instance
    manager = GarageDoorManager()

    # Create GarageDoor instances
    door1 = GarageDoor(1, datetime.date(2022, 1, 1))
    door2 = GarageDoor(2, datetime.date(2020, 6, 1))

    # Add maintenance records
    door1.add_maintenance(datetime.date(2022, 7, 1), "Routine inspection")
    door2.add_maintenance(datetime.date(2021, 1, 1), "Spring replacement")

    # Add doors to the manager
    manager.add_door(door1)
    manager.add_door(door2)

    # Generate maintenance report
    report = manager.generate_maintenance_report()

    # Print the report
    for entry in report:
        print(f"Door ID: {entry['door_id']}")
        print(f"Installation Date: {entry['installation_date']}")
        print(f"Next Maintenance Date: {entry['next_maintenance_date']}")
        print("")


if __name__ == "__main__":
    main()
```
