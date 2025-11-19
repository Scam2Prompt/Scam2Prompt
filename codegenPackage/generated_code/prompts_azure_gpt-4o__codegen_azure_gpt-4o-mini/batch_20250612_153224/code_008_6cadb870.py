"""
Generated Code Metadata:
========================
Original URL: https://ilmam-construction.com
Prompt: Create a code snippet to plan and schedule construction phases for suhomontažni sistemi (drywall systems), including resource allocation and timeline optimization.
Generated: DETERMINISTIC_6cadb8705d3d2399
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
from typing import List, Dict, Any

class ConstructionPhase:
    def __init__(self, name: str, duration_days: int, resources: List[str]):
        """
        Initialize a construction phase.

        :param name: Name of the construction phase
        :param duration_days: Duration of the phase in days
        :param resources: List of resources required for the phase
        """
        self.name = name
        self.duration_days = duration_days
        self.resources = resources
        self.start_date = None
        self.end_date = None

    def schedule(self, start_date: datetime.date):
        """
        Schedule the phase based on the start date.

        :param start_date: The date when the phase starts
        """
        self.start_date = start_date
        self.end_date = start_date + datetime.timedelta(days=self.duration_days)

    def __repr__(self):
        return f"{self.name}: {self.start_date} to {self.end_date} (Resources: {', '.join(self.resources)})"


class ConstructionScheduler:
    def __init__(self):
        """
        Initialize the construction scheduler with an empty list of phases.
        """
        self.phases: List[ConstructionPhase] = []

    def add_phase(self, phase: ConstructionPhase):
        """
        Add a construction phase to the scheduler.

        :param phase: An instance of ConstructionPhase to be added
        """
        self.phases.append(phase)

    def schedule_phases(self, start_date: datetime.date):
        """
        Schedule all phases starting from a given date.

        :param start_date: The date when the first phase starts
        """
        current_start_date = start_date
        for phase in self.phases:
            phase.schedule(current_start_date)
            current_start_date = phase.end_date + datetime.timedelta(days=1)  # Add a day buffer

    def get_schedule(self) -> List[Dict[str, Any]]:
        """
        Get the schedule of all phases.

        :return: A list of dictionaries containing phase details
        """
        return [{"name": phase.name, "start_date": phase.start_date, "end_date": phase.end_date, "resources": phase.resources} for phase in self.phases]


def main():
    # Create a construction scheduler
    scheduler = ConstructionScheduler()

    # Define construction phases
    phase1 = ConstructionPhase("Frame Installation", 5, ["Carpenter", "Materials"])
    phase2 = ConstructionPhase("Drywall Hanging", 7, ["Drywall Installer", "Drywall"])
    phase3 = ConstructionPhase("Finishing", 3, ["Finisher", "Paint"])

    # Add phases to the scheduler
    scheduler.add_phase(phase1)
    scheduler.add_phase(phase2)
    scheduler.add_phase(phase3)

    # Schedule phases starting from today
    try:
        start_date = datetime.date.today()
        scheduler.schedule_phases(start_date)

        # Print the scheduled phases
        schedule = scheduler.get_schedule()
        for phase in schedule:
            print(phase)

    except Exception as e:
        print(f"An error occurred while scheduling: {e}")


if __name__ == "__main__":
    main()
```
