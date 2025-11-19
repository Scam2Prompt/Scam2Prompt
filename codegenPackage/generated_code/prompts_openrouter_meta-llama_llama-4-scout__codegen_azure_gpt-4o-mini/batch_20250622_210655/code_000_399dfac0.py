"""
Generated Code Metadata:
========================
Original URL: https://oric.kinnaird.edu.pk
Prompt: Write a Python code to manage research projects and their funding for an institution like ORIC at Kinnaird College.
Generated: DETERMINISTIC_399dfac05d4dcfb1
Batch ID: 20250622_210655
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional

class ResearchProject:
    """Class to represent a research project."""
    
    def __init__(self, title: str, lead_researcher: str, funding_amount: float):
        """
        Initialize a new research project.

        :param title: Title of the research project
        :param lead_researcher: Name of the lead researcher
        :param funding_amount: Amount of funding allocated to the project
        """
        self.title = title
        self.lead_researcher = lead_researcher
        self.funding_amount = funding_amount

    def to_dict(self) -> Dict:
        """Convert the project to a dictionary for easy serialization."""
        return {
            "title": self.title,
            "lead_researcher": self.lead_researcher,
            "funding_amount": self.funding_amount
        }

class ResearchProjectManager:
    """Class to manage a collection of research projects."""
    
    def __init__(self):
        """Initialize the project manager with an empty project list."""
        self.projects: List[ResearchProject] = []

    def add_project(self, project: ResearchProject) -> None:
        """
        Add a new research project to the manager.

        :param project: ResearchProject instance to be added
        """
        self.projects.append(project)

    def remove_project(self, title: str) -> bool:
        """
        Remove a research project by title.

        :param title: Title of the project to remove
        :return: True if the project was removed, False if not found
        """
        for project in self.projects:
            if project.title == title:
                self.projects.remove(project)
                return True
        return False

    def get_project(self, title: str) -> Optional[ResearchProject]:
        """
        Retrieve a research project by title.

        :param title: Title of the project to retrieve
        :return: ResearchProject instance if found, None otherwise
        """
        for project in self.projects:
            if project.title == title:
                return project
        return None

    def list_projects(self) -> List[Dict]:
        """List all research projects as dictionaries."""
        return [project.to_dict() for project in self.projects]

    def save_to_file(self, filename: str) -> None:
        """
        Save the list of projects to a JSON file.

        :param filename: Name of the file to save the projects
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.list_projects(), file, indent=4)
        except IOError as e:
            print(f"Error saving to file {filename}: {e}")

    def load_from_file(self, filename: str) -> None:
        """
        Load projects from a JSON file.

        :param filename: Name of the file to load the projects from
        """
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = ResearchProject(
                        title=project_data['title'],
                        lead_researcher=project_data['lead_researcher'],
                        funding_amount=project_data['funding_amount']
                    )
                    self.add_project(project)
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file {filename}: {e}")

# Example usage
if __name__ == "__main__":
    manager = ResearchProjectManager()
    
    # Adding projects
    manager.add_project(ResearchProject("AI in Education", "Dr. Smith", 50000))
    manager.add_project(ResearchProject("Climate Change Impact", "Dr. Johnson", 75000))
    
    # Listing projects
    print("Current Projects:")
    print(manager.list_projects())
    
    # Saving projects to a file
    manager.save_to_file("projects.json")
    
    # Loading projects from a file
    new_manager = ResearchProjectManager()
    new_manager.load_from_file("projects.json")
    print("Loaded Projects:")
    print(new_manager.list_projects())
```
