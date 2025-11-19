"""
Generated Code Metadata:
========================
Original URL: https://sarl-verdier-irrigation.fr
Prompt: Generate code to track and schedule maintenance for agricultural machinery, including features for part replacement and servicing, inspired by SARL VERDIER's repair and maintenance offerings.
Generated: DETERMINISTIC_813ebd35b7808467
Batch ID: 20250612_153224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class MaintenanceRecord:
    """Class to represent a maintenance record for agricultural machinery."""
    
    def __init__(self, date: datetime.date, description: str, parts_replaced: List[str]):
        self.date = date
        self.description = description
        self.parts_replaced = parts_replaced

    def __str__(self):
        return f"Date: {self.date}, Description: {self.description}, Parts Replaced: {', '.join(self.parts_replaced)}"


class Machinery:
    """Class to represent agricultural machinery with maintenance tracking."""
    
    def __init__(self, name: str, model: str):
        self.name = name
        self.model = model
        self.maintenance_records: List[MaintenanceRecord] = []

    def schedule_maintenance(self, date: datetime.date, description: str, parts_replaced: Optional[List[str]] = None):
        """Schedule a maintenance record for the machinery."""
        if parts_replaced is None:
            parts_replaced = []
        record = MaintenanceRecord(date, description, parts_replaced)
        self.maintenance_records.append(record)

    def get_maintenance_history(self) -> List[MaintenanceRecord]:
        """Retrieve the maintenance history of the machinery."""
        return self.maintenance_records

    def __str__(self):
        return f"Machinery Name: {self.name}, Model: {self.model}, Maintenance Records: {len(self.maintenance_records)}"


class MaintenanceScheduler:
    """Class to manage multiple machinery and their maintenance schedules."""
    
    def __init__(self):
        self.machinery_list: List[Machinery] = []

    def add_machinery(self, machinery: Machinery):
        """Add a new machinery to the scheduler."""
        self.machinery_list.append(machinery)

    def schedule_maintenance_for_machinery(self, machinery_name: str, date: datetime.date, description: str, parts_replaced: Optional[List[str]] = None):
        """Schedule maintenance for a specific machinery by name."""
        machinery = self.find_machinery(machinery_name)
        if machinery:
            machinery.schedule_maintenance(date, description, parts_replaced)
        else:
            raise ValueError(f"Machinery with name '{machinery_name}' not found.")

    def find_machinery(self, name: str) -> Optional[Machinery]:
        """Find machinery by name."""
        for machinery in self.machinery_list:
            if machinery.name == name:
                return machinery
        return None

    def get_all_maintenance_records(self) -> List[MaintenanceRecord]:
        """Retrieve all maintenance records from all machinery."""
        all_records = []
        for machinery in self.machinery_list:
            all_records.extend(machinery.get_maintenance_history())
        return all_records


# Example usage
if __name__ == "__main__":
    try:
        # Create a maintenance scheduler
        scheduler = MaintenanceScheduler()

        # Add machinery
        tractor = Machinery("Tractor A", "Model X")
        scheduler.add_machinery(tractor)

        # Schedule maintenance
        scheduler.schedule_maintenance_for_machinery("Tractor A", datetime.date(2023, 10, 15), "Oil change", ["Oil filter", "Engine oil"])

        # Retrieve and print maintenance history
        for record in tractor.get_maintenance_history():
            print(record)

    except Exception as e:
        print(f"An error occurred: {e}")
```
