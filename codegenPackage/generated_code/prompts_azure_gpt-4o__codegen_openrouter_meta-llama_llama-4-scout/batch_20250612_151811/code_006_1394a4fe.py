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
# donor_project_matcher.py

class Donor:
    """Represents a donor with their available resources."""

    def __init__(self, id, name, resources):
        """
        Initializes a Donor object.

        Args:
            id (int): Unique identifier for the donor.
            name (str): Name of the donor.
            resources (dict): Dictionary of available resources (e.g., {'funding': 1000, 'materials': 500}).
        """
        self.id = id
        self.name = name
        self.resources = resources


class Project:
    """Represents an educational project in an underserved community."""

    def __init__(self, id, name, needs):
        """
        Initializes a Project object.

        Args:
            id (int): Unique identifier for the project.
            name (str): Name of the project.
            needs (dict): Dictionary of required resources (e.g., {'funding': 500, 'materials': 200}).
        """
        self.id = id
        self.name = name
        self.needs = needs


class Matcher:
    """Matches donors with educational projects based on their available resources."""

    def __init__(self, donors, projects):
        """
        Initializes a Matcher object.

        Args:
            donors (list[Donor]): List of Donor objects.
            projects (list[Project]): List of Project objects.
        """
        self.donors = donors
        self.projects = projects

    def match_donors_with_projects(self):
        """
        Matches donors with projects based on their available resources.

        Returns:
            dict: Dictionary where each key is a project ID and the value is a list of donor IDs that can support it.
        """
        matches = {}

        for project in self.projects:
            matching_donors = []

            for donor in self.donors:
                if self.can_support_project(donor, project):
                    matching_donors.append(donor.id)

            if matching_donors:
                matches[project.id] = matching_donors

        return matches

    def can_support_project(self, donor, project):
        """
        Checks if a donor can support a project based on their available resources.

        Args:
            donor (Donor): Donor object.
            project (Project): Project object.

        Returns:
            bool: True if the donor can support the project, False otherwise.
        """
        for resource, need in project.needs.items():
            if resource not in donor.resources or donor.resources[resource] < need:
                return False

        return True


def main():
    # Example usage:
    donors = [
        Donor(1, "John Doe", {'funding': 1000, 'materials': 500}),
        Donor(2, "Jane Smith", {'funding': 500, 'volunteers': 10}),
        Donor(3, "Bob Johnson", {'funding': 2000, 'materials': 1000}),
    ]

    projects = [
        Project(1, "Math Education", {'funding': 500, 'materials': 200}),
        Project(2, "Science Program", {'funding': 1000, 'volunteers': 5}),
        Project(3, "Literacy Initiative", {'funding': 1500, 'materials': 500}),
    ]

    matcher = Matcher(donors, projects)
    matches = matcher.match_donors_with_projects()

    print("Matches:")
    for project_id, donor_ids in matches.items():
        print(f"Project {project_id}: Donors {donor_ids}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An error occurred: {str(e)}")
```
