"""
Generated Code Metadata:
========================
Original URL: https://travaux.fr.fo
Prompt: Write a Python script to create a platform that matches customers with artisans for home renovation projects, including features for project estimation and professional profiles.
Generated: DETERMINISTIC_ec56f4b9e13a2c44
Batch ID: 20250622_212142
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

class Artisan:
    """Class representing an artisan with a profile and skills."""
    
    def __init__(self, name: str, skills: List[str], hourly_rate: float):
        self.name = name
        self.skills = skills
        self.hourly_rate = hourly_rate

    def to_dict(self) -> Dict:
        """Convert artisan details to a dictionary."""
        return {
            "name": self.name,
            "skills": self.skills,
            "hourly_rate": self.hourly_rate
        }

class Project:
    """Class representing a home renovation project."""
    
    def __init__(self, description: str, estimated_hours: float):
        self.description = description
        self.estimated_hours = estimated_hours

    def estimate_cost(self, artisan: Artisan) -> float:
        """Estimate the cost of the project based on the artisan's hourly rate."""
        return artisan.hourly_rate * self.estimated_hours

class Platform:
    """Class representing the matching platform for customers and artisans."""
    
    def __init__(self):
        self.artisans: List[Artisan] = []
        self.projects: List[Project] = []

    def add_artisan(self, artisan: Artisan) -> None:
        """Add an artisan to the platform."""
        self.artisans.append(artisan)

    def add_project(self, project: Project) -> None:
        """Add a project to the platform."""
        self.projects.append(project)

    def match_artisans(self, project: Project) -> List[Artisan]:
        """Match artisans based on project requirements."""
        matched_artisans = []
        for artisan in self.artisans:
            if any(skill in artisan.skills for skill in project.description.split()):
                matched_artisans.append(artisan)
        return matched_artisans

    def estimate_project_cost(self, project: Project, artisan: Artisan) -> float:
        """Estimate the cost of a project with a specific artisan."""
        return project.estimate_cost(artisan)

    def save_data(self, filename: str) -> None:
        """Save artisans and projects data to a JSON file."""
        data = {
            "artisans": [artisan.to_dict() for artisan in self.artisans],
            "projects": [project.__dict__ for project in self.projects]
        }
        try:
            with open(filename, 'w') as f:
                json.dump(data, f, indent=4)
        except IOError as e:
            print(f"Error saving data to {filename}: {e}")

    def load_data(self, filename: str) -> None:
        """Load artisans and projects data from a JSON file."""
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                self.artisans = [Artisan(**artisan) for artisan in data.get("artisans", [])]
                self.projects = [Project(**project) for project in data.get("projects", [])]
        except (IOError, json.JSONDecodeError) as e:
            print(f"Error loading data from {filename}: {e}")

# Example usage
if __name__ == "__main__":
    platform = Platform()

    # Adding artisans
    platform.add_artisan(Artisan("Alice", ["plumbing", "tiling"], 50.0))
    platform.add_artisan(Artisan("Bob", ["painting", "drywall"], 40.0))

    # Adding a project
    project = Project("plumbing renovation", 10)
    platform.add_project(project)

    # Matching artisans
    matched_artisans = platform.match_artisans(project)
    for artisan in matched_artisans:
        cost = platform.estimate_project_cost(project, artisan)
        print(f"Matched Artisan: {artisan.name}, Estimated Cost: ${cost:.2f}")

    # Save data to a file
    platform.save_data("platform_data.json")

    # Load data from a file
    platform.load_data("platform_data.json")
```
