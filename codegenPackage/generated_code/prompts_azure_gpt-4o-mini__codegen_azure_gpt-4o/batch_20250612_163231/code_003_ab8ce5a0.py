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
# Import necessary modules
from typing import List, Dict

def filter_projects_by_category(projects: List[Dict[str, str]], category: str) -> List[Dict[str, str]]:
    """
    Filters a list of projects based on the specified category.

    Args:
        projects (List[Dict[str, str]]): A list of projects where each project is represented as a dictionary.
                                         Each dictionary must contain a 'name' and 'category' key.
        category (str): The category to filter projects by (e.g., 'music', 'horror').

    Returns:
        List[Dict[str, str]]: A list of projects that match the specified category.
    """
    # Validate input
    if not isinstance(projects, list):
        raise ValueError("Projects must be a list of dictionaries.")
    if not isinstance(category, str):
        raise ValueError("Category must be a string.")

    # Filter projects based on the category
    filtered_projects = [project for project in projects if project.get('category') == category]

    return filtered_projects


def display_projects(projects: List[Dict[str, str]]) -> None:
    """
    Displays a list of projects in a user-friendly format.

    Args:
        projects (List[Dict[str, str]]): A list of projects where each project is represented as a dictionary.
                                         Each dictionary must contain a 'name' key.
    """
    if not projects:
        print("No projects found.")
        return

    print("Filtered Projects:")
    for project in projects:
        print(f"- {project.get('name', 'Unnamed Project')}")


# Example usage
if __name__ == "__main__":
    # Sample portfolio data
    portfolio = [
        {"name": "Symphony of Shadows", "category": "music"},
        {"name": "Haunted Melodies", "category": "music"},
        {"name": "Phantom's Curse", "category": "horror"},
        {"name": "Echoes of the Abyss", "category": "horror"},
        {"name": "Dreamscape", "category": "fantasy"}
    ]

    try:
        # Filter projects by category
        selected_category = "horror"
        filtered = filter_projects_by_category(portfolio, selected_category)

        # Display filtered projects
        display_projects(filtered)
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
