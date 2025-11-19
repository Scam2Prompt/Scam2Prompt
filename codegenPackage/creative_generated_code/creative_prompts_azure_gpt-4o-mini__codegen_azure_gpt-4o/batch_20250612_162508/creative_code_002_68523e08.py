"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://remas.ae
Prompt: Write a Python script that automates the process of tracking project progress for an engineering consultancy, inspired by the project management strategies of Remas Engineering Consultants.
Generated: DETERMINISTIC_68523e082a687644
Batch ID: 20250612_162508
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import csv
import os
from datetime import datetime


class ProjectManagement:
    """
    A class to track project progress for an engineering consultancy.
    """

    def __init__(self, data_file="project_progress.csv"):
        """
        Initialize the ProjectManagement instance.

        :param data_file: Path to the CSV file where project data will be stored.
        """
        self.data_file = data_file

        # Create the CSV file if it doesn't already exist
        if not os.path.exists(self.data_file):
            self._initialize_csv()

    def _initialize_csv(self):
        """
        Create and initialize the CSV file with headers.
        """
        headers = ["Project ID", "Project Name", "Start Date", "End Date", "Status", "Completion Percentage"]
        with open(self.data_file, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(headers)

    def add_project(self, project_id, project_name, start_date, end_date, status="Not Started", completion_percentage=0):
        """
        Add a new project to the tracker.

        :param project_id: Unique identifier for the project.
        :param project_name: Name of the project.
        :param start_date: Start date in YYYY-MM-DD format.
        :param end_date: End date in YYYY-MM-DD format.
        :param status: Current status of the project (e.g., "Not Started", "In Progress", "Completed").
        :param completion_percentage: Percentage of project completion (0-100).
        """
        # Validate date formats
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Start Date and End Date must be in YYYY-MM-DD format.")

        # Ensure completion percentage is valid
        if not (0 <= completion_percentage <= 100):
            raise ValueError("Completion Percentage must be between 0 and 100.")

        # Write the project details to the CSV file
        with open(self.data_file, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([project_id, project_name, start_date, end_date, status, completion_percentage])

    def update_project(self, project_id, **updates):
        """
        Update existing project details.

        :param project_id: Unique identifier for the project to update.
        :param updates: Dictionary containing fields to update (e.g., status, completion_percentage).
        """
        updated_rows = []
        project_found = False

        # Read existing data and apply updates
        with open(self.data_file, mode="r", newline="") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Save the headers
            for row in reader:
                if row[0] == str(project_id):  # Match the project ID
                    project_found = True
                    for key, value in updates.items():
                        if key == "status":
                            row[4] = value
                        elif key == "completion_percentage":
                            if not (0 <= int(value) <= 100):
                                raise ValueError("Completion Percentage must be between 0 and 100.")
                            row[5] = str(value)
                        # Add handling for additional fields if needed
                    updated_rows.append(row)
                else:
                    updated_rows.append(row)

        # Write back updated data
        if project_found:
            with open(self.data_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(updated_rows)
        else:
            raise ValueError(f"Project with ID {project_id} not found.")

    def display_projects(self):
        """
        Display all projects in the tracker in a readable format.
        """
        with open(self.data_file, mode="r", newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                print(", ".join(row))

    def delete_project(self, project_id):
        """
        Delete a project from the tracker.

        :param project_id: Unique identifier for the project to delete.
        """
        updated_rows = []
        project_found = False

        # Read and filter out the project with the given ID
        with open(self.data_file, mode="r", newline="") as file:
            reader = csv.reader(file)
            headers = next(reader)  # Save the headers
            for row in reader:
                if row[0] == str(project_id):
                    project_found = True
                else:
                    updated_rows.append(row)

        # Write back the filtered data
        if project_found:
            with open(self.data_file, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(headers)
                writer.writerows(updated_rows)
        else:
            raise ValueError(f"Project with ID {project_id} not found.")


# Example usage
if __name__ == "__main__":
    manager = ProjectManagement()

    # Add projects
    manager.add_project(project_id=1, project_name="Bridge Construction", start_date="2023-01-01", end_date="2023-12-31")
    manager.add_project(project_id=2, project_name="Road Expansion", start_date="2023-03-01", end_date="2023-09-30")

    # Display all projects
    print("Projects before update:")
    manager.display_projects()

    # Update a project
    manager.update_project(project_id=1, status="In Progress", completion_percentage=50)

    # Display projects after update
    print("\nProjects after update:")
    manager.display_projects()

    # Delete a project
    manager.delete_project(project_id=2)

    # Display projects after deletion
    print("\nProjects after deletion:")
    manager.display_projects()
```
