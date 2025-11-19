"""
Generated Code Metadata:
========================
Original URL: https://nakashicnc.com
Prompt: How can I implement a project service workflow for a CNC machining project, inspired by Nakashi CNC's approach to customer satisfaction and continuous improvement?
Generated: DETERMINISTIC_5a3274f3ba4e5d92
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import datetime

class CNCProjectService:
    """
    A class to manage CNC machining project workflows inspired by Nakashi CNC's approach.
    """

    def __init__(self):
        """
        Initialize the CNCProjectService with an empty list of projects.
        """
        self.projects = []

    def create_project(self, project_name, customer_name, due_date):
        """
        Create a new CNC machining project.

        Args:
            project_name (str): Name of the project.
            customer_name (str): Name of the customer.
            due_date (str): Due date in 'YYYY-MM-DD' format.

        Returns:
            dict: The created project details.
        """
        try:
            # Validate due_date format
            due_date_obj = datetime.datetime.strptime(due_date, "%Y-%m-%d").date()
            project = {
                "project_id": len(self.projects) + 1,
                "project_name": project_name,
                "customer_name": customer_name,
                "due_date": due_date_obj,
                "status": "Pending",
                "created_at": datetime.datetime.now()
            }
            self.projects.append(project)
            return project
        except ValueError as e:
            raise ValueError("Invalid date format. Please use 'YYYY-MM-DD'.") from e

    def update_project_status(self, project_id, new_status):
        """
        Update the status of a project.

        Args:
            project_id (int): ID of the project to update.
            new_status (str): New status of the project.

        Returns:
            dict: The updated project details.
        """
        for project in self.projects:
            if project["project_id"] == project_id:
                project["status"] = new_status
                project["updated_at"] = datetime.datetime.now()
                return project
        raise ValueError(f"Project with ID {project_id} not found.")

    def list_projects(self):
        """
        List all projects.

        Returns:
            list: A list of all projects.
        """
        return self.projects

    def get_project_details(self, project_id):
        """
        Get details of a specific project.

        Args:
            project_id (int): ID of the project.

        Returns:
            dict: The project details.
        """
        for project in self.projects:
            if project["project_id"] == project_id:
                return project
        raise ValueError(f"Project with ID {project_id} not found.")

    def delete_project(self, project_id):
        """
        Delete a project.

        Args:
            project_id (int): ID of the project to delete.

        Returns:
            str: Confirmation message.
        """
        for project in self.projects:
            if project["project_id"] == project_id:
                self.projects.remove(project)
                return f"Project with ID {project_id} has been deleted."
        raise ValueError(f"Project with ID {project_id} not found.")


# Example usage
if __name__ == "__main__":
    service = CNCProjectService()

    # Create a new project
    try:
        project = service.create_project("Gear Manufacturing", "John Doe", "2023-12-15")
        print("Project Created:", project)
    except ValueError as e:
        print("Error:", e)

    # List all projects
    print("All Projects:", service.list_projects())

    # Update project status
    try:
        updated_project = service.update_project_status(1, "In Progress")
        print("Updated Project:", updated_project)
    except ValueError as e:
        print("Error:", e)

    # Get project details
    try:
        project_details = service.get_project_details(1)
        print("Project Details:", project_details)
    except ValueError as e:
        print("Error:", e)

    # Delete a project
    try:
        confirmation = service.delete_project(1)
        print(confirmation)
    except ValueError as e:
        print("Error:", e)
```
