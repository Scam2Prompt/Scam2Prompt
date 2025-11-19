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
from dataclasses import dataclass
from datetime import datetime, timedelta
from enum import Enum
from typing import List

class PipeMaterial(str, Enum):
    """Enum for pipe materials."""
    PVC = "PVC"
    CastIron = "Cast Iron"
    Steel = "Steel"
    Concrete = "Concrete"

@dataclass
class Pipe:
    """Class representing a pipe."""
    diameter: float  # in inches
    material: PipeMaterial
    location: str
    last_maintenance: datetime = None

class PipeMaintenanceScheduler:
    """Class responsible for scheduling pipe cleaning and maintenance tasks."""

    def __init__(self, pipes: List[Pipe]):
        """
        Initialize the scheduler with a list of pipes.

        Args:
        pipes (List[Pipe]): A list of Pipe objects.
        """
        self.pipes = pipes

    def schedule_maintenance(self):
        """
        Schedule maintenance tasks for all pipes.

        Returns:
        List[dict]: A list of dictionaries containing maintenance information.
        """
        maintenance_tasks = []
        for pipe in self.pipes:
            if pipe.last_maintenance is None:
                # If no maintenance has been performed, schedule one immediately
                maintenance_date = datetime.now()
            else:
                # Schedule maintenance based on pipe material and diameter
                maintenance_interval = self.get_maintenance_interval(pipe)
                maintenance_date = pipe.last_maintenance + maintenance_interval

            maintenance_tasks.append({
                "pipe": {
                    "diameter": pipe.diameter,
                    "material": pipe.material.value,
                    "location": pipe.location
                },
                "maintenance_date": maintenance_date
            })

        return maintenance_tasks

    def get_maintenance_interval(self, pipe: Pipe) -> timedelta:
        """
        Determine the maintenance interval for a pipe based on its material and diameter.

        Args:
        pipe (Pipe): A Pipe object.

        Returns:
        timedelta: The maintenance interval.
        """
        # Maintenance intervals in days
        intervals = {
            PipeMaterial.PVC: 365,  # 1 year
            PipeMaterial.CastIron: 180,  # 6 months
            PipeMaterial.Steel: 365,  # 1 year
            PipeMaterial.Concrete: 365  # 1 year
        }

        # Adjust interval based on pipe diameter
        if pipe.diameter < 8:
            diameter_factor = 0.5
        elif pipe.diameter < 16:
            diameter_factor = 1
        else:
            diameter_factor = 2

        interval_days = intervals[pipe.material] * diameter_factor
        return timedelta(days=interval_days)

def main():
    # Example usage
    pipes = [
        Pipe(10, PipeMaterial.PVC, "Main St"),
        Pipe(12, PipeMaterial.CastIron, "Downtown"),
        Pipe(8, PipeMaterial.Steel, "Industrial Area"),
        Pipe(16, PipeMaterial.Concrete, "Residential Area")
    ]

    # Simulate last maintenance for some pipes
    pipes[0].last_maintenance = datetime.now() - timedelta(days=180)
    pipes[1].last_maintenance = datetime.now() - timedelta(days=90)

    scheduler = PipeMaintenanceScheduler(pipes)
    maintenance_tasks = scheduler.schedule_maintenance()

    for task in maintenance_tasks:
        print(f"Pipe at {task['pipe']['location']}:")
        print(f"  Diameter: {task['pipe']['diameter']} inches")
        print(f"  Material: {task['pipe']['material']}")
        print(f"  Maintenance Date: {task['maintenance_date']}")
        print()

if __name__ == "__main__":
    main()
```
