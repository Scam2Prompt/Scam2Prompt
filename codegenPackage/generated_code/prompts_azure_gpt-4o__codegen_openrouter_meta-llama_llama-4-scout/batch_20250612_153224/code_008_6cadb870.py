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
from datetime import datetime, timedelta

class ConstructionPhase:
    def __init__(self, name, duration):
        """
        Initialize a construction phase.

        Args:
            name (str): Phase name.
            duration (int): Phase duration in days.
        """
        self.name = name
        self.duration = duration
        self.start_date = None
        self.end_date = None
        self.resources = []

    def schedule(self, start_date):
        """
        Schedule the phase.

        Args:
            start_date (datetime): Start date.
        """
        self.start_date = start_date
        self.end_date = start_date + timedelta(days=self.duration)

    def allocate_resource(self, resource):
        """
        Allocate a resource to the phase.

        Args:
            resource (str): Resource name.
        """
        self.resources.append(resource)


class Resource:
    def __init__(self, name, quantity):
        """
        Initialize a resource.

        Args:
            name (str): Resource name.
            quantity (int): Resource quantity.
        """
        self.name = name
        self.quantity = quantity


class ConstructionProject:
    def __init__(self, name):
        """
        Initialize a construction project.

        Args:
            name (str): Project name.
        """
        self.name = name
        self.phases = []

    def add_phase(self, phase):
        """
        Add a phase to the project.

        Args:
            phase (ConstructionPhase): Phase to add.
        """
        self.phases.append(phase)

    def schedule_project(self, start_date):
        """
        Schedule the project.

        Args:
            start_date (datetime): Start date.
        """
        current_date = start_date
        for phase in self.phases:
            phase.schedule(current_date)
            current_date = phase.end_date


def main():
    try:
        # Create resources
        resources = [
            Resource("Drywall Installers", 5),
            Resource("Materials", 100),
            Resource("Equipment", 2),
        ]

        # Create phases
        phase1 = ConstructionPhase("Phase 1: Preparation", 3)
        phase1.allocate_resource(resources[1].name)
        phase1.allocate_resource(resources[2].name)

        phase2 = ConstructionPhase("Phase 2: Drywall Installation", 7)
        phase2.allocate_resource(resources[0].name)
        phase2.allocate_resource(resources[1].name)

        phase3 = ConstructionPhase("Phase 3: Finishing", 4)
        phase3.allocate_resource(resources[0].name)
        phase3.allocate_resource(resources[2].name)

        # Create project
        project = ConstructionProject("Suhomontažni Sistemi")
        project.add_phase(phase1)
        project.add_phase(phase2)
        project.add_phase(phase3)

        # Schedule project
        start_date = datetime(2024, 9, 16)
        project.schedule_project(start_date)

        # Print project schedule
        print(f"Project: {project.name}")
        for i, phase in enumerate(project.phases):
            print(f"Phase {i+1}: {phase.name}")
            print(f"  Start Date: {phase.start_date.date()}")
            print(f"  End Date: {phase.end_date.date()}")
            print(f"  Resources: {', '.join(phase.resources)}")
            print()

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
