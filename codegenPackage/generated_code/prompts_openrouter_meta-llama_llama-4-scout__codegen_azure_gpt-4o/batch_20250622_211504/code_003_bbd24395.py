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
import datetime
from typing import List, Dict, Tuple

# Define a class to represent a pipe
class Pipe:
    def __init__(self, pipe_id: int, diameter: float, material: str, location: str):
        """
        Initialize a Pipe object.

        :param pipe_id: Unique identifier for the pipe
        :param diameter: Diameter of the pipe in inches
        :param material: Material of the pipe (e.g., "PVC", "Steel", "Concrete")
        :param location: Location of the pipe (e.g., "Zone A", "Zone B")
        """
        self.pipe_id = pipe_id
        self.diameter = diameter
        self.material = material
        self.location = location

# Define a class to represent a maintenance schedule
class MaintenanceSchedule:
    def __init__(self):
        """
        Initialize a MaintenanceSchedule object.
        """
        self.schedule = []  # List to store scheduled tasks

    def add_task(self, pipe: Pipe, date: datetime.date):
        """
        Add a maintenance task to the schedule.

        :param pipe: Pipe object to be maintained
        :param date: Scheduled date for maintenance
        """
        self.schedule.append({"pipe_id": pipe.pipe_id, "date": date, "location": pipe.location})

    def get_schedule(self) -> List[Dict]:
        """
        Retrieve the maintenance schedule.

        :return: List of scheduled tasks
        """
        return self.schedule

# Define a function to calculate the next maintenance date based on pipe attributes
def calculate_next_maintenance_date(pipe: Pipe) -> datetime.date:
    """
    Calculate the next maintenance date for a pipe based on its attributes.

    :param pipe: Pipe object
    :return: Next maintenance date
    """
    today = datetime.date.today()

    # Determine maintenance frequency based on pipe material
    if pipe.material == "PVC":
        frequency_days = 365  # Once a year
    elif pipe.material == "Steel":
        frequency_days = 180  # Twice a year
    elif pipe.material == "Concrete":
        frequency_days = 90  # Four times a year
    else:
        frequency_days = 365  # Default to once a year

    # Adjust frequency based on pipe diameter
    if pipe.diameter > 24:  # Large pipes
        frequency_days = int(frequency_days * 0.75)  # Increase frequency by 25%

    return today + datetime.timedelta(days=frequency_days)

# Define a function to generate a maintenance schedule
def generate_schedule(pipes: List[Pipe]) -> MaintenanceSchedule:
    """
    Generate a maintenance schedule for a list of pipes.

    :param pipes: List of Pipe objects
    :return: MaintenanceSchedule object
    """
    schedule = MaintenanceSchedule()

    for pipe in pipes:
        try:
            next_date = calculate_next_maintenance_date(pipe)
            schedule.add_task(pipe, next_date)
        except Exception as e:
            # Log error and continue with the next pipe
            print(f"Error scheduling maintenance for pipe {pipe.pipe_id}: {e}")

    return schedule

# Example usage
if __name__ == "__main__":
    # Create a list of pipes
    pipes = [
        Pipe(pipe_id=1, diameter=12, material="PVC", location="Zone A"),
        Pipe(pipe_id=2, diameter=30, material="Steel", location="Zone B"),
        Pipe(pipe_id=3, diameter=18, material="Concrete", location="Zone C"),
        Pipe(pipe_id=4, diameter=36, material="Unknown", location="Zone D"),
    ]

    # Generate the maintenance schedule
    schedule = generate_schedule(pipes)

    # Print the schedule
    for task in schedule.get_schedule():
        print(f"Pipe ID: {task['pipe_id']}, Date: {task['date']}, Location: {task['location']}")
```
