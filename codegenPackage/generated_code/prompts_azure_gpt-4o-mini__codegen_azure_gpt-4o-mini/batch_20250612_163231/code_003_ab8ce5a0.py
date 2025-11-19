"""
Generated Code Metadata:
========================
Original URL: https://phantomslens.com
Prompt: Create a function to filter and display projects in a portfolio based on categories like music and horror, as seen on PhantomsLens.
Generated: DETERMINISTIC_ab8ce5a09b48ebe1
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
from typing import List, Dict

class Project:
    """Class representing a project in the portfolio."""
    
    def __init__(self, title: str, category: str):
        """
        Initialize a new project.

        :param title: The title of the project.
        :param category: The category of the project (e.g., music, horror).
        """
        self.title = title
        self.category = category

    def __repr__(self):
        """Return a string representation of the project."""
        return f"Project(title='{self.title}', category='{self.category}')"


def filter_projects_by_category(projects: List[Project], category: str) -> List[Project]:
    """
    Filter projects based on the specified category.

    :param projects: A list of Project objects to filter.
    :param category: The category to filter projects by.
    :return: A list of projects that match the specified category.
    """
    if not isinstance(projects, list):
        raise ValueError("The 'projects' parameter must be a list of Project objects.")
    
    if not isinstance(category, str):
        raise ValueError("The 'category' parameter must be a string.")

    filtered_projects = [project for project in projects if project.category.lower() == category.lower()]
    
    return filtered_projects


def display_projects(projects: List[Project]) -> None:
    """
    Display the list of projects.

    :param projects: A list of Project objects to display.
    """
    if not projects:
        print("No projects to display.")
        return

    print("Projects:")
    for project in projects:
        print(f"- {project.title} (Category: {project.category})")


# Example usage
if __name__ == "__main__":
    # Sample projects
    portfolio_projects = [
        Project("Chilling Tunes", "Music"),
        Project("Horror Nights", "Horror"),
        Project("Epic Soundtrack", "Music"),
        Project("Scary Stories", "Horror"),
        Project("Nature Documentary", "Documentary")
    ]

    # Filter and display music projects
    try:
        music_projects = filter_projects_by_category(portfolio_projects, "Music")
        display_projects(music_projects)

        # Filter and display horror projects
        horror_projects = filter_projects_by_category(portfolio_projects, "Horror")
        display_projects(horror_projects)

    except ValueError as e:
        print(f"Error: {e}")
```
