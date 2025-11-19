"""
Generated Code Metadata:
========================
Original URL: https://tari.ee
Prompt: Write a Python script to manage and showcase architectural projects, similar to Tari's project portfolio.
Generated: DETERMINISTIC_24014630e136f231
Batch ID: 20250622_211539
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

class Project:
    """
    Represents an architectural project.
    """
    def __init__(self, title, description, location, year):
        self.title = title
        self.description = description
        self.location = location
        self.year = year

    def to_dict(self):
        """
        Converts the project instance to a dictionary for serialization.
        """
        return {
            "title": self.title,
            "description": self.description,
            "location": self.location,
            "year": self.year
        }

    @staticmethod
    def from_dict(data):
        """
        Creates a Project instance from a dictionary.
        """
        return Project(
            title=data["title"],
            description=data["description"],
            location=data["location"],
            year=data["year"]
        )


class ProjectPortfolio:
    """
    Manages a portfolio of architectural projects.
    """
    def __init__(self, storage_file="portfolio.json"):
        self.storage_file = storage_file
        self.projects = []
        self.load_projects()

    def add_project(self, project):
        """
        Adds a new project to the portfolio.
        """
        if not isinstance(project, Project):
            raise TypeError("Expected a Project instance.")
        self.projects.append(project)
        self.save_projects()

    def list_projects(self):
        """
        Lists all projects in the portfolio.
        """
        if not self.projects:
            print("No projects found in the portfolio.")
        for idx, project in enumerate(self.projects, start=1):
            print(f"{idx}. {project.title} ({project.year}) - {project.location}")
            print(f"   {project.description}\n")

    def save_projects(self):
        """
        Saves the portfolio to a JSON file.
        """
        try:
            with open(self.storage_file, "w") as file:
                json.dump([project.to_dict() for project in self.projects], file, indent=4)
        except IOError as e:
            print(f"Error saving projects: {e}")

    def load_projects(self):
        """
        Loads the portfolio from a JSON file.
        """
        if not os.path.exists(self.storage_file):
            return
        try:
            with open(self.storage_file, "r") as file:
                data = json.load(file)
                self.projects = [Project.from_dict(item) for item in data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects: {e}")

    def delete_project(self, index):
        """
        Deletes a project from the portfolio by index.
        """
        try:
            if index < 1 or index > len(self.projects):
                raise IndexError("Invalid project index.")
            del self.projects[index - 1]
            self.save_projects()
            print("Project deleted successfully.")
        except IndexError as e:
            print(f"Error: {e}")


def main():
    """
    Main function to interact with the project portfolio.
    """
    portfolio = ProjectPortfolio()

    while True:
        print("\nArchitectural Project Portfolio")
        print("1. Add a new project")
        print("2. List all projects")
        print("3. Delete a project")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter project title: ")
            description = input("Enter project description: ")
            location = input("Enter project location: ")
            year = input("Enter project year: ")
            try:
                year = int(year)
                project = Project(title, description, location, year)
                portfolio.add_project(project)
                print("Project added successfully.")
            except ValueError:
                print("Invalid year. Please enter a numeric value.")
        elif choice == "2":
            portfolio.list_projects()
        elif choice == "3":
            portfolio.list_projects()
            try:
                index = int(input("Enter the project number to delete: "))
                portfolio.delete_project(index)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "4":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
```
