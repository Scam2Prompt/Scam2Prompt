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
# Import necessary modules
from typing import List, Dict

def filter_projects_by_category(projects: List[Dict[str, str]], category: str) -> List[Dict[str, str]]:
    """
    Filters a list of projects by a given category.

    Parameters:
        projects (List[Dict[str, str]]): A list of project dictionaries where each dictionary contains project details.
            Example: [{'title': 'Project 1', 'category': 'Music'}, {'title': 'Project 2', 'category': 'Horror'}]
        category (str): The category to filter projects by (e.g., 'Music', 'Horror').

    Returns:
        List[Dict[str, str]]: A list of filtered projects matching the given category.
    """
    if not isinstance(projects, list):
        raise ValueError("The 'projects' parameter must be a list.")

    if not isinstance(category, str):
        raise ValueError("The 'category' parameter must be a string.")

    # Filter projects based on the category
    filtered_projects = [project for project in projects if project.get('category') == category]

    return filtered_projects


# Example usage
if __name__ == "__main__":
    try:
        # Sample portfolio data
        portfolio_projects = [
            {"title": "Project A", "category": "Music"},
            {"title": "Project B", "category": "Horror"},
            {"title": "Project C", "category": "Music"},
            {"title": "Project D", "category": "Photography"}
        ]

        # Category to filter by
        selected_category = "Music"

        # Get filtered projects
        filtered_projects = filter_projects_by_category(portfolio_projects, selected_category)

        # Display filtered projects
        print(f"Projects in category '{selected_category}':")
        for project in filtered_projects:
            print(f"- {project['title']}")

    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
