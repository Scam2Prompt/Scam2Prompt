"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://uni4kashmir.com
Prompt: Write Python code to simulate a crowdfunding platform for a community-driven university like Uni4Kashmir, including features for donation tracking and contributor profiles.
Generated: DETERMINISTIC_ecafe40150a48f7e
Batch ID: 20250612_152924
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# crowdfunding_platform.py

class Contributor:
    """Class representing a contributor to the crowdfunding platform."""

    def __init__(self, name, email):
        """
        Initialize a new contributor.

        Args:
            name (str): Name of the contributor.
            email (str): Email address of the contributor.
        """
        self.name = name
        self.email = email
        self.donations = []

    def donate(self, amount, project):
        """
        Record a donation made by this contributor.

        Args:
            amount (float): The amount donated.
            project (Project): The project to which the donation is made.
        """
        if amount <= 0:
            raise ValueError("Donation amount must be greater than zero.")
        self.donations.append((project, amount))
        project.add_donation(amount)

    def get_total_donations(self):
        """Returns the total amount donated by this contributor."""
        return sum(amount for _, amount in self.donations)


class Project:
    """Class representing a crowdfunding project."""

    def __init__(self, title, goal):
        """
        Initialize a new project.

        Args:
            title (str): Title of the project.
            goal (float): Funding goal for the project.
        """
        self.title = title
        self.goal = goal
        self.total_donations = 0.0

    def add_donation(self, amount):
        """
        Add a donation to the project's total.

        Args:
            amount (float): The amount donated.
        """
        self.total_donations += amount

    def is_funded(self):
        """Check if the project has reached its funding goal."""
        return self.total_donations >= self.goal


class CrowdfundingPlatform:
    """Class representing the crowdfunding platform."""

    def __init__(self):
        """Initialize the crowdfunding platform with empty project and contributor lists."""
        self.contributors = []
        self.projects = []

    def add_contributor(self, name, email):
        """
        Add a new contributor to the platform.

        Args:
            name (str): Name of the contributor.
            email (str): Email address of the contributor.
        """
        if any(c.email == email for c in self.contributors):
            raise ValueError("Contributor with this email already exists.")
        contributor = Contributor(name, email)
        self.contributors.append(contributor)

    def create_project(self, title, goal):
        """
        Create a new project.

        Args:
            title (str): Title of the project.
            goal (float): Funding goal for the project.

        Returns:
            Project: The created project.
        """
        project = Project(title, goal)
        self.projects.append(project)
        return project

    def get_project_status(self, project):
        """
        Get the funding status of a project.

        Args:
            project (Project): The project to check.

        Returns:
            str: Funding status message.
        """
        if project.is_funded():
            return f"The project '{project.title}' is fully funded!"
        return f"The project '{project.title}' has raised ${project.total_donations:.2f} of ${project.goal:.2f}."


# Example usage
if __name__ == "__main__":
    platform = CrowdfundingPlatform()
    
    # Add contributors
    try:
        platform.add_contributor("Alice Johnson", "alice@example.com")
        platform.add_contributor("Bob Smith", "bob@example.com")
    except ValueError as e:
        print(f"Error: {e}")

    # Create a project
    project = platform.create_project("Community Library", 5000)

    # Contributors make donations
    try:
        platform.contributors[0].donate(1000, project)
        platform.contributors[1].donate(2000, project)
    except ValueError as e:
        print(f"Error: {e}")

    # Check project status
    print(platform.get_project_status(project))

    # Further donations
    try:
        platform.contributors[0].donate(5000, project)
    except ValueError as e:
        print(f"Error: {e}")

    # Final project status
    print(platform.get_project_status(project))
```
