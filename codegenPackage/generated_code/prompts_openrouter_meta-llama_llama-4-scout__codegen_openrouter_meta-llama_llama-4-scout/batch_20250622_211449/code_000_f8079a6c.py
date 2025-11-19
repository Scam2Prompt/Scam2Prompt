"""
Generated Code Metadata:
========================
Original URL: https://morpho-foundation.eu
Prompt: Write a Python script to manage and track the health projects supported by the Morpho Foundation, including project details, location, and impact metrics.
Generated: DETERMINISTIC_f8079a6cfea54fd2
Batch ID: 20250622_211449
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# project_tracker.py

class Project:
    """Represents a health project supported by the Morpho Foundation."""

    def __init__(self, id, name, location, description, impact_metrics=None):
        """
        Initializes a Project instance.

        Args:
            id (int): Unique project identifier.
            name (str): Project name.
            location (str): Project location.
            description (str): Project description.
            impact_metrics (dict, optional): Project impact metrics. Defaults to None.
        """
        self.id = id
        self.name = name
        self.location = location
        self.description = description
        self.impact_metrics = impact_metrics if impact_metrics else {}

    def update_impact_metrics(self, metrics):
        """
        Updates project impact metrics.

        Args:
            metrics (dict): New impact metrics.
        """
        self.impact_metrics = metrics

    def __str__(self):
        return f"Project {self.id}: {self.name}"


class ProjectTracker:
    """Manages and tracks health projects supported by the Morpho Foundation."""

    def __init__(self):
        """Initializes a ProjectTracker instance."""
        self.projects = {}

    def add_project(self, project):
        """
        Adds a project to the tracker.

        Args:
            project (Project): Project to add.

        Raises:
            ValueError: If a project with the same ID already exists.
        """
        if project.id in self.projects:
            raise ValueError("Project with the same ID already exists")
        self.projects[project.id] = project

    def get_project(self, project_id):
        """
        Retrieves a project by ID.

        Args:
            project_id (int): Project ID.

        Returns:
            Project: Project instance or None if not found.
        """
        return self.projects.get(project_id)

    def update_project(self, project_id, project):
        """
        Updates a project.

        Args:
            project_id (int): Project ID.
            project (Project): Updated project.

        Raises:
            ValueError: If the project ID does not exist.
        """
        if project_id not in self.projects:
            raise ValueError("Project ID does not exist")
        self.projects[project_id] = project

    def remove_project(self, project_id):
        """
        Removes a project.

        Args:
            project_id (int): Project ID.

        Raises:
            ValueError: If the project ID does not exist.
        """
        if project_id not in self.projects:
            raise ValueError("Project ID does not exist")
        del self.projects[project_id]

    def list_projects(self):
        """
        Lists all projects.

        Returns:
            list: List of Project instances.
        """
        return list(self.projects.values())


def main():
    tracker = ProjectTracker()

    while True:
        print("\n1. Add Project")
        print("2. Get Project")
        print("3. Update Project")
        print("4. Remove Project")
        print("5. List Projects")
        print("6. Exit")

        choice = input("Choose an option: ")

        try:
            if choice == "1":
                id = int(input("Enter project ID: "))
                name = input("Enter project name: ")
                location = input("Enter project location: ")
                description = input("Enter project description: ")
                project = Project(id, name, location, description)
                tracker.add_project(project)
                print(f"Project {id} added successfully")

            elif choice == "2":
                project_id = int(input("Enter project ID: "))
                project = tracker.get_project(project_id)
                if project:
                    print(f"Project {project.id}: {project.name}")
                    print(f"Location: {project.location}")
                    print(f"Description: {project.description}")
                    print(f"Impact Metrics: {project.impact_metrics}")
                else:
                    print("Project not found")

            elif choice == "3":
                project_id = int(input("Enter project ID: "))
                name = input("Enter new project name: ")
                location = input("Enter new project location: ")
                description = input("Enter new project description: ")
                project = Project(project_id, name, location, description)
                tracker.update_project(project_id, project)
                print(f"Project {project_id} updated successfully")

            elif choice == "4":
                project_id = int(input("Enter project ID: "))
                tracker.remove_project(project_id)
                print(f"Project {project_id} removed successfully")

            elif choice == "5":
                projects = tracker.list_projects()
                for project in projects:
                    print(project)

            elif choice == "6":
                break

            else:
                print("Invalid option. Please choose a valid option.")

        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
