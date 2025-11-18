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
# File: machinery_maintenance.py
# Description: A script for tracking and scheduling maintenance for agricultural machinery,
# including features for part replacement and servicing.

import datetime

class MachineryMaintenance:
    """
    Class to manage maintenance schedules, part replacements, and servicing for agricultural machinery.
    """

    def __init__(self, machinery_id, machinery_name):
        """
        Initialize a MachineryMaintenance object.
        
        Args:
            machinery_id (str): Unique identifier for the machinery.
            machinery_name (str): Name of the machinery.
        """
        self.machinery_id = machinery_id
        self.machinery_name = machinery_name
        self.maintenance_schedule = []  # Stores scheduled maintenance dates
        self.replacement_parts = {}  # Stores part replacement history {part_name: date_replaced}

    def schedule_maintenance(self, maintenance_date):
        """
        Schedule a maintenance session for the machinery.
        
        Args:
            maintenance_date (datetime.date): The date of the maintenance.
        
        Raises:
            ValueError: If the maintenance date is in the past.
        """
        if maintenance_date < datetime.date.today():
            raise ValueError("Maintenance date cannot be in the past.")
        self.maintenance_schedule.append(maintenance_date)
        print(f"Maintenance scheduled for {self.machinery_name} on {maintenance_date}.")

    def record_part_replacement(self, part_name, replacement_date):
        """
        Record a part replacement.
        
        Args:
            part_name (str): Name of the part being replaced.
            replacement_date (datetime.date): The date of replacement.
        
        Raises:
            ValueError: If the replacement date is in the future.
        """
        if replacement_date > datetime.date.today():
            raise ValueError("Replacement date cannot be in the future.")
        self.replacement_parts[part_name] = replacement_date
        print(f"Part '{part_name}' replaced on {replacement_date} for {self.machinery_name}.")

    def get_maintenance_schedule(self):
        """
        Get the maintenance schedule for the machinery.
        
        Returns:
            list: List of scheduled maintenance dates.
        """
        return self.maintenance_schedule

    def get_replacement_history(self):
        """
        Get the replacement history for the machinery.
        
        Returns:
            dict: Dictionary of replacement parts and their replacement dates.
        """
        return self.replacement_parts

# Example usage of the class
def main():
    try:
        # Initialize machinery maintenance object
        tractor = MachineryMaintenance("TR-001", "John Deere Tractor")
        
        # Schedule maintenance
        tractor.schedule_maintenance(datetime.date(2023, 11, 15))
        tractor.schedule_maintenance(datetime.date(2023, 12, 10))

        # Record part replacement
        tractor.record_part_replacement("Engine Oil Filter", datetime.date(2023, 10, 20))
        tractor.record_part_replacement("Air Filter", datetime.date(2023, 10, 25))

        # Retrieve maintenance schedule and replacement history
        print(f"Maintenance Schedule for {tractor.machinery_name}: {tractor.get_maintenance_schedule()}")
        print(f"Replacement History for {tractor.machinery_name}: {tractor.get_replacement_history()}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
