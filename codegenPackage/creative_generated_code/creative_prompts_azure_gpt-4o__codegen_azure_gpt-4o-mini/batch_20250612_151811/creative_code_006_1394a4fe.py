"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://nicerfoundation.org.ng
Prompt: Develop an algorithm for matching donors with educational projects in underserved communities, reflecting the NICER Foundation's focus on connecting resources to those in need.
Generated: DETERMINISTIC_1394a4fec24dfee0
Batch ID: 20250612_151811
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict, Optional

class Donor:
    def __init__(self, name: str, donation_amount: float, interests: List[str]):
        """
        Initializes a Donor instance.

        :param name: Name of the donor.
        :param donation_amount: Amount the donor is willing to donate.
        :param interests: List of interests related to educational projects.
        """
        self.name = name
        self.donation_amount = donation_amount
        self.interests = interests

class Project:
    def __init__(self, title: str, funding_needed: float, tags: List[str]):
        """
        Initializes a Project instance.

        :param title: Title of the educational project.
        :param funding_needed: Amount required to fund the project.
        :param tags: List of tags categorizing the project.
        """
        self.title = title
        self.funding_needed = funding_needed
        self.tags = tags

class Matcher:
    def __init__(self, donors: List[Donor], projects: List[Project]):
        """
        Initializes a Matcher instance.

        :param donors: List of donors.
        :param projects: List of projects.
        """
        self.donors = donors
        self.projects = projects

    def match_donors_to_projects(self) -> Dict[str, List[str]]:
        """
        Matches donors to educational projects based on interests and available funding.

        :return: A dictionary with donor names as keys and lists of matched project titles as values.
        """
        matches = {}
        for donor in self.donors:
            matches[donor.name] = []
            for project in self.projects:
                # Check if donor's interests overlap with project tags
                if donor.donation_amount >= project.funding_needed and any(tag in donor.interests for tag in project.tags):
                    matches[donor.name].append(project.title)
        return matches

def load_data(donor_file: str, project_file: str) -> Optional[Matcher]:
    """
    Loads donor and project data from JSON files.

    :param donor_file: Path to the JSON file containing donor data.
    :param project_file: Path to the JSON file containing project data.
    :return: A Matcher instance if data is successfully loaded, None otherwise.
    """
    try:
        with open(donor_file, 'r') as df, open(project_file, 'r') as pf:
            donors_data = json.load(df)
            projects_data = json.load(pf)

            donors = [Donor(d['name'], d['donation_amount'], d['interests']) for d in donors_data]
            projects = [Project(p['title'], p['funding_needed'], p['tags']) for p in projects_data]

            return Matcher(donors, projects)

    except (FileNotFoundError, json.JSONDecodeError) as e:
        print(f"Error loading data: {e}")
        return None

def main():
    """
    Main function to execute the donor-project matching algorithm.
    """
    matcher = load_data('donors.json', 'projects.json')
    
    if matcher is None:
        print("Failed to load data.")
        return

    matches = matcher.match_donors_to_projects()
    
    # Output the matches in a readable format
    for donor, projects in matches.items():
        if projects:
            print(f"Donor: {donor} is matched with projects: {', '.join(projects)}")
        else:
            print(f"Donor: {donor} has no matching projects.")

if __name__ == "__main__":
    main()
```
