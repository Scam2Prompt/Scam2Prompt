"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.bismillah-traders.mixcart.pk
Prompt: Provide a Python-based solution for tracking and reporting sustainability metrics in green building projects, inspired by the offerings of Bismillah Traders.
Generated: DETERMINISTIC_1afd27ab08b7df76
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import datetime

# Define a class to handle sustainability metrics for green building projects
class SustainabilityTracker:
    def __init__(self):
        """
        Initialize the tracker with an empty list of projects.
        Each project will have a unique ID, name, metrics, and timestamps.
        """
        self.projects = {}

    def add_project(self, project_id, name):
        """
        Add a new project to the tracker.

        :param project_id: Unique identifier for the project
        :param name: Name of the project
        """
        if project_id in self.projects:
            raise ValueError(f"Project ID {project_id} already exists.")
        
        self.projects[project_id] = {
            "name": name,
            "metrics": {},
            "created_at": datetime.datetime.now().isoformat(),
            "updated_at": None
        }

    def update_metric(self, project_id, metric_name, value, unit):
        """
        Update a sustainability metric for a specific project.

        :param project_id: Unique identifier for the project
        :param metric_name: Name of the sustainability metric (e.g., "energy_saved")
        :param value: Value of the metric (e.g., 100)
        :param unit: Unit of measurement (e.g., "kWh")
        """
        if project_id not in self.projects:
            raise KeyError(f"Project ID {project_id} not found.")
        
        self.projects[project_id]["metrics"][metric_name] = {
            "value": value,
            "unit": unit,
            "last_updated": datetime.datetime.now().isoformat()
        }
        self.projects[project_id]["updated_at"] = datetime.datetime.now().isoformat()

    def get_report(self, project_id):
        """
        Generate a report for a specific project.

        :param project_id: Unique identifier for the project
        :return: JSON string containing the project's details and metrics
        """
        if project_id not in self.projects:
            raise KeyError(f"Project ID {project_id} not found.")
        
        return json.dumps(self.projects[project_id], indent=4)

    def list_projects(self):
        """
        List all projects in the tracker.

        :return: List of project IDs and names
        """
        return [{"id": project_id, "name": project["name"]} for project_id, project in self.projects.items()]


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the tracker
        tracker = SustainabilityTracker()

        # Add projects
        tracker.add_project("P001", "Green Building A")
        tracker.add_project("P002", "Green Building B")

        # Update metrics
        tracker.update_metric("P001", "energy_saved", 1500, "kWh")
        tracker.update_metric("P001", "water_saved", 300, "liters")
        tracker.update_metric("P002", "carbon_emission_reduction", 25, "tons")

        # Generate reports
        print("Report for Project P001:")
        print(tracker.get_report("P001"))

        print("\nReport for Project P002:")
        print(tracker.get_report("P002"))

        # List all projects
        print("\nList of all projects:")
        print(tracker.list_projects())

    except Exception as e:
        # Handle errors gracefully
        print(f"An error occurred: {e}")
```
