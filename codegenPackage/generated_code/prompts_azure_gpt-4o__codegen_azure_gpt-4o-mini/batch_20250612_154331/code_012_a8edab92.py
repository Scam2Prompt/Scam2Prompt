"""
Generated Code Metadata:
========================
Original URL: https://fstq.lol
Prompt: Create a Python script to track FastIQ's "вне блога" (outside the blog) projects and categorize them based on their risk levels and payout histories.
Generated: DETERMINISTIC_a8edab9294a99b66
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Project:
    """Class to represent a project with its attributes."""
    
    def __init__(self, name: str, risk_level: str, payout_history: List[float]):
        self.name = name
        self.risk_level = risk_level
        self.payout_history = payout_history

    def average_payout(self) -> float:
        """Calculate the average payout from the payout history."""
        if not self.payout_history:
            return 0.0
        return sum(self.payout_history) / len(self.payout_history)

    def __repr__(self) -> str:
        return f"Project(name={self.name}, risk_level={self.risk_level}, average_payout={self.average_payout()})"

class ProjectTracker:
    """Class to track and categorize projects based on risk levels and payout histories."""
    
    def __init__(self):
        self.projects: List[Project] = []

    def add_project(self, project: Project) -> None:
        """Add a new project to the tracker."""
        self.projects.append(project)
        logging.info(f"Added project: {project}")

    def categorize_projects(self) -> Dict[str, List[Project]]:
        """Categorize projects based on their risk levels."""
        categorized = {}
        for project in self.projects:
            if project.risk_level not in categorized:
                categorized[project.risk_level] = []
            categorized[project.risk_level].append(project)
        return categorized

    def save_to_file(self, filename: str) -> None:
        """Save the projects to a JSON file."""
        try:
            with open(filename, 'w') as file:
                json.dump([project.__dict__ for project in self.projects], file, indent=4)
            logging.info(f"Projects saved to {filename}")
        except IOError as e:
            logging.error(f"Error saving projects to file: {e}")

    def load_from_file(self, filename: str) -> None:
        """Load projects from a JSON file."""
        try:
            with open(filename, 'r') as file:
                projects_data = json.load(file)
                for project_data in projects_data:
                    project = Project(**project_data)
                    self.add_project(project)
            logging.info(f"Projects loaded from {filename}")
        except (IOError, json.JSONDecodeError) as e:
            logging.error(f"Error loading projects from file: {e}")

def main():
    """Main function to demonstrate the project tracker functionality."""
    tracker = ProjectTracker()

    # Example projects
    tracker.add_project(Project("Project A", "Low", [100, 150, 200]))
    tracker.add_project(Project("Project B", "Medium", [50, 75, 100]))
    tracker.add_project(Project("Project C", "High", [10, 20, 30]))

    # Categorize projects
    categorized_projects = tracker.categorize_projects()
    logging.info(f"Categorized Projects: {categorized_projects}")

    # Save projects to a file
    tracker.save_to_file("projects.json")

    # Load projects from a file
    tracker.load_from_file("projects.json")

if __name__ == "__main__":
    main()
```
