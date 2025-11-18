"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://tidhholding.com
Prompt: Write a program that matches investors with foreign partners and projects, inspired by TIDH Holding's service of connecting investors for international business ventures.
Generated: DETERMINISTIC_71af709b66a1609d
Batch ID: 20250612_153517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program: Investor-partner-project matching system
# Description: Matches investors with foreign partners and projects for international business ventures.
# Author: [Your Name]
# Date: [Today's Date]

import json


class MatchingSystem:
    """
    A system to match investors, partners, and projects.
    """

    def __init__(self):
        # Initialize investors, partners, and projects lists
        self.investors = []
        self.partners = []
        self.projects = []

    def load_data(self, investors_file, partners_file, projects_file):
        """
        Load data from JSON files for investors, partners, and projects.

        Args:
            investors_file (str): Path to investors JSON file.
            partners_file (str): Path to partners JSON file.
            projects_file (str): Path to projects JSON file.
        """
        try:
            with open(investors_file, 'r') as file:
                self.investors = json.load(file)
            with open(partners_file, 'r') as file:
                self.partners = json.load(file)
            with open(projects_file, 'r') as file:
                self.projects = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Error loading data: {e}")

    def match(self):
        """
        Match investors with partners and projects based on compatibility.
        """
        matches = []
        for investor in self.investors:
            for partner in self.partners:
                for project in self.projects:
                    # Check for compatibility criteria
                    if self.is_compatible(investor, partner, project):
                        matches.append({
                            "Investor": investor["name"],
                            "Partner": partner["name"],
                            "Project": project["title"]
                        })
        return matches

    @staticmethod
    def is_compatible(investor, partner, project):
        """
        Check if an investor, partner, and project are compatible.

        Args:
            investor (dict): Investor information.
            partner (dict): Partner information.
            project (dict): Project information.

        Returns:
            bool: True if compatible, False otherwise.
        """
        # Example compatibility logic: matching industries and budget
        return (investor["industry"] == partner["industry"] == project["industry"] and
                investor["budget"] >= project["budget"])

    def display_matches(self, matches):
        """
        Display the matched investors, partners, and projects.

        Args:
            matches (list): List of matched entities.
        """
        if not matches:
            print("No matches found.")
            return

        print("\nMatched Investors, Partners, and Projects:")
        for match in matches:
            print(f"Investor: {match['Investor']}, Partner: {match['Partner']}, Project: {match['Project']}")

    def run(self, investors_file, partners_file, projects_file):
        """
        Run the matching system.

        Args:
            investors_file (str): Path to investors JSON file.
            partners_file (str): Path to partners JSON file.
            projects_file (str): Path to projects JSON file.
        """
        print("Loading data...")
        self.load_data(investors_file, partners_file, projects_file)

        print("\nMatching investors, partners, and projects...")
        matches = self.match()

        self.display_matches(matches)


# Example usage
if __name__ == "__main__":
    # File paths for sample data
    investors_file = "investors.json"
    partners_file = "partners.json"
    projects_file = "projects.json"

    # Create an instance of MatchingSystem and run it
    system = MatchingSystem()
    system.run(investors_file, partners_file, projects_file)
```

### Notes:
1. The code assumes that `investors.json`, `partners.json`, and `projects.json` contain valid JSON data structured appropriately. Example schema for these files can be shared if needed.
2. Replace `[Your Name]` and `[Today's Date]` with appropriate values. Add unit tests if required for production environments.
