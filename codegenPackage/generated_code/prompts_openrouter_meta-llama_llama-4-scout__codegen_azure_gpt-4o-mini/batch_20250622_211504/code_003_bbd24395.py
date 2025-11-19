"""
Generated Code Metadata:
========================
Original URL: https://aktivrorteknikk.no
Prompt: Develop a simple algorithm for scheduling pipe cleaning and maintenance tasks for a water utility company, taking into account factors like pipe diameter, material, and location.
Generated: DETERMINISTIC_bbd24395fc781087
Batch ID: 20250622_211504
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from datetime import datetime, timedelta
from typing import List, Dict, Any

class Pipe:
    def __init__(self, diameter: float, material: str, location: str):
        """
        Initialize a Pipe object.

        :param diameter: Diameter of the pipe in inches.
        :param material: Material of the pipe (e.g., 'PVC', 'Steel').
        :param location: Location of the pipe (e.g., 'Downtown', 'Uptown').
        """
        self.diameter = diameter
        self.material = material
        self.location = location
        self.last_cleaned = datetime.now() - timedelta(days=30)  # Default to 30 days ago

    def needs_cleaning(self) -> bool:
        """
        Determine if the pipe needs cleaning based on the last cleaned date.

        :return: True if the pipe needs cleaning, False otherwise.
        """
        # Assume pipes need cleaning every 30 days
        return (datetime.now() - self.last_cleaned).days >= 30

    def schedule_cleaning(self) -> None:
        """
        Schedule the next cleaning for the pipe.
        """
        self.last_cleaned = datetime.now()


class MaintenanceScheduler:
    def __init__(self):
        """
        Initialize the MaintenanceScheduler with an empty list of pipes.
        """
        self.pipes: List[Pipe] = []

    def add_pipe(self, pipe: Pipe) -> None:
        """
        Add a pipe to the maintenance scheduler.

        :param pipe: Pipe object to be added.
        """
        self.pipes.append(pipe)

    def schedule_maintenance(self) -> List[Dict[str, Any]]:
        """
        Schedule maintenance for pipes that need cleaning.

        :return: A list of dictionaries containing details of scheduled maintenance.
        """
        scheduled_tasks = []
        for pipe in self.pipes:
            if pipe.needs_cleaning():
                pipe.schedule_cleaning()
                scheduled_tasks.append({
                    'location': pipe.location,
                    'diameter': pipe.diameter,
                    'material': pipe.material,
                    'scheduled_date': pipe.last_cleaned.strftime('%Y-%m-%d %H:%M:%S')
                })
        return scheduled_tasks


def main():
    """
    Main function to demonstrate the scheduling of pipe cleaning and maintenance tasks.
    """
    # Create a maintenance scheduler
    scheduler = MaintenanceScheduler()

    # Add some pipes to the scheduler
    scheduler.add_pipe(Pipe(4.0, 'PVC', 'Downtown'))
    scheduler.add_pipe(Pipe(6.0, 'Steel', 'Uptown'))
    scheduler.add_pipe(Pipe(3.0, 'Copper', 'Suburb'))

    # Schedule maintenance and print the results
    scheduled_tasks = scheduler.schedule_maintenance()
    if scheduled_tasks:
        print("Scheduled Maintenance Tasks:")
        for task in scheduled_tasks:
            print(task)
    else:
        print("No pipes need maintenance at this time.")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {e}")
```
