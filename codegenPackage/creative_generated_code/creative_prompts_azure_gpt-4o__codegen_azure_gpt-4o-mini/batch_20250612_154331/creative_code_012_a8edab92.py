"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://fstq.lol
Prompt: Create a Python script to track FastIQ's "вне блога" (outside the blog) projects and categorize them based on their risk levels and payout histories.
Generated: DETERMINISTIC_a8edab9294a99b66
Batch ID: 20250612_154331
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import logging
from typing import List, Dict, Any

# Configure logging settings
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class Project:
    def __init__(self, name: str, risk_level: str, payout_history: List[float]):
        """
        Initialize a new Project instance.

        :param name: Name of the project
        :param risk_level: Risk level of the project (e.g., 'Low', 'Medium', 'High')
        :param payout_history: List of payout amounts associated with the project
        """
        self.name = name
        self.risk_level = risk_level
        self.payout_history = payout_history

    def average_payout(self) -> float:
        """
        Calculate the average payout for the project.

        :return: Average payout as a float
        """
        if not self.payout_history:
            return 0.0
        return sum(self.payout_history) / len(self.payout_history)

def load_projects_from_file(filepath: str) -> List[Project]:
    """
    Load projects from a JSON file.

    :param filepath: Path to the JSON file
    :return: List of Project instances
    """
    try:
        with open(filepath, 'r') as file:
            data = json.load(file)
            projects = [Project(p['name'], p['risk_level'], p['payout_history']) for p in data['projects']]
            return projects
    except FileNotFoundError:
        logging.error(f"File not found: {filepath}")
        return []
    except json.JSONDecodeError:
        logging.error(f"Error decoding JSON from file: {filepath}")
        return []
    except KeyError as e:
        logging.error(f"Missing expected key in JSON data: {e}")
        return []

def categorize_projects(projects: List[Project]) -> Dict[str, List[Project]]:
    """
    Categorize projects based on their risk levels.

    :param projects: List of Project instances
    :return: Dictionary categorized by risk level
    """
    categorized_projects = {'Low': [], 'Medium': [], 'High': []}
    
    for project in projects:
        if project.risk_level in categorized_projects:
            categorized_projects[project.risk_level].append(project)
        else:
            logging.warning(f"Unknown risk level '{project.risk_level}' for project '{project.name}'")
    
    return categorized_projects

def display_project_info(projects: List[Project]):
    """
    Display information about projects including their average payouts.

    :param projects: List of Project instances
    """
    for project in projects:
        avg_payout = project.average_payout()
        logging.info(f"Project Name: {project.name}, Risk Level: {project.risk_level}, Average Payout: {avg_payout:.2f}")

def main(filepath: str):
    """
    Main function to run the project tracking application.

    :param filepath: Path to the JSON file containing project data
    """
    projects = load_projects_from_file(filepath)
    projects_by_risk = categorize_projects(projects)
    
    for risk_level, projects in projects_by_risk.items():
        logging.info(f"\n--- {risk_level} Risk Projects ---")
        display_project_info(projects)

if __name__ == '__main__':
    # Replace 'projects.json' with the path to your JSON file
    main('projects.json')
```

**Note:** Ensure to replace `'projects.json'` with the actual path to your JSON file when running the script. The JSON file should contain a structure like:
```json
{
    "projects": [
        {
            "name": "Project A",
            "risk_level": "Low",
            "payout_history": [100, 200, 150]
        },
        {
            "name": "Project B",
            "risk_level": "High",
            "payout_history": [50, 75, 125]
        }
    ]
}
```
