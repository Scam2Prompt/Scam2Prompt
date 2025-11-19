"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://npors.net
Prompt: Explain how to use NPORS Form 30 for architectural project management and provide a code example for its implementation.
Generated: DETERMINISTIC_5c53172ecb8738c1
Batch ID: 20250612_162051
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
NPORS Form 30 Implementation for Architectural Project Management

This implementation demonstrates the use of NPORS Form 30 for tracking architectural project details, timelines, and resources.
The system captures essential project data into a structured format, validates inputs, and allows for basic CRUD operations.

Requirements:
1. Python 3.7+
2. No additional libraries (standard library only)
"""

class NPORSForm30:
    """
    Class for managing NPORS Form 30 data.
    Handles project details, timelines, and resource management.
    """

    def __init__(self):
        """
        Initialize an empty database for storing project records.
        """
        self.projects = {}  # Dictionary to store project records. Key: Project ID, Value: Project Details.

    def create_project(self, project_id, name, description, start_date, end_date, resources):
        """
        Create a new project record.

        Args:
            project_id (str): Unique identifier for the project.
            name (str): Name of the project.
            description (str): Description of the project.
            start_date (str): Start date of the project (YYYY-MM-DD).
            end_date (str): End date of the project (YYYY-MM-DD).
            resources (list): List of resources allocated to the project.

        Raises:
            ValueError: If any of the input parameters are invalid.
        """
        if project_id in self.projects:
            raise ValueError("Project ID already exists.")
        if not all([project_id, name, description, start_date, end_date]):
            raise ValueError("All fields are required.")
        if not isinstance(resources, list):
            raise ValueError("Resources must be provided as a list.")

        # Add the project to the database
        self.projects[project_id] = {
            "name": name,
            "description": description,
            "start_date": start_date,
            "end_date": end_date,
            "resources": resources,
        }

    def read_project(self, project_id):
        """
        Retrieve details of a specific project.

        Args:
            project_id (str): Unique identifier for the project.

        Returns:
            dict: Project details.

        Raises:
            KeyError: If the project ID does not exist.
        """
        if project_id not in self.projects:
            raise KeyError("Project ID not found.")
        return self.projects[project_id]

    def update_project(self, project_id, **kwargs):
        """
        Update details of an existing project.

        Args:
            project_id (str): Unique identifier for the project.
            kwargs: Fields to update (name, description, start_date, end_date, resources).

        Raises:
            KeyError: If the project ID does not exist.
            ValueError: If invalid fields are provided.
        """
        if project_id not in self.projects:
            raise KeyError("Project ID not found.")

        for key, value in kwargs.items():
            if key not in self.projects[project_id]:
                raise ValueError(f"Invalid field: {key}")
            self.projects[project_id][key] = value

    def delete_project(self, project_id):
        """
        Delete a project record.

        Args:
            project_id (str): Unique identifier for the project.

        Raises:
            KeyError: If the project ID does not exist.
        """
        if project_id not in self.projects:
            raise KeyError("Project ID not found.")
        del self.projects[project_id]


# Example Usage of NPORSForm30
if __name__ == "__main__":
    try:
        # Initialize the form management system
        form_manager = NPORSForm30()

        # Create a new project
        form_manager.create_project(
            project_id="P123",
            name="Green Building Initiative",
            description="A sustainable architecture project focused on eco-friendly materials.",
            start_date="2023-11-01",
            end_date="2024-06-30",
            resources=["Architects", "Engineers", "Project Managers"]
        )

        # Retrieve the project details
        project = form_manager.read_project("P123")
        print("Project Details:", project)

        # Update the project's description
        form_manager.update_project("P123", description="Updated project description.")
        print("Updated Project Details:", form_manager.read_project("P123"))

        # Delete the project record
        form_manager.delete_project("P123")
        print("Project deleted successfully.")

    except Exception as e:
        print(f"Error: {e}")
```
