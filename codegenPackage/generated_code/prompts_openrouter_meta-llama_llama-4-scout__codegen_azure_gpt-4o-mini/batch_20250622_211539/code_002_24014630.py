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
    """Class to represent an architectural project."""
    
    def __init__(self, title, description, year, images):
        """
        Initialize a new project.

        Args:
            title (str): The title of the project.
            description (str): A brief description of the project.
            year (int): The year the project was completed.
            images (list): A list of image file paths associated with the project.
        """
        self.title = title
        self.description = description
        self.year = year
        self.images = images

    def to_dict(self):
        """Convert the project to a dictionary for JSON serialization."""
        return {
            'title': self.title,
            'description': self.description,
            'year': self.year,
            'images': self.images
        }

class Portfolio:
    """Class to manage a collection of architectural projects."""
    
    def __init__(self, filename='portfolio.json'):
        """
        Initialize the portfolio.

        Args:
            filename (str): The filename for storing the portfolio data.
        """
        self.filename = filename
        self.projects = []
        self.load_portfolio()

    def load_portfolio(self):
        """Load projects from a JSON file."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                try:
                    self.projects = [Project(**proj) for proj in json.load(file)]
                except json.JSONDecodeError as e:
                    print(f"Error loading portfolio: {e}")
                    self.projects = []
        else:
            print("Portfolio file not found. Starting with an empty portfolio.")

    def save_portfolio(self):
        """Save the current projects to a JSON file."""
        with open(self.filename, 'w') as file:
            json.dump([proj.to_dict() for proj in self.projects], file, indent=4)

    def add_project(self, title, description, year, images):
        """Add a new project to the portfolio."""
        new_project = Project(title, description, year, images)
        self.projects.append(new_project)
        self.save_portfolio()

    def display_projects(self):
        """Display all projects in the portfolio."""
        if not self.projects:
            print("No projects to display.")
            return
        
        for project in self.projects:
            print(f"Title: {project.title}")
            print(f"Description: {project.description}")
            print(f"Year: {project.year}")
            print(f"Images: {', '.join(project.images)}")
            print("-" * 40)

def main():
    """Main function to run the portfolio manager."""
    portfolio = Portfolio()

    # Example usage
    portfolio.add_project(
        title="Modern House",
        description="A modern house with sustainable features.",
        year=2023,
        images=["image1.jpg", "image2.jpg"]
    )

    portfolio.display_projects()

if __name__ == "__main__":
    main()
```
