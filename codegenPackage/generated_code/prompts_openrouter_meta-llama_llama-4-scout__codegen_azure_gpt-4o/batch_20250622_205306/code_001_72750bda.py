"""
Generated Code Metadata:
========================
Original URL: https://peacecitycontracting.com
Prompt: Write a Python script to manage construction projects for a company like Peace City Contracting LLC, including tasks for building construction, renovation, and MEP works.
Generated: DETERMINISTIC_72750bda4a16efd5
Batch ID: 20250622_205306
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import datetime


class ProjectManager:
    """
    A class to manage construction projects for a company.
    Includes tasks for building construction, renovation, and MEP works.
    """

    def __init__(self):
        # Initialize an empty list to store projects
        self.projects = []

    def add_project(self, name, type_of_work, start_date, end_date, budget):
        """
        Add a new project to the list.

        :param name: Name of the project
        :param type_of_work: Type of work (e.g., Building Construction, Renovation, MEP Works)
        :param start_date: Start date of the project (YYYY-MM-DD)
        :param end_date: End date of the project (YYYY-MM-DD)
        :param budget: Budget allocated for the project
        """
        try:
            # Validate dates
            start_date = datetime.datetime.strptime(start_date, "%Y-%m-%d")
            end_date = datetime.datetime.strptime(end_date, "%Y-%m-%d")
            if end_date <= start_date:
                raise ValueError("End date must be after start date.")

            # Create a project dictionary
            project = {
                "name": name,
                "type_of_work": type_of_work,
                "start_date": start_date.strftime("%Y-%m-%d"),
                "end_date": end_date.strftime("%Y-%m-%d"),
                "budget": budget,
                "status": "Active"
            }

            # Add the project to the list
            self.projects.append(project)
            print(f"Project '{name}' added successfully.")
        except ValueError as e:
            print(f"Error adding project: {e}")

    def list_projects(self):
        """
        List all projects with their details.
        """
        if not self.projects:
            print("No projects found.")
            return

        print("Current Projects:")
        for idx, project in enumerate(self.projects, start=1):
            print(f"{idx}. {project['name']} - {project['type_of_work']} - "
                  f"Start: {project['start_date']} - End: {project['end_date']} - "
                  f"Budget: ${project['budget']} - Status: {project['status']}")

    def update_project_status(self, name, status):
        """
        Update the status of a project.

        :param name: Name of the project
        :param status: New status (e.g., Active, Completed, On Hold)
        """
        for project in self.projects:
            if project["name"] == name:
                project["status"] = status
                print(f"Project '{name}' status updated to '{status}'.")
                return
        print(f"Project '{name}' not found.")

    def save_projects_to_file(self, filename):
        """
        Save all projects to a JSON file.

        :param filename: Name of the file to save the projects
        """
        try:
            with open(filename, "w") as file:
                json.dump(self.projects, file, indent=4)
            print(f"Projects saved to '{filename}'.")
        except IOError as e:
            print(f"Error saving projects to file: {e}")

    def load_projects_from_file(self, filename):
        """
        Load projects from a JSON file.

        :param filename: Name of the file to load the projects from
        """
        try:
            with open(filename, "r") as file:
                self.projects = json.load(file)
            print(f"Projects loaded from '{filename}'.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects from file: {e}")


# Example usage
if __name__ == "__main__":
    manager = ProjectManager()

    # Add some projects
    manager.add_project("Skyline Tower", "Building Construction", "2023-01-01", "2023-12-31", 5000000)
    manager.add_project("City Mall Renovation", "Renovation", "2023-03-01", "2023-08-31", 2000000)

    # List all projects
    manager.list_projects()

    # Update project status
    manager.update_project_status("Skyline Tower", "Completed")

    # Save projects to a file
    manager.save_projects_to_file("projects.json")

    # Load projects from a file
    manager.load_projects_from_file("projects.json")

    # List projects again to verify loading
    manager.list_projects()
```
