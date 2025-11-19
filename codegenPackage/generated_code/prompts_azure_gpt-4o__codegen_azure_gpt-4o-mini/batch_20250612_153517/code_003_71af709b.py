"""
Generated Code Metadata:
========================
Original URL: https://tidhholding.com
Prompt: Write a program that matches investors with foreign partners and projects, inspired by TIDH Holding's service of connecting investors for international business ventures.
Generated: DETERMINISTIC_71af709b66a1609d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any, Optional

class Investor:
    """Class representing an investor."""
    
    def __init__(self, name: str, investment_amount: float, preferred_industries: List[str]):
        self.name = name
        self.investment_amount = investment_amount
        self.preferred_industries = preferred_industries

    def __repr__(self):
        return f"Investor(name={self.name}, investment_amount={self.investment_amount}, preferred_industries={self.preferred_industries})"


class Project:
    """Class representing a project."""
    
    def __init__(self, title: str, required_amount: float, industry: str):
        self.title = title
        self.required_amount = required_amount
        self.industry = industry

    def __repr__(self):
        return f"Project(title={self.title}, required_amount={self.required_amount}, industry={self.industry})"


class Matchmaker:
    """Class to match investors with projects."""
    
    def __init__(self):
        self.investors: List[Investor] = []
        self.projects: List[Project] = []

    def add_investor(self, investor: Investor) -> None:
        """Add an investor to the matchmaker."""
        self.investors.append(investor)

    def add_project(self, project: Project) -> None:
        """Add a project to the matchmaker."""
        self.projects.append(project)

    def find_matches(self) -> Dict[str, List[str]]:
        """Find matches between investors and projects based on preferences and requirements."""
        matches = {}
        for investor in self.investors:
            matches[investor.name] = []
            for project in self.projects:
                if (investor.investment_amount >= project.required_amount and
                        project.industry in investor.preferred_industries):
                    matches[investor.name].append(project.title)
        return matches


def load_data(file_path: str) -> Optional[Dict[str, Any]]:
    """Load data from a JSON file."""
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return None


def main():
    """Main function to run the investor-project matching program."""
    # Load data from JSON files
    data = load_data('data.json')
    if data is None:
        return

    matchmaker = Matchmaker()

    # Add investors
    for investor_data in data.get('investors', []):
        investor = Investor(
            name=investor_data['name'],
            investment_amount=investor_data['investment_amount'],
            preferred_industries=investor_data['preferred_industries']
        )
        matchmaker.add_investor(investor)

    # Add projects
    for project_data in data.get('projects', []):
        project = Project(
            title=project_data['title'],
            required_amount=project_data['required_amount'],
            industry=project_data['industry']
        )
        matchmaker.add_project(project)

    # Find and print matches
    matches = matchmaker.find_matches()
    for investor, matched_projects in matches.items():
        print(f"Investor: {investor} -> Matched Projects: {matched_projects}")


if __name__ == "__main__":
    main()
```

**Note:** The program expects a JSON file named `data.json` with the following structure:

```json
{
    "investors": [
        {
            "name": "Investor A",
            "investment_amount": 500000,
            "preferred_industries": ["Technology", "Healthcare"]
        },
        {
            "name": "Investor B",
            "investment_amount": 300000,
            "preferred_industries": ["Real Estate"]
        }
    ],
    "projects": [
        {
            "title": "Tech Startup",
            "required_amount": 400000,
            "industry": "Technology"
        },
        {
            "title": "Healthcare Initiative",
            "required_amount": 200000,
            "industry": "Healthcare"
        },
        {
            "title": "Real Estate Development",
            "required_amount": 250000,
            "industry": "Real Estate"
        }
    ]
}
```
