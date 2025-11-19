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
# project_management_tool.py

from datetime import datetime
from typing import List, Dict

class Equipment:
    """Represents equipment hired for a project."""

    def __init__(self, name: str, hire_date: datetime, return_date: datetime):
        """
        Initializes an Equipment object.

        Args:
        - name (str): The name of the equipment.
        - hire_date (datetime): The date the equipment was hired.
        - return_date (datetime): The date the equipment is expected to be returned.
        """
        self.name = name
        self.hire_date = hire_date
        self.return_date = return_date

    def __str__(self):
        return f"Equipment: {self.name}, Hire Date: {self.hire_date}, Return Date: {self.return_date}"


class SafetyStandard:
    """Represents a safety standard for a project."""

    def __init__(self, name: str, description: str, status: str):
        """
        Initializes a SafetyStandard object.

        Args:
        - name (str): The name of the safety standard.
        - description (str): A description of the safety standard.
        - status (str): The status of the safety standard (e.g., "Met", "Not Met").
        """
        self.name = name
        self.description = description
        self.status = status

    def __str__(self):
        return f"Safety Standard: {self.name}, Description: {self.description}, Status: {self.status}"


class Project:
    """Represents a civil engineering project."""

    def __init__(self, name: str, start_date: datetime, end_date: datetime):
        """
        Initializes a Project object.

        Args:
        - name (str): The name of the project.
        - start_date (datetime): The start date of the project.
        - end_date (datetime): The end date of the project.
        """
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.equipment: List[Equipment] = []
        self.safety_standards: List[SafetyStandard] = []

    def add_equipment(self, equipment: Equipment):
        """Adds equipment to the project."""
        self.equipment.append(equipment)

    def add_safety_standard(self, safety_standard: SafetyStandard):
        """Adds a safety standard to the project."""
        self.safety_standards.append(safety_standard)

    def __str__(self):
        project_info = f"Project: {self.name}, Start Date: {self.start_date}, End Date: {self.end_date}\n"
        equipment_info = "\n".join([str(e) for e in self.equipment])
        safety_standards_info = "\n".join([str(s) for s in self.safety_standards])

        return f"{project_info}\nEquipment:\n{equipment_info}\n\nSafety Standards:\n{safety_standards_info}"


class ProjectManagementTool:
    """Manages civil engineering projects."""

    def __init__(self):
        self.projects: Dict[str, Project] = {}

    def add_project(self, project: Project):
        """Adds a project to the tool."""
        self.projects[project.name] = project

    def get_project(self, project_name: str) -> Project:
        """
        Retrieves a project by name.

        Args:
        - project_name (str): The name of the project.

        Returns:
        - Project: The project object if found, otherwise None.
        """
        return self.projects.get(project_name)

    def __str__(self):
        projects_info = "\n\n".join([str(p) for p in self.projects.values()])
        return projects_info


def main():
    try:
        # Create a project management tool
        tool = ProjectManagementTool()

        # Create a project
        project = Project(
            "Highway Construction",
            datetime(2024, 1, 1),
            datetime(2024, 12, 31)
        )

        # Add equipment to the project
        project.add_equipment(Equipment("Crane", datetime(2024, 1, 5), datetime(2024, 6, 30)))
        project.add_equipment(Equipment("Excavator", datetime(2024, 2, 10), datetime(2024, 8, 31)))

        # Add safety standards to the project
        project.add_safety_standard(SafetyStandard("Hard Hat", "All personnel must wear hard hats on site.", "Met"))
        project.add_safety_standard(SafetyStandard("Safety Harnesses", "All personnel must wear safety harnesses when working at heights.", "Not Met"))

        # Add the project to the tool
        tool.add_project(project)

        # Print the project management tool info
        print(tool)

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
