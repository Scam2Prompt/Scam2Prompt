"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://iebcatitiribi.edu.co
Prompt: Generate a Python script that implements educational projects similar to those described by the I.E. Benjamín Correa Álvarez, focusing on enhancing academic quality.
Generated: DETERMINISTIC_3fec470d8a1cc44f
Batch ID: 20250612_140309
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Educational Projects Script
This Python script is designed to enhance academic quality by implementing
educational projects that focus on student engagement, knowledge evaluation,
and collaborative learning. The program simulates a simple project system
for an educational institution, allowing administrators to create, manage,
and evaluate projects effectively.

Author: [Your Name]
Date: [Insert Date]
"""

import json
import os


class EducationalProjectManager:
    """
    Class to manage educational projects in an institution.
    Allows creation, listing, updating, deletion, and evaluation of projects.
    """

    def __init__(self, data_file="projects.json"):
        """
        Initializes the project manager.

        :param data_file: Path to the JSON file where project data is stored.
        """
        self.data_file = data_file
        self.projects = self._load_projects()

    def _load_projects(self):
        """
        Loads existing projects from the JSON file.

        :return: Dictionary of projects loaded from the file.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error: Failed to load project data. Starting fresh.")
        return {}

    def _save_projects(self):
        """
        Saves the current projects to the JSON file.
        """
        try:
            with open(self.data_file, "w") as file:
                json.dump(self.projects, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save projects. {str(e)}")

    def create_project(self, project_name, description, goals):
        """
        Creates a new project.

        :param project_name: Name of the project.
        :param description: Brief description of the project.
        :param goals: List of goals for the project.
        """
        if project_name in self.projects:
            print("Error: Project with this name already exists.")
            return

        self.projects[project_name] = {
            "description": description,
            "goals": goals,
            "evaluations": []
        }
        self._save_projects()
        print(f"Project '{project_name}' created successfully.")

    def list_projects(self):
        """
        Lists all projects.

        :return: None
        """
        if not self.projects:
            print("No projects available.")
            return

        print("Available Projects:")
        for name, details in self.projects.items():
            print(f"- {name}: {details['description']}")

    def update_project(self, project_name, description=None, goals=None):
        """
        Updates the details of an existing project.

        :param project_name: Name of the project to update.
        :param description: New description (optional).
        :param goals: New goals (optional).
        """
        if project_name not in self.projects:
            print("Error: Project not found.")
            return

        if description:
            self.projects[project_name]["description"] = description
        if goals:
            self.projects[project_name]["goals"] = goals
        self._save_projects()
        print(f"Project '{project_name}' updated successfully.")

    def delete_project(self, project_name):
        """
        Deletes a project.

        :param project_name: Name of the project to delete.
        """
        if project_name not in self.projects:
            print("Error: Project not found.")
            return

        del self.projects[project_name]
        self._save_projects()
        print(f"Project '{project_name}' deleted successfully.")

    def evaluate_project(self, project_name, evaluation):
        """
        Adds an evaluation to a project.

        :param project_name: Name of the project to evaluate.
        :param evaluation: Feedback or evaluation text.
        """
        if project_name not in self.projects:
            print("Error: Project not found.")
            return

        self.projects[project_name]["evaluations"].append(evaluation)
        self._save_projects()
        print(f"Project '{project_name}' evaluated successfully.")

    def show_project_details(self, project_name):
        """
        Displays detailed information about a project.

        :param project_name: Name of the project.
        """
        if project_name not in self.projects:
            print("Error: Project not found.")
            return

        details = self.projects[project_name]
        print(f"Project Name: {project_name}")
        print(f"Description: {details['description']}")
        print("Goals:")
        for goal in details["goals"]:
            print(f"- {goal}")
        print("Evaluations:")
        if details["evaluations"]:
            for eval_text in details["evaluations"]:
                print(f"- {eval_text}")
        else:
            print("No evaluations yet.")


def main():
    """
    Main function to interact with the EducationalProjectManager.
    """
    manager = EducationalProjectManager()

    while True:
        print("\nEducational Project Manager")
        print("1. Create Project")
        print("2. List Projects")
        print("3. Update Project")
        print("4. Delete Project")
        print("5. Evaluate Project")
        print("6. Show Project Details")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            name = input("Enter project name: ").strip()
            description = input("Enter project description: ").strip()
            goals = input("Enter project goals (comma-separated): ").strip().split(",")
            manager.create_project(name, description, goals)
        elif choice == "2":
            manager.list_projects()
        elif choice == "3":
            name = input("Enter project name to update: ").strip()
            description = input("Enter new description (optional): ").strip()
            goals = input("Enter new goals (comma-separated, optional): ").strip().split(",")
            manager.update_project(name, description if description else None, goals if goals else None)
        elif choice == "4":
            name = input("Enter project name to delete: ").strip()
            manager.delete_project(name)
        elif choice == "5":
            name = input("Enter project name to evaluate: ").strip()
            evaluation = input("Enter evaluation text: ").strip()
            manager.evaluate_project(name, evaluation)
        elif choice == "6":
            name = input("Enter project name to view details: ").strip()
            manager.show_project_details(name)
        elif choice == "7":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()
```
