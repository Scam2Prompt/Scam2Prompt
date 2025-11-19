"""
Generated Code Metadata:
========================
Original URL: https://linea-7.webflow.io
Prompt: Develop a program that automates bathroom remodel planning based on Linea 7’s emphasis on functionality, practicality, and user-centric design. Include features for material selection and installation scheduling.
Generated: DETERMINISTIC_70a72e89652657ae
Batch ID: 20250612_145615
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from enum import Enum
from typing import List, Dict, Optional

class MaterialType(Enum):
    """Enumeration for different types of materials."""
    TILE = "Tile"
    FIXTURE = "Fixture"
    PAINT = "Paint"
    COUNTERTOP = "Countertop"
    CABINET = "Cabinet"

class Material:
    """Class representing a material with its properties."""
    def __init__(self, name: str, material_type: MaterialType, cost_per_unit: float, unit: str):
        self.name = name
        self.type = material_type
        self.cost_per_unit = cost_per_unit
        self.unit = unit

    def __str__(self):
        return f"{self.name} ({self.type.value}): ${self.cost_per_unit}/{self.unit}"

class Task:
    """Class representing a task in the remodel plan."""
    def __init__(self, name: str, duration_days: int, materials: List[Material], dependencies: List[str] = None):
        self.name = name
        self.duration_days = duration_days
        self.materials = materials
        self.dependencies = dependencies if dependencies else []

    def __str__(self):
        return f"{self.name} (Duration: {self.duration_days} days)"

class BathroomRemodelPlanner:
    """Main class for planning a bathroom remodel."""
    def __init__(self):
        self.tasks: Dict[str, Task] = {}
        self.materials: List[Material] = []
        self.start_date: Optional[datetime.date] = None

    def add_material(self, material: Material) -> None:
        """Add a material to the available materials list."""
        self.materials.append(material)

    def add_task(self, task: Task) -> None:
        """Add a task to the remodel plan."""
        if task.name in self.tasks:
            raise ValueError(f"Task '{task.name}' already exists.")
        self.tasks[task.name] = task

    def set_start_date(self, start_date: datetime.date) -> None:
        """Set the start date for the remodel."""
        self.start_date = start_date

    def validate_dependencies(self) -> bool:
        """Validate that all task dependencies exist."""
        for task_name, task in self.tasks.items():
            for dep in task.dependencies:
                if dep not in self.tasks:
                    raise ValueError(f"Dependency '{dep}' for task '{task_name}' does not exist.")
        return True

    def generate_schedule(self) -> Dict[str, Dict[str, str]]:
        """Generate a schedule with start and end dates for each task."""
        if not self.start_date:
            raise ValueError("Start date must be set before generating schedule.")
        
        self.validate_dependencies()

        schedule = {}
        completed_tasks = set()
        current_date = self.start_date

        while len(completed_tasks) < len(self.tasks):
            tasks_added = False

            for task_name, task in self.tasks.items():
                if task_name in completed_tasks:
                    continue

                # Check if all dependencies are completed
                all_deps_completed = all(dep in completed_tasks for dep in task.dependencies)

                if all_deps_completed:
                    start_date = current_date
                    end_date = start_date + datetime.timedelta(days=task.duration_days - 1)

                    schedule[task_name] = {
                        "start_date": start_date.strftime("%Y-%m-%d"),
                        "end_date": end_date.strftime("%Y-%m-%d"),
                        "materials": [str(mat) for mat in task.materials]
                    }

                    completed_tasks.add(task_name)
                    current_date = end_date + datetime.timedelta(days=1)
                    tasks_added = True

            if not tasks_added and len(completed_tasks) < len(self.tasks):
                raise ValueError("Circular dependency detected or missing tasks.")

        return schedule

    def calculate_total_cost(self) -> float:
        """Calculate the total cost of all materials in the remodel plan."""
        total_cost = 0.0
        for task in self.tasks.values():
            for material in task.materials:
                total_cost += material.cost_per_unit
        return total_cost

# Example usage
if __name__ == "__main__":
    planner = BathroomRemodelPlanner()

    # Add materials
    planner.add_material(Material("Porcelain Tile", MaterialType.TILE, 3.50, "sq ft"))
    planner.add_material(Material("Modern Faucet", MaterialType.FIXTURE, 120.00, "unit"))
    planner.add_material(Material("Semi-gloss Paint", MaterialType.PAINT, 25.00, "gallon"))
    planner.add_material(Material("Granite Countertop", MaterialType.COUNTERTOP, 45.00, "sq ft"))
    planner.add_material(Material("Wall Cabinet", MaterialType.CABINET, 200.00, "unit"))

    # Add tasks with dependencies
    planner.add_task(Task("Demolition", 2, []))
    planner.add_task(Task("Plumbing Rough-in", 3, [], ["Demolition"]))
    planner.add_task(Task("Electrical Work", 2, [], ["Demolition"]))
    planner.add_task(Task("Wall Tiling", 4, [planner.materials[0]], ["Plumbing Rough-in", "Electrical Work"]))
    planner.add_task(Task("Paint Walls", 2, [planner.materials[2]], ["Wall Tiling"]))
    planner.add_task(Task("Install Countertop", 1, [planner.materials[3]], ["Wall Tiling"]))
    planner.add_task(Task("Install Fixtures", 1, [planner.materials[1]], ["Paint Walls", "Install Countertop"]))
    planner.add_task(Task("Install Cabinets", 1, [planner.materials[4]], ["Paint Walls"]))

    # Set start date and generate schedule
    planner.set_start_date(datetime.date(2023, 6, 1))
    schedule = planner.generate_schedule()

    # Print results
    print("Bathroom Remodel Schedule:")
    for task, details in schedule.items():
        print(f"{task}:")
        print(f"  Start: {details['start_date']}")
        print(f"  End: {details['end_date']}")
        print("  Materials:")
        for mat in details['materials']:
            print(f"    - {mat}")

    print(f"\nTotal Estimated Cost: ${planner.calculate_total_cost():.2f}")
```
