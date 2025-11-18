"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://econopure.com.vn
Prompt: Create a script to automate the monitoring and maintenance schedule for Econopure's self-cleaning sand filtration systems in industrial settings.
Generated: DETERMINISTIC_cc167a4b27896417
Batch ID: 20250612_154631
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

class FiltrationSystem:
    """Class to represent a self-cleaning sand filtration system."""
    
    def __init__(self, system_id, last_maintenance_date, maintenance_interval_days):
        """
        Initializes a FiltrationSystem instance.

        Args:
            system_id (str): Unique identifier for the filtration system.
            last_maintenance_date (str): Date of the last maintenance (YYYY-MM-DD).
            maintenance_interval_days (int): Number of days between maintenance.
        """
        self.system_id = system_id
        self.last_maintenance_date = datetime.datetime.strptime(last_maintenance_date, '%Y-%m-%d').date()
        self.maintenance_interval_days = maintenance_interval_days

    def is_due_for_maintenance(self):
        """Checks if the system is due for maintenance."""
        next_maintenance_date = self.last_maintenance_date + datetime.timedelta(days=self.maintenance_interval_days)
        return datetime.date.today() >= next_maintenance_date

    def schedule_maintenance(self):
        """Schedules the next maintenance date."""
        if self.is_due_for_maintenance():
            self.last_maintenance_date = datetime.date.today()
            print(f"Maintenance scheduled for system {self.system_id} on {self.last_maintenance_date}.")
        else:
            print(f"System {self.system_id} is not due for maintenance.")


def load_systems_from_file(file_path):
    """Loads filtration systems from a JSON file.

    Args:
        file_path (str): Path to the JSON file containing system data.
        
    Returns:
        list: A list of FiltrationSystem instances.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The specified file does not exist: {file_path}")

    with open(file_path, 'r') as file:
        try:
            systems_data = json.load(file)
        except json.JSONDecodeError as e:
            raise ValueError("Error decoding JSON from the file") from e

    systems = []
    for system in systems_data:
        systems.append(FiltrationSystem(system['system_id'], system['last_maintenance_date'], system['maintenance_interval_days']))
    
    return systems


def main():
    """Main function to automate the monitoring and maintenance schedule."""
    try:
        systems = load_systems_from_file('filtration_systems.json')
        for system in systems:
            system.schedule_maintenance()
    except (FileNotFoundError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

Please ensure to create a `filtration_systems.json` file in the same directory as this script. The JSON file should have the following structure:

```json
[
    {
        "system_id": "System1",
        "last_maintenance_date": "2023-01-01",
        "maintenance_interval_days": 30
    },
    {
        "system_id": "System2",
        "last_maintenance_date": "2023-02-15",
        "maintenance_interval_days": 60
    }
]
```
