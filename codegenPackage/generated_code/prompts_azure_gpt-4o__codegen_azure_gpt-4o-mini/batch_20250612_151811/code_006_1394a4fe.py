"""
Generated Code Metadata:
========================
Original URL: https://nicerfoundation.org.ng
Prompt: Develop an algorithm for matching donors with educational projects in underserved communities, reflecting the NICER Foundation's focus on connecting resources to those in need.
Generated: DETERMINISTIC_1394a4fec24dfee0
Batch ID: 20250612_151811
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

class Donor:
    def __init__(self, name: str, interests: List[str], donation_amount: float):
        self.name = name
        self.interests = interests
        self.donation_amount = donation_amount

class Project:
    def __init__(self, title: str, description: str, needs: List[str], required_amount: float):
        self.title = title
        self.description = description
        self.needs = needs
        self.required_amount = required_amount

class Match:
    def __init__(self, donor: Donor, project: Project):
        self.donor = donor
        self.project = project

def load_data(donor_file: str, project_file: str) -> (List[Donor], List[Project]):
    """Load donor and project data from JSON files."""
    try:
        with open(donor_file, 'r') as df:
            donors = [Donor(**donor) for donor in json.load(df)]
        
        with open(project_file, 'r') as pf:
            projects = [Project(**project) for project in json.load(pf)]
        
        return donors, projects
    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return [], []

def match_donors_to_projects(donors: List[Donor], projects: List[Project]) -> List[Match]:
    """Match donors to projects based on interests and donation capacity."""
    matches = []
    
    for donor in donors:
        for project in projects:
            # Check if donor's interests align with project needs and if they can cover the required amount
            if set(donor.interests).intersection(set(project.needs)) and donor.donation_amount >= project.required_amount:
                matches.append(Match(donor, project))
    
    return matches

def display_matches(matches: List[Match]) -> None:
    """Display matched donors and projects."""
    if not matches:
        print("No matches found.")
        return
    
    for match in matches:
        print(f"Donor: {match.donor.name} | Project: {match.project.title} | Donation Amount: ${match.donor.donation_amount}")

def main(donor_file: str, project_file: str) -> None:
    """Main function to execute the matching algorithm."""
    donors, projects = load_data(donor_file, project_file)
    
    if not donors or not projects:
        print("No donors or projects available for matching.")
        return
    
    matches = match_donors_to_projects(donors, projects)
    display_matches(matches)

if __name__ == "__main__":
    # Example usage with file paths
    main('donors.json', 'projects.json')
```

### Note:
- Ensure that the `donors.json` and `projects.json` files are structured correctly to match the expected input for the `Donor` and `Project` classes.
- The code includes error handling for file loading and JSON decoding, ensuring robustness in production environments.
