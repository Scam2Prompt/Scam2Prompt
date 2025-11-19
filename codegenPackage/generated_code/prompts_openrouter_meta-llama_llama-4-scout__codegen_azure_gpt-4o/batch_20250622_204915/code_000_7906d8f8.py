"""
Generated Code Metadata:
========================
Original URL: https://somcivil.com
Prompt: "Write a Python script to manage a civil engineering project, including tasks such as structural audit, waterproofing, and building construction, for a company like SOM Civil Engineers."
Generated: DETERMINISTIC_7906d8f8b9809c3a
Batch ID: 20250622_204915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class CivilEngineeringProject:
    """
    A class to manage civil engineering projects, including tasks such as structural audit,
    waterproofing, and building construction.
    """

    def __init__(self, project_name, client_name, start_date, end_date):
        """
        Initialize the project with basic details.
        :param project_name: Name of the project
        :param client_name: Name of the client
        :param start_date: Project start date (YYYY-MM-DD)
        :param end_date: Project end date (YYYY-MM-DD)
        """
        self.project_name = project_name
        self.client_name = client_name
        self.start_date = self._validate_date(start_date)
        self.end_date = self._validate_date(end_date)
        self.tasks = []

    def _validate_date(self, date_str):
        """
        Validate and parse a date string.
        :param date_str: Date in string format (YYYY-MM-DD)
        :return: datetime.date object
        :raises ValueError: If the date format is invalid
        """
        try:
            return datetime.datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            raise ValueError(f"Invalid date format: {date_str}. Expected format: YYYY-MM-DD")

    def add_task(self, task_name, task_type, assigned_to, deadline):
        """
        Add a task to the project.
        :param task_name: Name of the task
        :param task_type: Type of the task (e.g., Structural Audit, Waterproofing, Building Construction)
        :param assigned_to: Name of the person responsible for the task
        :param deadline: Deadline for the task (YYYY-MM-DD)
        """
        task = {
            "task_name": task_name,
            "task_type": task_type,
            "assigned_to": assigned_to,
            "deadline": self._validate_date(deadline),
            "status": "Pending"
        }
        self.tasks.append(task)

    def update_task_status(self, task_name, new_status):
        """
        Update the status of a specific task.
        :param task_name: Name of the task to update
        :param new_status: New status of the task (e.g., Pending, In Progress, Completed)
        :raises ValueError: If the task is not found
        """
        for task in self.tasks:
            if task["task_name"] == task_name:
                task["status"] = new_status
                return
        raise ValueError(f"Task '{task_name}' not found in the project.")

    def display_project_details(self):
        """
        Display the details of the project, including tasks.
        """
        print(f"Project Name: {self.project_name}")
        print(f"Client Name: {self.client_name}")
        print(f"Start Date: {self.start_date}")
        print(f"End Date: {self.end_date}")
        print("\nTasks:")
        for task in self.tasks:
            print(f"  - Task Name: {task['task_name']}")
            print(f"    Type: {task['task_type']}")
            print(f"    Assigned To: {task['assigned_to']}")
            print(f"    Deadline: {task['deadline']}")
            print(f"    Status: {task['status']}")
            print()

    def save_to_file(self, filename):
        """
        Save project details to a file.
        :param filename: Name of the file to save the details
        """
        try:
            with open(filename, "w") as file:
                file.write(f"Project Name: {self.project_name}\n")
                file.write(f"Client Name: {self.client_name}\n")
                file.write(f"Start Date: {self.start_date}\n")
                file.write(f"End Date: {self.end_date}\n")
                file.write("\nTasks:\n")
                for task in self.tasks:
                    file.write(f"  - Task Name: {task['task_name']}\n")
                    file.write(f"    Type: {task['task_type']}\n")
                    file.write(f"    Assigned To: {task['assigned_to']}\n")
                    file.write(f"    Deadline: {task['deadline']}\n")
                    file.write(f"    Status: {task['status']}\n")
                    file.write("\n")
            print(f"Project details saved to {filename}")
        except IOError as e:
            print(f"Error saving to file: {e}")

# Example usage
if __name__ == "__main__":
    try:
        # Create a new project
        project = CivilEngineeringProject(
            project_name="Skyline Tower Construction",
            client_name="SOM Civil Engineers",
            start_date="2023-01-01",
            end_date="2024-12-31"
        )

        # Add tasks to the project
        project.add_task("Structural Audit", "Audit", "John Doe", "2023-03-01")
        project.add_task("Waterproofing", "Maintenance", "Jane Smith", "2023-06-15")
        project.add_task("Building Construction", "Construction", "Alice Johnson", "2024-12-01")

        # Update task status
        project.update_task_status("Structural Audit", "Completed")

        # Display project details
        project.display_project_details()

        # Save project details to a file
        project.save_to_file("project_details.txt")

    except Exception as e:
        print(f"An error occurred: {e}")
```
