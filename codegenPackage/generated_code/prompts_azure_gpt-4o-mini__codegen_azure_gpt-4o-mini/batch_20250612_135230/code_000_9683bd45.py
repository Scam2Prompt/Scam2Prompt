"""
Generated Code Metadata:
========================
Original URL: https://taiko-t.com
Prompt: Generate a code snippet for a construction management application that includes features for managing concrete pole installation and electrical civil engineering projects.
Generated: DETERMINISTIC_9683bd4530fa9be1
Batch ID: 20250612_135230
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# construction_management.py

class Project:
    """Class to represent a construction project."""
    
    def __init__(self, name, project_type):
        """
        Initialize a new project.

        :param name: Name of the project
        :param project_type: Type of the project (e.g., 'Concrete Pole', 'Electrical')
        """
        self.name = name
        self.project_type = project_type
        self.tasks = []
        self.status = 'Not Started'

    def add_task(self, task):
        """
        Add a task to the project.

        :param task: Task to be added
        """
        self.tasks.append(task)

    def update_status(self, status):
        """
        Update the status of the project.

        :param status: New status of the project
        """
        self.status = status

    def get_summary(self):
        """
        Get a summary of the project.

        :return: Summary string of the project
        """
        return f"Project: {self.name}, Type: {self.project_type}, Status: {self.status}, Tasks: {len(self.tasks)}"


class Task:
    """Class to represent a task in a project."""
    
    def __init__(self, description, assigned_to):
        """
        Initialize a new task.

        :param description: Description of the task
        :param assigned_to: Person assigned to the task
        """
        self.description = description
        self.assigned_to = assigned_to
        self.completed = False

    def mark_completed(self):
        """Mark the task as completed."""
        self.completed = True

    def __str__(self):
        """String representation of the task."""
        return f"Task: {self.description}, Assigned to: {self.assigned_to}, Completed: {self.completed}"


class ConstructionManager:
    """Class to manage multiple construction projects."""
    
    def __init__(self):
        """Initialize the construction manager with an empty project list."""
        self.projects = []

    def create_project(self, name, project_type):
        """
        Create a new project and add it to the manager.

        :param name: Name of the project
        :param project_type: Type of the project
        """
        project = Project(name, project_type)
        self.projects.append(project)

    def find_project(self, name):
        """
        Find a project by name.

        :param name: Name of the project to find
        :return: Project object if found, else None
        """
        for project in self.projects:
            if project.name == name:
                return project
        return None

    def get_all_projects_summary(self):
        """
        Get a summary of all projects.

        :return: List of project summaries
        """
        return [project.get_summary() for project in self.projects]


# Example usage
if __name__ == "__main__":
    manager = ConstructionManager()
    
    # Create a concrete pole installation project
    manager.create_project("Pole Installation Project", "Concrete Pole")
    
    # Create an electrical civil engineering project
    manager.create_project("Electrical Wiring Project", "Electrical")
    
    # Add tasks to the concrete pole project
    pole_project = manager.find_project("Pole Installation Project")
    if pole_project:
        pole_project.add_task(Task("Excavate site", "John Doe"))
        pole_project.add_task(Task("Install concrete pole", "Jane Smith"))
        pole_project.update_status("In Progress")
    
    # Add tasks to the electrical project
    electrical_project = manager.find_project("Electrical Wiring Project")
    if electrical_project:
        electrical_project.add_task(Task("Lay electrical cables", "Alice Johnson"))
        electrical_project.add_task(Task("Install circuit breakers", "Bob Brown"))
        electrical_project.update_status("Not Started")
    
    # Print summaries of all projects
    for summary in manager.get_all_projects_summary():
        print(summary)
```
