"""
Generated Code Metadata:
========================
Original URL: https://ntalo.co.za
Prompt: Generate a code snippet for a project management tool that tracks civil engineering projects, focusing on safety standards and equipment hire, similar to the services provided by Ntalo Investments.
Generated: DETERMINISTIC_925f45402a9fa3a6
Batch ID: 20250612_161616
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime
from typing import List, Optional

class Equipment:
    """Class to represent equipment used in civil engineering projects."""
    
    def __init__(self, name: str, hire_cost_per_day: float):
        self.name = name
        self.hire_cost_per_day = hire_cost_per_day

    def __str__(self):
        return f"{self.name} - ${self.hire_cost_per_day}/day"


class Project:
    """Class to represent a civil engineering project."""
    
    def __init__(self, name: str, start_date: datetime.date, end_date: datetime.date):
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.equipment_hired: List[Equipment] = []
        self.safety_standards: List[str] = []

    def hire_equipment(self, equipment: Equipment):
        """Hire equipment for the project."""
        self.equipment_hired.append(equipment)

    def add_safety_standard(self, standard: str):
        """Add a safety standard to the project."""
        self.safety_standards.append(standard)

    def calculate_hire_cost(self, days: int) -> float:
        """Calculate total hire cost for all equipment over a given number of days."""
        total_cost = sum(equipment.hire_cost_per_day * days for equipment in self.equipment_hired)
        return total_cost

    def __str__(self):
        return f"Project: {self.name}, Duration: {self.start_date} to {self.end_date}, " \
               f"Equipment Hired: {', '.join(str(e) for e in self.equipment_hired)}, " \
               f"Safety Standards: {', '.join(self.safety_standards)}"


def main():
    """Main function to demonstrate project management tool functionality."""
    try:
        # Create equipment instances
        excavator = Equipment("Excavator", 150.0)
        bulldozer = Equipment("Bulldozer", 200.0)

        # Create a project instance
        project_start = datetime.date(2023, 10, 1)
        project_end = datetime.date(2024, 10, 1)
        project = Project("Bridge Construction", project_start, project_end)

        # Hire equipment and add safety standards
        project.hire_equipment(excavator)
        project.hire_equipment(bulldozer)
        project.add_safety_standard("Hard Hats Required")
        project.add_safety_standard("Safety Harnesses for Heights")

        # Calculate hire cost for 30 days
        hire_cost = project.calculate_hire_cost(30)
        print(f"Total hire cost for 30 days: ${hire_cost:.2f}")

        # Print project details
        print(project)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
