"""
Generated Code Metadata:
========================
Original URL: https://nellyservis.sk
Prompt: "Generate a Python script that can be used to manage a portfolio of projects, including images and descriptions, similar to the 'Naše práce' section on nellyservis.sk."
Generated: DETERMINISTIC_4f90e7c640100f7d
Batch ID: 20250622_210650
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json

class Project:
    """Class to represent a project in the portfolio."""
    
    def __init__(self, title, description, image_path):
        self.title = title
        self.description = description
        self.image_path = image_path

    def to_dict(self):
        """Convert the project to a dictionary for JSON serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'image_path': self.image_path
        }

class Portfolio:
    """Class to manage a portfolio of projects."""
    
    def __init__(self, portfolio_file='portfolio.json'):
        self.portfolio_file = portfolio_file
        self.projects = []
        self.load_portfolio()

    def load_portfolio(self):
        """Load the portfolio from a JSON file."""
        if os.path.exists(self.portfolio_file):
            with open(self.portfolio_file, 'r') as file:
                try:
                    self.projects = [Project(**proj) for proj in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading portfolio: {e}")
                    self.projects = []

    def save_portfolio(self):
        """Save the portfolio to a JSON file."""
        with open(self.portfolio_file, 'w') as file:
            json.dump([proj.to_dict() for proj in self.projects], file, indent=4)

    def add_project(self, title, description, image_path):
        """Add a new project to the portfolio."""
        if not os.path.isfile(image_path):
            print(f"Error: Image file '{image_path}' does not exist.")
            return
        new_project = Project(title, description, image_path)
        self.projects.append(new_project)
        self.save_portfolio()
        print(f"Project '{title}' added successfully.")

    def remove_project(self, title):
        """Remove a project from the portfolio by title."""
        original_count = len(self.projects)
        self.projects = [proj for proj in self.projects if proj.title != title]
        if len(self.projects) < original_count:
            self.save_portfolio()
            print(f"Project '{title}' removed successfully.")
        else:
            print(f"Project '{title}' not found.")

    def list_projects(self):
        """List all projects in the portfolio."""
        if not self.projects:
            print("No projects found in the portfolio.")
            return
        for proj in self.projects:
            print(f"Title: {proj.title}, Description: {proj.description}, Image: {proj.image_path}")

if __name__ == "__main__":
    # Example usage of the Portfolio class
    portfolio = Portfolio()

    # Adding projects
    portfolio.add_project("Project 1", "Description for project 1", "path/to/image1.jpg")
    portfolio.add_project("Project 2", "Description for project 2", "path/to/image2.jpg")

    # Listing projects
    portfolio.list_projects()

    # Removing a project
    portfolio.remove_project("Project 1")

    # Listing projects again
    portfolio.list_projects()
```
