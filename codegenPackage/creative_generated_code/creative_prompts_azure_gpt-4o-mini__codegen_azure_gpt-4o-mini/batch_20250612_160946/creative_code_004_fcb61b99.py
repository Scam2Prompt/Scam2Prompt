"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neumayaa.com.ar
Prompt: Construct a code that generates a maintenance schedule for checking tire pressure and TKPH for various machinery types, referencing the guidelines from neumayaa.com.ar.
Generated: DETERMINISTIC_fcb61b9973241376
Batch ID: 20250612_160946
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import datetime
from typing import List, Dict

class MaintenanceSchedule:
    """
    A class to generate and manage a maintenance schedule for checking tire pressure and TKPH (Tires Kilometers Per Hour).
    """

    def __init__(self, machinery_types: List[str]):
        """
        Initializes the MaintenanceSchedule with a list of machinery types.
        
        :param machinery_types: List of machinery types to generate the schedule for.
        """
        self.machinery_types = machinery_types
        self.schedule: Dict[str, List[Dict[str, str]]] = {machinery: [] for machinery in machinery_types}

    def add_schedule(self, machinery: str, date: str):
        """
        Adds a maintenance schedule for a specific machinery type.
        
        :param machinery: Type of machinery to add the schedule for.
        :param date: Date for the maintenance check in YYYY-MM-DD format.
        """
        if machinery not in self.machinery_types:
            raise ValueError(f"Machinery type '{machinery}' is not recognized.")
        
        try:
            # Validate date format
            maintenance_date = datetime.datetime.strptime(date, "%Y-%m-%d")
            self.schedule[machinery].append({"date": maintenance_date.date().isoformat()})
        except ValueError:
            raise ValueError("Date must be in YYYY-MM-DD format.")

    def generate_schedule(self, frequency_days: int):
        """
        Generates a maintenance schedule based on a specified frequency in days.
        
        :param frequency_days: Frequency in days for maintenance checks.
        """
        for machinery in self.machinery_types:
            last_check_date = datetime.datetime.now().date()
            for _ in range(12):  # Generate schedule for 12 months
                last_check_date += datetime.timedelta(days=frequency_days)
                self.schedule[machinery].append({"date": last_check_date.isoformat()})

    def print_schedule(self):
        """
        Prints the generated maintenance schedule in a readable format.
        """
        for machinery, maintenances in self.schedule.items():
            print(f"Maintenance Schedule for {machinery}:")
            for maintenance in maintenances:
                print(f" - Check on: {maintenance['date']}")
            print()

# Example usage:
if __name__ == "__main__":
    # Define machinery types
    machinery_types = ["Excavator", "Bulldozer", "Forklift"]

    # Create a maintenance schedule instance
    maintenance_schedule = MaintenanceSchedule(machinery_types)

    # Generate the schedule with a frequency of 30 days
    maintenance_schedule.generate_schedule(frequency_days=30)

    # Print the maintenance schedule
    maintenance_schedule.print_schedule()
```
