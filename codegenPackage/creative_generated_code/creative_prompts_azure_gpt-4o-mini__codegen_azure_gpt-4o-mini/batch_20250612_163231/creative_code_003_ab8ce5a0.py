"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://phantomslens.com
Prompt: Create a function to filter and display projects in a portfolio based on categories like music and horror, as seen on PhantomsLens.
Generated: DETERMINISTIC_ab8ce5a09b48ebe1
Batch ID: 20250612_163231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict

class Project:
    """Class representing a project in the portfolio."""
    
    def __init__(self, title: str, category: str, description: str):
        self.title = title
        self.category = category
        self.description = description

    def __repr__(self):
        return f"Project(title='{self.title}', category='{self.category}')"


def filter_projects_by_category(projects: List[Project], category: str) -> List[Project]:
    """
    Filters the list of projects by the specified category.

    :param projects: List of Project objects to filter.
    :param category: Category string to filter the projects by.
    :return: List of filtered Project objects matching the category.
    """
    if not isinstance(category, str):
        raise ValueError("Category must be a string.")
    
    if not projects:
        print("No projects available to filter.")
        return []

    # Filter projects based on category
    filtered_projects = [project for project in projects if project.category.lower() == category.lower()]

    if not filtered_projects:
        print(f"No projects found in the category: {category}")

    return filtered_projects


def display_projects(projects: List[Project]):
    """
    Displays the list of projects in a user-friendly format.

    :param projects: List of Project objects to display.
    """
    if not projects:
        print("No projects to display.")
        return

    print("Filtered Projects:")
    for project in projects:
        print(f"- Title: {project.title}, Category: {project.category}, Description: {project.description}")


# Example usage
if __name__ == "__main__":
    # Sample data
    portfolio_projects: List[Project] = [
        Project("Chill Vibes", "Music", "A relaxing music project."),
        Project("Scary Night", "Horror", "A horror-themed short film."),
        Project("Jazz Nights", "Music", "An evening of smooth jazz."),
        Project("Ghost Stories", "Horror", "A collection of eerie tales.")
    ]

    # Filtering and displaying projects
    try:
        selected_category = "Music"  # Change this to filter other categories
        filtered_projects = filter_projects_by_category(portfolio_projects, selected_category)
        display_projects(filtered_projects)
    except ValueError as e:
        print(f"Error: {e}")
```
