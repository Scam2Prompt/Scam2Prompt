"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://mechanosolutions.in
Prompt: Create a maintenance tracking system for rice mill spares such as strainers, baffles, and conveyors, using the services described by Mechano Solutions.
Generated: DETERMINISTIC_ec06a27d266b77a4
Batch ID: 20250612_154954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
import json
import os

class SparePart:
    """
    Class representing a spare part in the maintenance tracking system.
    """
    def __init__(self, name, part_number, last_maintenance_date, next_maintenance_due):
        self.name = name
        self.part_number = part_number
        self.last_maintenance_date = last_maintenance_date
        self.next_maintenance_due = next_maintenance_due

    def to_dict(self):
        """Convert the SparePart instance to a dictionary."""
        return {
            'name': self.name,
            'part_number': self.part_number,
            'last_maintenance_date': self.last_maintenance_date.isoformat(),
            'next_maintenance_due': self.next_maintenance_due.isoformat(),
        }

    @classmethod
    def from_dict(cls, data):
        """Create a SparePart instance from a dictionary."""
        return cls(
            name=data['name'],
            part_number=data['part_number'],
            last_maintenance_date=datetime.datetime.fromisoformat(data['last_maintenance_date']),
            next_maintenance_due=datetime.datetime.fromisoformat(data['next_maintenance_due']),
        )

class MaintenanceTracker:
    """
    Class to manage the maintenance tracking of spare parts.
    """
    def __init__(self, filename='maintenance_data.json'):
        self.filename = filename
        self.spare_parts = []
        self.load_data()

    def load_data(self):
        """Load spare parts data from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    data = json.load(file)
                    self.spare_parts = [SparePart.from_dict(item) for item in data]
                except json.JSONDecodeError as e:
                    print(f"Error loading data: {e}")
        else:
            print("No data file found, starting fresh.")

    def save_data(self):
        """Save spare parts data to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([part.to_dict() for part in self.spare_parts], file)

    def add_spare_part(self, name, part_number, last_maintenance_date, next_maintenance_due):
        """Add a new spare part to the tracking system."""
        spare_part = SparePart(
            name=name,
            part_number=part_number,
            last_maintenance_date=last_maintenance_date,
            next_maintenance_due=next_maintenance_due
        )
        self.spare_parts.append(spare_part)
        self.save_data()

    def list_spare_parts(self):
        """List all spare parts currently tracked."""
        for part in self.spare_parts:
            print(f"Name: {part.name}, Part Number: {part.part_number}, "
                  f"Last Maintenance: {part.last_maintenance_date}, "
                  f"Next Due: {part.next_maintenance_due}")

    def find_spare_part(self, part_number):
        """Find and return a spare part by its part number."""
        for part in self.spare_parts:
            if part.part_number == part_number:
                return part
        return None

if __name__ == "__main__":
    # Example usage of the MaintenanceTracker class
    tracker = MaintenanceTracker()

    # Adding spare parts
    tracker.add_spare_part(
        name="Strainer",
        part_number="STR-001",
        last_maintenance_date=datetime.datetime(2023, 5, 10),
        next_maintenance_due=datetime.datetime(2024, 5, 10)
    )
    
    tracker.add_spare_part(
        name="Baffle",
        part_number="BAF-002",
        last_maintenance_date=datetime.datetime(2023, 6, 15),
        next_maintenance_due=datetime.datetime(2024, 6, 15)
    )

    # Listing all spare parts
    tracker.list_spare_parts()

    # Searching for a specific spare part
    searched_part = tracker.find_spare_part("STR-001")
    if searched_part:
        print(f"Found Spare Part: {searched_part.name}")
    else:
        print("Spare part not found.")
```
