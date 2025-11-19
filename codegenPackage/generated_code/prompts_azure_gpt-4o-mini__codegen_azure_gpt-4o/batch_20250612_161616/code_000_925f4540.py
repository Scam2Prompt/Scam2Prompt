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

import datetime

class Project:
    """
    Represents a civil engineering project.
    Tracks project details, safety standards, and equipment hire.
    """
    def __init__(self, project_id, name, start_date, end_date, safety_standards):
        """
        Initialize a new project.

        :param project_id: Unique identifier for the project
        :param name: Name of the project
        :param start_date: Project start date (datetime object)
        :param end_date: Project end date (datetime object)
        :param safety_standards: List of safety standards to be followed
        """
        self.project_id = project_id
        self.name = name
        self.start_date = start_date
        self.end_date = end_date
        self.safety_standards = safety_standards
        self.equipment_hired = []  # List to track hired equipment

    def hire_equipment(self, equipment_name, hire_date, return_date):
        """
        Hire equipment for the project.

        :param equipment_name: Name of the equipment
        :param hire_date: Date the equipment is hired (datetime object)
        :param return_date: Date the equipment is returned (datetime object)
        :raises ValueError: If hire_date or return_date is outside project duration
        """
        if hire_date < self.start_date or return_date > self.end_date:
            raise ValueError("Equipment hire dates must be within project duration.")
        
        self.equipment_hired.append({
            "equipment_name": equipment_name,
            "hire_date": hire_date,
            "return_date": return_date
        })

    def get_project_summary(self):
        """
        Generate a summary of the project.

        :return: Dictionary containing project details and hired equipment
        """
        return {
            "project_id": self.project_id,
            "name": self.name,
            "start_date": self.start_date.strftime('%Y-%m-%d'),
            "end_date": self.end_date.strftime('%Y-%m-%d'),
            "safety_standards": self.safety_standards,
            "equipment_hired": self.equipment_hired
        }


# Example usage
if __name__ == "__main__":
    try:
        # Create a new project
        project = Project(
            project_id=1,
            name="Bridge Construction",
            start_date=datetime.datetime(2023, 10, 1),
            end_date=datetime.datetime(2024, 3, 31),
            safety_standards=["Wear helmets", "Use safety harnesses", "Follow OSHA guidelines"]
        )

        # Hire equipment
        project.hire_equipment(
            equipment_name="Excavator",
            hire_date=datetime.datetime(2023, 10, 5),
            return_date=datetime.datetime(2023, 11, 15)
        )
        project.hire_equipment(
            equipment_name="Concrete Mixer",
            hire_date=datetime.datetime(2023, 10, 10),
            return_date=datetime.datetime(2023, 12, 20)
        )

        # Print project summary
        summary = project.get_project_summary()
        print("Project Summary:")
        print(summary)

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
