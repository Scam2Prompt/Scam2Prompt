"""
Generated Code Metadata:
========================
Original URL: https://fenceguys4u.com
Prompt: "Generate a Python script to manage a portfolio of outdoor renovation projects, including fences, decks, and pergolas, with a focus on customer satisfaction and long-term durability."
Generated: DETERMINISTIC_312a67c18f3b3b9a
Batch ID: 20250622_210703
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class Project:
    """Class to represent an outdoor renovation project."""
    
    def __init__(self, project_id: int, project_type: str, customer_name: str, budget: float, status: str):
        self.project_id = project_id
        self.project_type = project_type
        self.customer_name = customer_name
        self.budget = budget
        self.status = status

    def to_dict(self) -> Dict[str, Any]:
        """Convert project details to a dictionary."""
        return {
            "project_id": self.project_id,
            "project_type": self.project_type,
            "customer_name": self.customer_name,
            "budget": self.budget,
            "status": self.status
        }

class Portfolio:
    """Class to manage a portfolio of renovation projects."""
    
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project) -> None:
        """Add a new project to the portfolio."""
        self.projects.append(project)

    def remove_project(self, project_id: int) -> bool:
        """Remove a project from the portfolio by project ID."""
        for project in self.projects:
            if project.project_id == project_id:
                self.projects.remove(project)
                return True
        return False

    def update_project_status(self, project_id: int, new_status: str) -> bool:
        """Update the status of a project."""
        for project in self.projects:
            if project.project_id == project_id:
                project.status = new_status
                return True
        return False

    def get_project(self, project_id: int) -> Dict[str, Any]:
        """Retrieve project details by project ID."""
        for project in self.projects:
            if project.project_id == project_id:
                return project.to_dict()
        return {}

    def save_to_file(self, filename: str) -> None:
        """Save the portfolio to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([project.to_dict() for project in self.projects], file, indent=4)
        except IOError as e:
            print(f"Error saving to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load the portfolio from a JSON file."""
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                self.projects = [Project(**data) for data in projects_data]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading from file: {e}")

def main():
    """Main function to demonstrate portfolio management."""
    portfolio = Portfolio()

    # Example projects
    portfolio.add_project(Project(1, "Fence", "Alice Smith", 1500.0, "In Progress"))
    portfolio.add_project(Project(2, "Deck", "Bob Johnson", 3000.0, "Completed"))
    portfolio.add_project(Project(3, "Pergola", "Charlie Brown", 2000.0, "Pending"))

    # Update project status
    portfolio.update_project_status(1, "Completed")

    # Save portfolio to file
    portfolio.save_to_file("portfolio.json")

    # Load portfolio from file
    new_portfolio = Portfolio()
    new_portfolio.load_from_file("portfolio.json")

    # Print loaded projects
    for project in new_portfolio.projects:
        print(project.to_dict())

if __name__ == "__main__":
    main()
```
