"""
Generated Code Metadata:
========================
Original URL: https://mgel.com.br
Prompt: What are some best practices for implementing a sistema de gestão in a construction company like MGEL, and how can they be coded into a software application?
Generated: DETERMINISTIC_e0132afdd9eea63d
Batch ID: 20250622_205348
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# sistema_de_gestao.py

class SistemaDeGestao:
    """
    A class representing a sistema de gestão for a construction company.

    Attributes:
    -----------
    company_name : str
        The name of the construction company.
    projects : list
        A list of projects currently being managed.

    Methods:
    --------
    add_project(project_name, project_manager, start_date, end_date)
        Adds a new project to the sistema de gestão.
    remove_project(project_name)
        Removes a project from the sistema de gestão.
    get_project_status(project_name)
        Retrieves the status of a specific project.
    """

    def __init__(self, company_name):
        """
        Initializes a new SistemaDeGestao instance.

        Args:
        -----
        company_name : str
            The name of the construction company.
        """
        self.company_name = company_name
        self.projects = {}

    def add_project(self, project_name, project_manager, start_date, end_date):
        """
        Adds a new project to the sistema de gestão.

        Args:
        -----
        project_name : str
            The name of the project.
        project_manager : str
            The name of the project manager.
        start_date : str
            The start date of the project (YYYY-MM-DD).
        end_date : str
            The end date of the project (YYYY-MM-DD).

        Raises:
        ------
        ValueError
            If the project name already exists.
        """
        if project_name in self.projects:
            raise ValueError("Project name already exists")

        self.projects[project_name] = {
            "project_manager": project_manager,
            "start_date": start_date,
            "end_date": end_date,
            "status": "In Progress"
        }

    def remove_project(self, project_name):
        """
        Removes a project from the sistema de gestão.

        Args:
        -----
        project_name : str
            The name of the project.

        Raises:
        ------
        ValueError
            If the project name does not exist.
        """
        if project_name not in self.projects:
            raise ValueError("Project name does not exist")

        del self.projects[project_name]

    def get_project_status(self, project_name):
        """
        Retrieves the status of a specific project.

        Args:
        -----
        project_name : str
            The name of the project.

        Returns:
        -------
        str
            The status of the project.

        Raises:
        ------
        ValueError
            If the project name does not exist.
        """
        if project_name not in self.projects:
            raise ValueError("Project name does not exist")

        return self.projects[project_name]["status"]

    def update_project_status(self, project_name, status):
        """
        Updates the status of a specific project.

        Args:
        -----
        project_name : str
            The name of the project.
        status : str
            The new status of the project.

        Raises:
        ------
        ValueError
            If the project name does not exist.
        """
        if project_name not in self.projects:
            raise ValueError("Project name does not exist")

        self.projects[project_name]["status"] = status


def main():
    # Example usage
    sistema_de_gestao = SistemaDeGestao("MGEL")

    try:
        sistema_de_gestao.add_project("Project 1", "John Doe", "2022-01-01", "2022-12-31")
        sistema_de_gestao.add_project("Project 2", "Jane Doe", "2022-06-01", "2023-05-31")

        print(sistema_de_gestao.get_project_status("Project 1"))  # Output: In Progress

        sistema_de_gestao.update_project_status("Project 1", "Completed")
        print(sistema_de_gestao.get_project_status("Project 1"))  # Output: Completed

        sistema_de_gestao.remove_project("Project 2")

        # Attempt to retrieve a non-existent project
        sistema_de_gestao.get_project_status("Project 3")
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
