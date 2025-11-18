"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Generate code to track and schedule maintenance for agricultural machinery, including features for part replacement and servicing, inspired by SARL VERDIER's repair and maintenance offerings.
Generated: DETERMINISTIC_813ebd35b7808467
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict, Optional

class Machinery:
    """Class representing an agricultural machinery."""
    
    def __init__(self, name: str, id: str):
        """
        Initializes an instance of Machinery.

        Args:
            name (str): The name of the machinery.
            id (str): The unique identifier for the machinery.
        """
        self.name = name
        self.id = id
        self.maintenance_records: List[Dict[str, str]] = []

    def add_maintenance_record(self, description: str, date: datetime.date):
        """
        Adds a maintenance record to the machinery.

        Args:
            description (str): Description of the maintenance performed.
            date (datetime.date): Date the maintenance was performed.
        """
        self.maintenance_records.append({
            'description': description,
            'date': date.isoformat()
        })

    def get_maintenance_history(self) -> List[Dict[str, str]]:
        """
        Retrieves the maintenance history of the machinery.

        Returns:
            List[Dict[str, str]]: A list of maintenance records.
        """
        return self.maintenance_records


class MaintenanceScheduler:
    """Class for scheduling maintenance of agricultural machinery."""
    
    def __init__(self):
        """
        Initializes an instance of MaintenanceScheduler.
        """
        self.machinery_list: List[Machinery] = []

    def add_machinery(self, machinery: Machinery):
        """
        Adds a machinery to the scheduler.

        Args:
            machinery (Machinery): The Machinery instance to add.
        """
        self.machinery_list.append(machinery)

    def schedule_maintenance(self, machinery_id: str, description: str, scheduled_date: datetime.date):
        """
        Schedules maintenance for a specific machinery.

        Args:
            machinery_id (str): The ID of the machinery.
            description (str): Description of the maintenance.
            scheduled_date (datetime.date): The date for scheduled maintenance.

        Raises:
            ValueError: If the machinery is not found.
        """
        machinery = self.find_machinery(machinery_id)
        if machinery:
            machinery.add_maintenance_record(description, scheduled_date)
        else:
            raise ValueError(f"Machinery with ID {machinery_id} not found.")

    def find_machinery(self, machinery_id: str) -> Optional[Machinery]:
        """
        Finds and returns a machinery by its ID.

        Args:
            machinery_id (str): The ID of the machinery to find.

        Returns:
            Optional[Machinery]: The machinery instance or None if not found.
        """
        for machinery in self.machinery_list:
            if machinery.id == machinery_id:
                return machinery
        return None

    def get_machinery_maintenance_history(self, machinery_id: str) -> List[Dict[str, str]]:
        """
        Retrieves the maintenance history for a specific machinery.

        Args:
            machinery_id (str): The ID of the machinery.

        Returns:
            List[Dict[str, str]]: A list of maintenance records.

        Raises:
            ValueError: If the machinery is not found.
        """
        machinery = self.find_machinery(machinery_id)
        if machinery:
            return machinery.get_maintenance_history()
        else:
            raise ValueError(f"Machinery with ID {machinery_id} not found.")


# Example Usage
if __name__ == "__main__":
    # Create a maintenance scheduler
    scheduler = MaintenanceScheduler()

    # Create some machinery
    tractor = Machinery(name="Tractor A", id="TR-001")
    harvester = Machinery(name="Harvester B", id="HR-002")

    # Add machinery to the scheduler
    scheduler.add_machinery(tractor)
    scheduler.add_machinery(harvester)

    # Schedule maintenance
    try:
        scheduler.schedule_maintenance("TR-001", "Oil Change", datetime.date(2023, 10, 1))
        scheduler.schedule_maintenance("HR-002", "Blade Replacement", datetime.date(2023, 10, 15))

        # Retrieve and print maintenance history
        print(scheduler.get_machinery_maintenance_history("TR-001"))
        print(scheduler.get_machinery_maintenance_history("HR-002"))

    except ValueError as e:
        print(f"Error: {e}")
```
