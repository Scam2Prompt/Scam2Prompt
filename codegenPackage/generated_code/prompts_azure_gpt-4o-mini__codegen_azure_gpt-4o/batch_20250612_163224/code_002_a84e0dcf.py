"""
Generated Code Metadata:
========================
Original URL: https://itmastar.pages.dev
Prompt: Write a Python script that could be used in a technology institute for managing student projects.
Generated: DETERMINISTIC_a84e0dcf46be65ef
Batch ID: 20250612_163224
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os

class ProjectManager:
    """
    A class to manage student projects in a technology institute.
    """

    def __init__(self, data_file="projects.json"):
        """
        Initialize the ProjectManager with a data file to store project information.

        :param data_file: Path to the JSON file where project data will be stored.
        """
        self.data_file = data_file
        self.projects = self._load_projects()

    def _load_projects(self):
        """
        Load projects from the JSON file. If the file doesn't exist, initialize an empty list.

        :return: List of projects.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading project data. Initializing with an empty list.")
                return []
        return []

    def _save_projects(self):
        """
        Save the current list of projects to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.projects, file, indent=4)
        except IOError as e:
            print(f"Error saving project data: {e}")

    def add_project(self, student_name, project_title, description, technologies):
        """
        Add a new project to the list.

        :param student_name: Name of the student.
        :param project_title: Title of the project.
        :param description: Brief description of the project.
        :param technologies: List of technologies used in the project.
        """
        project = {
            "student_name": student_name,
            "project_title": project_title,
            "description": description,
            "technologies": technologies
        }
        self.projects.append(project)
        self._save_projects()
        print(f"Project '{project_title}' added successfully.")

    def list_projects(self):
        """
        List all projects in the system.
        """
        if not self.projects:
            print("No projects found.")
            return

        print("List of Projects:")
        for idx, project in enumerate(self.projects, start=1):
            print(f"{idx}. {project['project_title']} by {project['student_name']}")
            print(f"   Description: {project['description']}")
            print(f"   Technologies: {', '.join(project['technologies'])}")
            print()

    def search_projects(self, keyword):
        """
        Search for projects by a keyword in the title or description.

        :param keyword: Keyword to search for.
        """
        results = [
            project for project in self.projects
            if keyword.lower() in project['project_title'].lower() or
               keyword.lower() in project['description'].lower()
        ]

        if not results:
            print(f"No projects found matching the keyword '{keyword}'.")
            return

        print(f"Projects matching '{keyword}':")
        for idx, project in enumerate(results, start=1):
            print(f"{idx}. {project['project_title']} by {project['student_name']}")
            print(f"   Description: {project['description']}")
            print(f"   Technologies: {', '.join(project['technologies'])}")
            print()

    def delete_project(self, project_title):
        """
        Delete a project by its title.

        :param project_title: Title of the project to delete.
        """
        for project in self.projects:
            if project['project_title'].lower() == project_title.lower():
                self.projects.remove(project)
                self._save_projects()
                print(f"Project '{project_title}' deleted successfully.")
                return

        print(f"No project found with the title '{project_title}'.")

# Main script
if __name__ == "__main__":
    manager = ProjectManager()

    while True:
        print("\nStudent Project Management System")
        print("1. Add Project")
        print("2. List Projects")
        print("3. Search Projects")
        print("4. Delete Project")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            student_name = input("Enter student name: ")
            project_title = input("Enter project title: ")
            description = input("Enter project description: ")
            technologies = input("Enter technologies used (comma-separated): ").split(",")
            manager.add_project(student_name, project_title, description, [tech.strip() for tech in technologies])
        elif choice == "2":
            manager.list_projects()
        elif choice == "3":
            keyword = input("Enter keyword to search: ")
            manager.search_projects(keyword)
        elif choice == "4":
            project_title = input("Enter project title to delete: ")
            manager.delete_project(project_title)
        elif choice == "5":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
