"""
Generated Code Metadata:
========================
Original URL: https://www.swellnetwork.tv
Prompt: How can I implement a project-based model for creative services in my application, similar to the approach used by Swell Creative Management?
Generated: DETERMINISTIC_dafd2577ae618af0
Batch ID: 20250612_161235
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_management.py

class Project:
    """
    A class to represent a creative service project.

    Attributes:
    ----------
    project_id : int
        Unique identifier for the project.
    name : str
        Name of the project.
    description : str
        Detailed description of the project.
    status : str
        Current status of the project (e.g., 'pending', 'in_progress', 'completed').
    team_members : list
        List of team members assigned to the project.
    """

    def __init__(self, project_id, name, description):
        """
        Initializes a new project with the given parameters.

        Parameters:
        ----------
        project_id : int
            Unique identifier for the project.
        name : str
            Name of the project.
        description : str
            Detailed description of the project.
        """
        self.project_id = project_id
        self.name = name
        self.description = description
        self.status = 'pending'
        self.team_members = []

    def add_team_member(self, member):
        """
        Adds a team member to the project.

        Parameters:
        ----------
        member : str
            Name of the team member to be added.
        """
        if member not in self.team_members:
            self.team_members.append(member)
        else:
            raise ValueError(f"Member '{member}' is already assigned to the project.")

    def update_status(self, new_status):
        """
        Updates the status of the project.

        Parameters:
        ----------
        new_status : str
            New status to set for the project.
        """
        valid_statuses = ['pending', 'in_progress', 'completed']
        if new_status in valid_statuses:
            self.status = new_status
        else:
            raise ValueError(f"Invalid status '{new_status}'. Valid statuses are: {valid_statuses}")

    def __str__(self):
        """
        Returns a string representation of the project.
        """
        return f"Project ID: {self.project_id}, Name: {self.name}, Status: {self.status}, Team: {self.team_members}"


class ProjectManager:
    """
    A class to manage multiple projects.

    Attributes:
    ----------
    projects : dict
        A dictionary to store projects with their IDs as keys.
    """

    def __init__(self):
        """
        Initializes the ProjectManager with an empty project list.
        """
        self.projects = {}

    def create_project(self, project_id, name, description):
        """
        Creates a new project and adds it to the project manager.

        Parameters:
        ----------
        project_id : int
            Unique identifier for the project.
        name : str
            Name of the project.
        description : str
            Detailed description of the project.

        Returns:
        -------
        Project
            The created project instance.
        """
        if project_id in self.projects:
            raise ValueError(f"Project ID '{project_id}' already exists.")
        project = Project(project_id, name, description)
        self.projects[project_id] = project
        return project

    def get_project(self, project_id):
        """
        Retrieves a project by its ID.

        Parameters:
        ----------
        project_id : int
            Unique identifier for the project.

        Returns:
        -------
        Project
            The project instance if found.

        Raises:
        ------
        KeyError
            If the project ID does not exist.
        """
        if project_id not in self.projects:
            raise KeyError(f"Project ID '{project_id}' not found.")
        return self.projects[project_id]

    def list_projects(self):
        """
        Lists all projects managed by the ProjectManager.

        Returns:
        -------
        list
            A list of all project instances.
        """
        return list(self.projects.values())


# Example usage
if __name__ == "__main__":
    try:
        manager = ProjectManager()
        project1 = manager.create_project(1, "Website Redesign", "Redesign the company website.")
        project1.add_team_member("Alice")
        project1.update_status("in_progress")

        print(project1)
        print(manager.list_projects())

    except Exception as e:
        print(f"An error occurred: {e}")
```
