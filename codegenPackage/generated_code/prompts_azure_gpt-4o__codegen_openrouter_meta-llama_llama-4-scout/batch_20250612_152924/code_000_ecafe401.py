"""
Generated Code Metadata:
========================
Original URL: https://uni4kashmir.com
Prompt: Write Python code to simulate a crowdfunding platform for a community-driven university like Uni4Kashmir, including features for donation tracking and contributor profiles.
Generated: DETERMINISTIC_ecafe40150a48f7e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# crowdfunding_platform.py

class Contributor:
    """Represents a contributor to a crowdfunding campaign."""

    def __init__(self, name, email):
        """
        Initializes a Contributor object.

        Args:
            name (str): The contributor's name.
            email (str): The contributor's email address.
        """
        self.name = name
        self.email = email
        self.donations = []

    def add_donation(self, amount, project):
        """
        Records a donation made by the contributor.

        Args:
            amount (float): The donation amount.
            project (str): The project being donated to.
        """
        self.donations.append((project, amount))


class Project:
    """Represents a crowdfunding project."""

    def __init__(self, name, goal):
        """
        Initializes a Project object.

        Args:
            name (str): The project's name.
            goal (float): The project's funding goal.
        """
        self.name = name
        self.goal = goal
        self.donations = []

    def add_donation(self, contributor, amount):
        """
        Records a donation made to the project.

        Args:
            contributor (Contributor): The contributor making the donation.
            amount (float): The donation amount.
        """
        self.donations.append((contributor, amount))
        contributor.add_donation(amount, self.name)

    def get_progress(self):
        """
        Calculates the project's funding progress.

        Returns:
            float: The percentage of the goal that has been funded.
        """
        total_donated = sum(donation[1] for donation in self.donations)
        return (total_donated / self.goal) * 100


class CrowdfundingPlatform:
    """Simulates a crowdfunding platform."""

    def __init__(self):
        self.contributors = {}
        self.projects = {}

    def add_contributor(self, name, email):
        """
        Adds a new contributor to the platform.

        Args:
            name (str): The contributor's name.
            email (str): The contributor's email address.

        Raises:
            ValueError: If a contributor with the same email already exists.
        """
        if email in self.contributors:
            raise ValueError("Contributor with this email already exists")
        self.contributors[email] = Contributor(name, email)

    def add_project(self, name, goal):
        """
        Adds a new project to the platform.

        Args:
            name (str): The project's name.
            goal (float): The project's funding goal.

        Raises:
            ValueError: If a project with the same name already exists.
        """
        if name in self.projects:
            raise ValueError("Project with this name already exists")
        self.projects[name] = Project(name, goal)

    def make_donation(self, contributor_email, project_name, amount):
        """
        Records a donation made by a contributor to a project.

        Args:
            contributor_email (str): The contributor's email address.
            project_name (str): The project's name.
            amount (float): The donation amount.

        Raises:
            ValueError: If the contributor or project does not exist.
        """
        if contributor_email not in self.contributors:
            raise ValueError("Contributor does not exist")
        if project_name not in self.projects:
            raise ValueError("Project does not exist")
        contributor = self.contributors[contributor_email]
        project = self.projects[project_name]
        project.add_donation(contributor, amount)

    def get_contributor_profile(self, email):
        """
        Retrieves a contributor's profile.

        Args:
            email (str): The contributor's email address.

        Returns:
            dict: The contributor's profile information.

        Raises:
            ValueError: If the contributor does not exist.
        """
        if email not in self.contributors:
            raise ValueError("Contributor does not exist")
        contributor = self.contributors[email]
        return {
            "name": contributor.name,
            "email": contributor.email,
            "donations": contributor.donations,
        }

    def get_project_status(self, project_name):
        """
        Retrieves a project's status.

        Args:
            project_name (str): The project's name.

        Returns:
            dict: The project's status information.

        Raises:
            ValueError: If the project does not exist.
        """
        if project_name not in self.projects:
            raise ValueError("Project does not exist")
        project = self.projects[project_name]
        return {
            "name": project.name,
            "goal": project.goal,
            "donations": project.donations,
            "progress": project.get_progress(),
        }


def main():
    platform = CrowdfundingPlatform()

    # Add contributors
    platform.add_contributor("John Doe", "john@example.com")
    platform.add_contributor("Jane Doe", "jane@example.com")

    # Add projects
    platform.add_project("Uni4Kashmir", 10000.0)
    platform.add_project("Kashmir Education Initiative", 5000.0)

    # Make donations
    platform.make_donation("john@example.com", "Uni4Kashmir", 1000.0)
    platform.make_donation("jane@example.com", "Uni4Kashmir", 2000.0)
    platform.make_donation("john@example.com", "Kashmir Education Initiative", 500.0)

    # Get contributor profiles
    print(platform.get_contributor_profile("john@example.com"))
    print(platform.get_contributor_profile("jane@example.com"))

    # Get project status
    print(platform.get_project_status("Uni4Kashmir"))
    print(platform.get_project_status("Kashmir Education Initiative"))


if __name__ == "__main__":
    main()
```
