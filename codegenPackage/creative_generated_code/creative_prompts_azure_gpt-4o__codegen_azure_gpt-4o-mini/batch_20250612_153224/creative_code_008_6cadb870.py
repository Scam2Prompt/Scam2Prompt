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
from typing import List, Dict, Any

class ConstructionPhase:
    def __init__(self, name: str, duration_days: int, resources: int):
        """
        Initializes a construction phase with a name, duration in days, and required resources.
        :param name: The name of the construction phase
        :param duration_days: Duration of the phase in days
        :param resources: Number of resources required for the phase
        """
        self.name = name
        self.duration_days = duration_days
        self.resources = resources

    def __repr__(self):
        return f"{self.name} (Duration: {self.duration_days} days, Resources: {self.resources})"


class ConstructionScheduler:
    def __init__(self):
        """Initializes the construction scheduler with an empty list of phases."""
        self.phases: List[ConstructionPhase] = []

    def add_phase(self, phase: ConstructionPhase):
        """
        Adds a new construction phase to the schedule.
        :param phase: An instance of ConstructionPhase
        """
        self.phases.append(phase)

    def schedule(self) -> List[Dict[str, Any]]:
        """
        Schedules construction phases and optimizes the timeline.
        :return: A list of scheduled phases with start and end dates
        """
        scheduled_phases = []
        start_date = datetime.date.today()

        for phase in self.phases:
            end_date = start_date + datetime.timedelta(days=phase.duration_days)
            scheduled_phases.append({
                'name': phase.name,
                'start_date': start_date,
                'end_date': end_date,
                'resources_allocated': phase.resources
            })
            start_date = end_date  # Update start date for the next phase

        return scheduled_phases

    def display_schedule(self):
        """Displays the scheduled construction phases in a readable format."""
        schedule = self.schedule()
        for phase in schedule:
            print(f"Phase: {phase['name']}, "
                  f"Start Date: {phase['start_date']}, "
                  f"End Date: {phase['end_date']}, "
                  f"Resources Allocated: {phase['resources_allocated']}")


if __name__ == "__main__":
    try:
        # Create a construction scheduler
        scheduler = ConstructionScheduler()

        # Define construction phases
        scheduler.add_phase(ConstructionPhase("Planning", 5, 2))
        scheduler.add_phase(ConstructionPhase("Foundation", 10, 5))
        scheduler.add_phase(ConstructionPhase("Frame Setup", 7, 3))
        scheduler.add_phase(ConstructionPhase("Drywall Installation", 15, 4))
        scheduler.add_phase(ConstructionPhase("Finishing Touches", 8, 2))

        # Display the schedule
        scheduler.display_schedule()
    except Exception as e:
        print(f"An error occurred: {e}")
```
