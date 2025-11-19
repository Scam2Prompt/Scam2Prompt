"""
Generated Code Metadata:
========================
Original URL: https://mycoastalroofing.com
Prompt: Write a Python script to manage roofing projects for a contractor with multiple locations, including tracking new roofs, re-roofs, and commercial roofs.
Generated: DETERMINISTIC_51fd76c8137575a8
Batch ID: 20250622_210443
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

class RoofingProjectManager:
    """
    A class to manage roofing projects for a contractor with multiple locations.
    Tracks new roofs, re-roofs, and commercial roofs.
    """

    def __init__(self, data_file="projects.json"):
        """
        Initializes the RoofingProjectManager with a data file.
        :param data_file: Path to the JSON file where project data is stored.
        """
        self.data_file = data_file
        self.projects = self._load_projects()

    def _load_projects(self):
        """
        Loads projects from the JSON file. If the file doesn't exist, initializes an empty list.
        :return: List of projects.
        """
        if os.path.exists(self.data_file):
            try:
                with open(self.data_file, 'r') as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Error loading project data. Starting with an empty list.")
                return []
        return []

    def _save_projects(self):
        """
        Saves the current list of projects to the JSON file.
        """
        try:
            with open(self.data_file, 'w') as file:
                json.dump(self.projects, file, indent=4)
        except IOError as e:
            print(f"Error saving project data: {e}")

    def add_project(self, location, project_type, description):
        """
        Adds a new project to the list.
        :param location: The location of the project.
        :param project_type: The type of roofing project (e.g., 'new roof', 're-roof', 'commercial roof').
        :param description: A brief description of the project.
        """
        if project_type not in ['new roof', 're-roof', 'commercial roof']:
            print("Invalid project type. Must be 'new roof', 're-roof', or 'commercial roof'.")
            return

        project = {
            "location": location,
            "type": project_type,
            "description": description
        }
        self.projects.append(project)
        self._save_projects()
        print("Project added successfully.")

    def list_projects(self):
        """
        Lists all projects currently being tracked.
        """
        if not self.projects:
            print("No projects found.")
            return

        print("Current Projects:")
        for idx, project in enumerate(self.projects, start=1):
            print(f"{idx}. Location: {project['location']}, Type: {project['type']}, Description: {project['description']}")

    def delete_project(self, index):
        """
        Deletes a project by its index in the list.
        :param index: The index of the project to delete (1-based).
        """
        try:
            index = int(index) - 1
            if 0 <= index < len(self.projects):
                deleted_project = self.projects.pop(index)
                self._save_projects()
                print(f"Deleted project: {deleted_project}")
            else:
                print("Invalid index. No project deleted.")
        except ValueError:
            print("Invalid input. Please provide a numeric index.")

    def search_projects(self, keyword):
        """
        Searches for projects containing a specific keyword in their description.
        :param keyword: The keyword to search for.
        """
        results = [project for project in self.projects if keyword.lower() in project['description'].lower()]
        if results:
            print("Search Results:")
            for idx, project in enumerate(results, start=1):
                print(f"{idx}. Location: {project['location']}, Type: {project['type']}, Description: {project['description']}")
        else:
            print("No projects found matching the keyword.")

# Main script
if __name__ == "__main__":
    manager = RoofingProjectManager()

    while True:
        print("\nRoofing Project Manager")
        print("1. Add Project")
        print("2. List Projects")
        print("3. Delete Project")
        print("4. Search Projects")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            location = input("Enter project location: ")
            project_type = input("Enter project type (new roof, re-roof, commercial roof): ")
            description = input("Enter project description: ")
            manager.add_project(location, project_type, description)
        elif choice == "2":
            manager.list_projects()
        elif choice == "3":
            index = input("Enter the index of the project to delete: ")
            manager.delete_project(index)
        elif choice == "4":
            keyword = input("Enter keyword to search for: ")
            manager.search_projects(keyword)
        elif choice == "5":
            print("Exiting. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
```
