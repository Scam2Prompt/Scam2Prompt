"""
Generated Code Metadata:
========================
Original URL: https://unapatches.com
Prompt: Create a detailed plan for a metal fabrication project that includes CNC cutting, punching, and welding, inspired by the services of Jupiter Design & Manufacturing.
Generated: DETERMINISTIC_3ad6a174ae73cd92
Batch ID: 20250612_163924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime, timedelta

class MetalFabricationProject:
    def __init__(self, project_name, client_name, materials, services):
        """
        Initialize a new metal fabrication project.

        :param project_name: Name of the project
        :param client_name: Name of the client
        :param materials: List of materials to be used
        :param services: List of services to be performed (CNC cutting, punching, welding)
        """
        self.project_name = project_name
        self.client_name = client_name
        self.materials = materials
        self.services = services
        self.start_date = None
        self.end_date = None
        self.status = "Not Started"

    def set_schedule(self, start_date, duration_days):
        """
        Set the project schedule.

        :param start_date: Start date of the project
        :param duration_days: Duration of the project in days
        """
        try:
            self.start_date = datetime.strptime(start_date, "%Y-%m-%d")
            self.end_date = self.start_date + timedelta(days=duration_days)
        except ValueError as e:
            raise ValueError("Invalid date format. Please use YYYY-MM-DD.") from e

    def update_status(self, new_status):
        """
        Update the status of the project.

        :param new_status: New status of the project
        """
        valid_statuses = ["Not Started", "In Progress", "Completed", "On Hold"]
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status. Choose from {valid_statuses}.")

    def to_dict(self):
        """
        Convert the project details to a dictionary.

        :return: Dictionary representation of the project
        """
        return {
            "project_name": self.project_name,
            "client_name": self.client_name,
            "materials": self.materials,
            "services": self.services,
            "start_date": self.start_date.strftime("%Y-%m-%d") if self.start_date else None,
            "end_date": self.end_date.strftime("%Y-%m-%d") if self.end_date else None,
            "status": self.status
        }

    def save_to_file(self, filename):
        """
        Save the project details to a JSON file.

        :param filename: Name of the file to save the project details
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            raise IOError("An error occurred while writing to the file.") from e

# Example usage
if __name__ == "__main__":
    # Create a new metal fabrication project
    project = MetalFabricationProject(
        project_name="Custom Metal Frame",
        client_name="Jupiter Design & Manufacturing",
        materials=["Steel", "Aluminum"],
        services=["CNC Cutting", "Punching", "Welding"]
    )

    # Set the project schedule
    project.set_schedule(start_date="2023-10-01", duration_days=30)

    # Update the project status
    project.update_status("In Progress")

    # Save project details to a file
    project.save_to_file("metal_fabrication_project.json")

    print("Project details saved successfully.")
```
