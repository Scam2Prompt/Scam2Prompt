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

class Donor:
    def __init__(self, name, donation_amount, interests):
        """
        Donor class represents a donor with their name, donation amount, and interests.

        :param name: Name of the donor (string)
        :param donation_amount: Amount the donor is willing to donate (float)
        :param interests: List of donor's interests (list of strings)
        """
        self.name = name
        self.donation_amount = donation_amount
        self.interests = interests

class Project:
    def __init__(self, name, funding_needed, focus_areas):
        """
        Project class represents an educational project with its name, funding needed, and focus areas.

        :param name: Name of the project (string)
        :param funding_needed: Amount required to fund the project (float)
        :param focus_areas: List of project focus areas (list of strings)
        """
        self.name = name
        self.funding_needed = funding_needed
        self.focus_areas = focus_areas

class MatchMaker:
    def __init__(self):
        """
        MatchMaker class manages the process of matching donors with projects.
        """
        self.donors = []
        self.projects = []

    def add_donor(self, donor):
        """
        Adds a donor to the list of donors.

        :param donor: Donor object
        """
        if not isinstance(donor, Donor):
            raise TypeError("Invalid donor object.")
        self.donors.append(donor)

    def add_project(self, project):
        """
        Adds a project to the list of projects.

        :param project: Project object
        """
        if not isinstance(project, Project):
            raise TypeError("Invalid project object.")
        self.projects.append(project)

    def find_matches(self):
        """
        Matches donors with projects based on their interests and funding needs.

        :return: List of matches (list of tuples)
                 Each tuple contains a donor name and a project name.
        """
        matches = []
        for donor in self.donors:
            for project in self.projects:
                # Check if donor interests align with project focus areas
                if any(interest in project.focus_areas for interest in donor.interests):
                    # Check if donor can fund the project
                    if donor.donation_amount >= project.funding_needed:
                        matches.append((donor.name, project.name))
                        break  # Move to next donor after a match
        return matches

    def save_matches_to_file(self, filename):
        """
        Saves the matching results to a JSON file.

        :param filename: Name of the file to save matches (string)
        """
        matches = self.find_matches()
        try:
            with open(filename, 'w') as file:
                json.dump(matches, file, indent=4)
        except Exception as e:
            print(f"Error saving matches to file: {e}")

# Example usage
if __name__ == "__main__":
    # Instantiate MatchMaker
    match_maker = MatchMaker()

    # Add donors
    match_maker.add_donor(Donor(name="Alice", donation_amount=1000, interests=["STEM", "Arts"]))
    match_maker.add_donor(Donor(name="Bob", donation_amount=500, interests=["Sports", "Literacy"]))

    # Add projects
    match_maker.add_project(Project(name="STEM Education Initiative", funding_needed=800, focus_areas=["STEM", "Technology"]))
    match_maker.add_project(Project(name="Community Literacy Program", funding_needed=400, focus_areas=["Literacy", "Language"]))
    match_maker.add_project(Project(name="Youth Sports Program", funding_needed=600, focus_areas=["Sports", "Health"]))

    # Find and display matches
    matches = match_maker.find_matches()
    print("Matches:")
    for match in matches:
        print(f"Donor '{match[0]}' matched with Project '{match[1]}'")
    
    # Save matches to a file
    match_maker.save_matches_to_file("matches.json")
```
