"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://neotokyo.pages.dev
Prompt: Generate code to display and manage citizen-run projects within the Neo Tokyo community, highlighting contributions to the gaming/metaverse space as described on the webpage.
Generated: DETERMINISTIC_9a84f34a264001c7
Batch ID: 20250612_152410
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import json

# Define a class to represent a citizen-run project
class CitizenProject:
    def __init__(self, project_id, name, description, contributors, category):
        """
        Initializes a CitizenProject instance.

        Args:
            project_id (int): Unique identifier for the project.
            name (str): Name of the project.
            description (str): Description of the project.
            contributors (list): List of contributors to the project.
            category (str): Category of the project (e.g., Gaming/Metaverse).
        """
        self.project_id = project_id
        self.name = name
        self.description = description
        self.contributors = contributors
        self.category = category

    def __str__(self):
        """
        Returns a string representation of the project.
        """
        return f"Project ID: {self.project_id}, Name: {self.name}, Category: {self.category}, Contributors: {', '.join(self.contributors)}"

# Define a class to manage the Neo Tokyo community projects
class NeoTokyoCommunity:
    def __init__(self):
        """
        Initializes the Neo Tokyo Community Project Manager.
        """
        self.projects = []

    def add_project(self, project):
        """
        Adds a new project to the community.

        Args:
            project (CitizenProject): The project to add.
        """
        if not isinstance(project, CitizenProject):
            raise TypeError("Expected an instance of CitizenProject.")
        self.projects.append(project)

    def list_projects(self, category=None):
        """
        Lists all projects or filters by category.

        Args:
            category (str, optional): Category to filter projects by. Defaults to None.
        
        Returns:
            list: Filtered list of projects if category is provided; otherwise, all projects.
        """
        if category:
            return [project for project in self.projects if project.category.lower() == category.lower()]
        return self.projects

    def display_projects(self, category=None):
        """
        Displays the projects in a readable format.

        Args:
            category (str, optional): Category to filter projects by. Defaults to None.
        """
        filtered_projects = self.list_projects(category)
        if not filtered_projects:
            print("No projects found.")
            return
        for project in filtered_projects:
            print(project)

    def save_projects_to_file(self, file_path):
        """
        Saves all projects to a JSON file.

        Args:
            file_path (str): Path to the file where projects will be saved.
        """
        try:
            projects_data = [
                {
                    "project_id": project.project_id,
                    "name": project.name,
                    "description": project.description,
                    "contributors": project.contributors,
                    "category": project.category,
                }
                for project in self.projects
            ]
            with open(file_path, 'w') as file:
                json.dump(projects_data, file, indent=4)
            print(f"Projects successfully saved to {file_path}.")
        except IOError as e:
            print(f"Error saving projects to file: {str(e)}")

    def load_projects_from_file(self, file_path):
        """
        Loads projects from a JSON file.

        Args:
            file_path (str): Path to the file from which projects will be loaded.
        """
        try:
            with open(file_path, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = CitizenProject(
                        project_id=project_data["project_id"],
                        name=project_data["name"],
                        description=project_data["description"],
                        contributors=project_data["contributors"],
                        category=project_data["category"],
                    )
                    self.add_project(project)
            print(f"Projects successfully loaded from {file_path}.")
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading projects from file: {str(e)}")

# Example usage:
if __name__ == "__main__":
    # Initialize the community manager
    community_manager = NeoTokyoCommunity()

    # Create some projects
    project1 = CitizenProject(
        project_id=1,
        name="Neo Tokyo VR Hub",
        description="A virtual reality hub for citizens to interact.",
        contributors=["Alice", "Bob"],
        category="Metaverse"
    )
    project2 = CitizenProject(
        project_id=2,
        name="Gaming DAO",
        description="A decentralized autonomous organization focused on game funding.",
        contributors=["Charlie", "Dave"],
        category="Gaming"
    )

    # Add projects to the community
    community_manager.add_project(project1)
    community_manager.add_project(project2)

    # Display all projects
    print("All Projects:")
    community_manager.display_projects()

    # Display projects filtered by category
    print("\nProjects in Gaming category:")
    community_manager.display_projects(category="Gaming")

    # Save projects to a file
    community_manager.save_projects_to_file("projects.json")

    # Load projects from a file
    community_manager.load_projects_from_file("projects.json")
```
