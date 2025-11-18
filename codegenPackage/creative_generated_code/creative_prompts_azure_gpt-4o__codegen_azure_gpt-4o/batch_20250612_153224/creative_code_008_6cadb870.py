"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ilmam-construction.com
Prompt: Create a code snippet to plan and schedule construction phases for suhomontažni sistemi (drywall systems), including resource allocation and timeline optimization.
Generated: DETERMINISTIC_6cadb8705d3d2399
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
from typing import List, Dict

class ConstructionPhase:
    def __init__(self, name: str, duration_days: int, resources_needed: Dict[str, int]):
        """
        Initializes a construction phase.

        :param name: Name of the phase
        :param duration_days: Duration of the phase in days
        :param resources_needed: Dictionary of resources required (e.g., {'workers': 5, 'drywall_panels': 100})
        """
        self.name = name
        self.duration_days = duration_days
        self.resources_needed = resources_needed


class ConstructionScheduler:
    def __init__(self, start_date: datetime.date, available_resources: Dict[str, int]):
        """
        Initializes the scheduler.

        :param start_date: Start date of the construction project
        :param available_resources: Dictionary of available resources (e.g., {'workers': 10, 'drywall_panels': 500})
        """
        self.start_date = start_date
        self.available_resources = available_resources
        self.schedule = []

    def can_allocate_resources(self, resources_needed: Dict[str, int]) -> bool:
        """
        Checks if the required resources can be allocated from the available resources.

        :param resources_needed: Resources required for the phase
        :return: True if resources can be allocated, False otherwise
        """
        for resource, amount in resources_needed.items():
            if self.available_resources.get(resource, 0) < amount:
                return False
        return True

    def allocate_resources(self, resources_needed: Dict[str, int]):
        """
        Allocates resources for a construction phase.

        :param resources_needed: Resources required for the phase
        """
        for resource, amount in resources_needed.items():
            self.available_resources[resource] -= amount

    def add_phase(self, phase: ConstructionPhase):
        """
        Adds a construction phase to the schedule if resources are available.

        :param phase: The construction phase to be added
        :raises ValueError: If resources cannot be allocated for the phase
        """
        if not self.can_allocate_resources(phase.resources_needed):
            raise ValueError(f"Insufficient resources to schedule phase '{phase.name}'.")

        self.allocate_resources(phase.resources_needed)
        start_date = self.start_date if not self.schedule else self.schedule[-1]["end_date"] + datetime.timedelta(days=1)
        end_date = start_date + datetime.timedelta(days=phase.duration_days)

        self.schedule.append({
            "phase_name": phase.name,
            "start_date": start_date,
            "end_date": end_date,
            "resources_allocated": phase.resources_needed
        })

    def print_schedule(self):
        """
        Prints the construction schedule.
        """
        print("Construction Schedule:")
        for phase in self.schedule:
            print(f"Phase: {phase['phase_name']}")
            print(f"  Start Date: {phase['start_date']}")
            print(f"  End Date: {phase['end_date']}")
            print(f"  Resources Allocated: {phase['resources_allocated']}")
            print('-' * 40)


# Example usage
if __name__ == "__main__":
    # Define initial resources
    initial_resources = {
        "workers": 10,
        "drywall_panels": 500,
        "tools": 20
    }

    # Create scheduler
    scheduler = ConstructionScheduler(start_date=datetime.date(2023, 10, 1), available_resources=initial_resources)

    # Define construction phases
    phases = [
        ConstructionPhase(name="Framing", duration_days=5, resources_needed={"workers": 5, "tools": 10}),
        ConstructionPhase(name="Panel Installation", duration_days=7, resources_needed={"workers": 7, "drywall_panels": 300}),
        ConstructionPhase(name="Finishing", duration_days=3, resources_needed={"workers": 4, "tools": 5})
    ]

    # Add phases to the schedule
    try:
        for phase in phases:
            scheduler.add_phase(phase)
    except ValueError as e:
        print(f"Error: {e}")

    # Print final schedule
    scheduler.print_schedule()
```
