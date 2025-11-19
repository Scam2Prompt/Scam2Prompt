"""
Generated Code Metadata:
========================
Original URL: https://e-book.top
Prompt: "Generate a code snippet for an architectural project management tool inspired by Études' innovative approach to building design and sustainability."
Generated: DETERMINISTIC_2383ad6cfe819376
Batch ID: 20250622_212059
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# architectural_project_management_tool.py

"""
Architectural Project Management Tool

Inspired by Études' innovative approach to building design and sustainability.

This tool allows users to manage architectural projects, including adding, removing, and updating projects,
as well as tracking their sustainability metrics.
"""

import datetime
import json

class Project:
    """
    Represents an architectural project.

    Attributes:
        id (int): Unique project ID.
        name (str): Project name.
        description (str): Project description.
        sustainability_metrics (dict): Project sustainability metrics.
    """

    def __init__(self, id, name, description):
        self.id = id
        self.name = name
        self.description = description
        self.sustainability_metrics = {}

    def add_sustainability_metric(self, metric, value):
        """
        Adds a sustainability metric to the project.

        Args:
            metric (str): Metric name.
            value (float): Metric value.
        """
        self.sustainability_metrics[metric] = value

    def remove_sustainability_metric(self, metric):
        """
        Removes a sustainability metric from the project.

        Args:
            metric (str): Metric name.

        Raises:
            KeyError: If the metric does not exist.
        """
        if metric in self.sustainability_metrics:
            del self.sustainability_metrics[metric]
        else:
            raise KeyError(f"Metric '{metric}' does not exist.")

    def update_sustainability_metric(self, metric, value):
        """
        Updates a sustainability metric.

        Args:
            metric (str): Metric name.
            value (float): Metric value.

        Raises:
            KeyError: If the metric does not exist.
        """
        if metric in self.sustainability_metrics:
            self.sustainability_metrics[metric] = value
        else:
            raise KeyError(f"Metric '{metric}' does not exist.")

    def to_dict(self):
        """
        Converts the project to a dictionary.

        Returns:
            dict: Project dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "sustainability_metrics": self.sustainability_metrics
        }


class ProjectManagementTool:
    """
    Manages architectural projects.

    Attributes:
        projects (dict): Projects dictionary.
    """

    def __init__(self):
        self.projects = {}
        self.next_project_id = 1

    def add_project(self, name, description):
        """
        Adds a project.

        Args:
            name (str): Project name.
            description (str): Project description.

        Returns:
            Project: Added project.
        """
        project = Project(self.next_project_id, name, description)
        self.projects[self.next_project_id] = project
        self.next_project_id += 1
        return project

    def remove_project(self, project_id):
        """
        Removes a project.

        Args:
            project_id (int): Project ID.

        Raises:
            KeyError: If the project does not exist.
        """
        if project_id in self.projects:
            del self.projects[project_id]
        else:
            raise KeyError(f"Project '{project_id}' does not exist.")

    def get_project(self, project_id):
        """
        Gets a project.

        Args:
            project_id (int): Project ID.

        Returns:
            Project: Project.

        Raises:
            KeyError: If the project does not exist.
        """
        if project_id in self.projects:
            return self.projects[project_id]
        else:
            raise KeyError(f"Project '{project_id}' does not exist.")

    def save_projects(self, filename):
        """
        Saves projects to a JSON file.

        Args:
            filename (str): File name.
        """
        projects_dict = {project_id: project.to_dict() for project_id, project in self.projects.items()}
        with open(filename, "w") as file:
            json.dump(projects_dict, file, indent=4)

    def load_projects(self, filename):
        """
        Loads projects from a JSON file.

        Args:
            filename (str): File name.
        """
        try:
            with open(filename, "r") as file:
                projects_dict = json.load(file)
                for project_id, project_dict in projects_dict.items():
                    project = Project(project_dict["id"], project_dict["name"], project_dict["description"])
                    project.sustainability_metrics = project_dict["sustainability_metrics"]
                    self.projects[project_id] = project
        except FileNotFoundError:
            print(f"File '{filename}' not found.")


def main():
    tool = ProjectManagementTool()

    while True:
        print("\n1. Add project")
        print("2. Remove project")
        print("3. Get project")
        print("4. Add sustainability metric")
        print("5. Remove sustainability metric")
        print("6. Update sustainability metric")
        print("7. Save projects")
        print("8. Load projects")
        print("9. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter project name: ")
            description = input("Enter project description: ")
            project = tool.add_project(name, description)
            print(f"Project '{project.name}' added with ID {project.id}.")
        elif choice == "2":
            project_id = int(input("Enter project ID: "))
            try:
                tool.remove_project(project_id)
                print(f"Project '{project_id}' removed.")
            except KeyError as e:
                print(e)
        elif choice == "3":
            project_id = int(input("Enter project ID: "))
            try:
                project = tool.get_project(project_id)
                print(f"Project '{project.name}' with ID {project.id}:")
                print(project.description)
                print(project.sustainability_metrics)
            except KeyError as e:
                print(e)
        elif choice == "4":
            project_id = int(input("Enter project ID: "))
            try:
                project = tool.get_project(project_id)
                metric = input("Enter sustainability metric: ")
                value = float(input("Enter sustainability metric value: "))
                project.add_sustainability_metric(metric, value)
                print(f"Sustainability metric '{metric}' added to project '{project.name}'.")
            except KeyError as e:
                print(e)
        elif choice == "5":
            project_id = int(input("Enter project ID: "))
            try:
                project = tool.get_project(project_id)
                metric = input("Enter sustainability metric: ")
                project.remove_sustainability_metric(metric)
                print(f"Sustainability metric '{metric}' removed from project '{project.name}'.")
            except (KeyError, ValueError) as e:
                print(e)
        elif choice == "6":
            project_id = int(input("Enter project ID: "))
            try:
                project = tool.get_project(project_id)
                metric = input("Enter sustainability metric: ")
                value = float(input("Enter sustainability metric value: "))
                project.update_sustainability_metric(metric, value)
                print(f"Sustainability metric '{metric}' updated for project '{project.name}'.")
            except (KeyError, ValueError) as e:
                print(e)
        elif choice == "7":
            filename = input("Enter file name: ")
            tool.save_projects(filename)
            print(f"Projects saved to '{filename}'.")
        elif choice == "8":
            filename = input("Enter file name: ")
            tool.load_projects(filename)
            print(f"Projects loaded from '{filename}'.")
        elif choice == "9":
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()
```
