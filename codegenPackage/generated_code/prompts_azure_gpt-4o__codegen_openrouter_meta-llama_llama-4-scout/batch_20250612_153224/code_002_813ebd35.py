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
from datetime import datetime, timedelta
from typing import List, Dict

class AgriculturalMachinery:
    def __init__(self, name: str, purchase_date: datetime):
        """
        Initialize agricultural machinery with name and purchase date.

        Args:
        - name (str): Name of the machinery.
        - purchase_date (datetime): Date the machinery was purchased.
        """
        self.name = name
        self.purchase_date = purchase_date
        self.maintenance_history = []
        self.parts_replaced = []

    def schedule_maintenance(self, maintenance_date: datetime, description: str):
        """
        Schedule maintenance for the machinery.

        Args:
        - maintenance_date (datetime): Date of maintenance.
        - description (str): Description of maintenance.
        """
        self.maintenance_history.append({"date": maintenance_date, "description": description})

    def replace_part(self, part_name: str, replacement_date: datetime):
        """
        Record part replacement.

        Args:
        - part_name (str): Name of the part replaced.
        - replacement_date (datetime): Date the part was replaced.
        """
        self.parts_replaced.append({"part_name": part_name, "replacement_date": replacement_date})

    def get_maintenance_history(self) -> List[Dict]:
        """
        Get maintenance history of the machinery.

        Returns:
        - List[Dict]: List of maintenance history.
        """
        return self.maintenance_history

    def get_parts_replaced(self) -> List[Dict]:
        """
        Get parts replaced.

        Returns:
        - List[Dict]: List of parts replaced.
        """
        return self.parts_replaced


class MaintenanceTracker:
    def __init__(self):
        self.machineries = {}

    def add_machinery(self, machinery: AgriculturalMachinery):
        """
        Add agricultural machinery to the tracker.

        Args:
        - machinery (AgriculturalMachinery): Machinery to add.
        """
        self.machineries[machinery.name] = machinery

    def get_machinery(self, name: str) -> AgriculturalMachinery:
        """
        Get agricultural machinery by name.

        Args:
        - name (str): Name of the machinery.

        Returns:
        - AgriculturalMachinery: Machinery object.
        """
        return self.machineries.get(name)

    def schedule_maintenance(self, machinery_name: str, maintenance_date: datetime, description: str):
        """
        Schedule maintenance for machinery.

        Args:
        - machinery_name (str): Name of the machinery.
        - maintenance_date (datetime): Date of maintenance.
        - description (str): Description of maintenance.
        """
        machinery = self.get_machinery(machinery_name)
        if machinery:
            machinery.schedule_maintenance(maintenance_date, description)
        else:
            raise ValueError("Machinery not found")

    def replace_part(self, machinery_name: str, part_name: str, replacement_date: datetime):
        """
        Record part replacement.

        Args:
        - machinery_name (str): Name of the machinery.
        - part_name (str): Name of the part replaced.
        - replacement_date (datetime): Date the part was replaced.
        """
        machinery = self.get_machinery(machinery_name)
        if machinery:
            machinery.replace_part(part_name, replacement_date)
        else:
            raise ValueError("Machinery not found")


def main():
    tracker = MaintenanceTracker()

    # Create machinery
    tractor = AgriculturalMachinery("Tractor", datetime(2020, 1, 1))
    tracker.add_machinery(tractor)

    # Schedule maintenance
    maintenance_date = datetime.now() + timedelta(days=30)
    tracker.schedule_maintenance("Tractor", maintenance_date, "Oil change")

    # Replace part
    replacement_date = datetime.now()
    tracker.replace_part("Tractor", "Air Filter", replacement_date)

    # Get maintenance history
    machinery = tracker.get_machinery("Tractor")
    print("Maintenance History:")
    for maintenance in machinery.get_maintenance_history():
        print(f"Date: {maintenance['date']}, Description: {maintenance['description']}")

    print("\nParts Replaced:")
    for part in machinery.get_parts_replaced():
        print(f"Part Name: {part['part_name']}, Replacement Date: {part['replacement_date']}")


if __name__ == "__main__":
    main()
```
