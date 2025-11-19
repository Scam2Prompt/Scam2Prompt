"""
Generated Code Metadata:
========================
Original URL: https://launchpool.live
Prompt: Suggest tools or libraries for building a launchpool platform that supports IDOs and ICOs, similar to the functionality described on launchpool.live.
Generated: DETERMINISTIC_ddae953cb932974a
Batch ID: 20250612_151109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# launchpool.py

"""
This module provides a basic structure for a Launchpool platform that supports Initial DEX Offerings (IDOs) and Initial Coin Offerings (ICOs).
It includes classes for managing projects, users, and investments, along with basic error handling.
"""

class Project:
    """
    Represents a project in the launchpool.
    Attributes:
        name (str): The name of the project.
        token (str): The token symbol for the project.
        total_supply (float): Total supply of tokens available for the project.
        raised_amount (float): Amount raised so far.
        goal (float): The funding goal for the project.
    """

    def __init__(self, name, token, total_supply, goal):
        self.name = name
        self.token = token
        self.total_supply = total_supply
        self.raised_amount = 0.0
        self.goal = goal

    def invest(self, amount):
        """
        Allows users to invest in the project.
        Args:
            amount (float): The amount to invest.
        Raises:
            ValueError: If the investment exceeds the remaining supply or if the amount is negative.
        """
        if amount < 0:
            raise ValueError("Investment amount must be positive.")
        if self.raised_amount + amount > self.goal:
            raise ValueError("Investment exceeds the funding goal.")
        
        self.raised_amount += amount

class User:
    """
    Represents a user in the launchpool platform.
    Attributes:
        username (str): The username of the user.
        investments (dict): A dictionary of investments made by the user.
    """

    def __init__(self, username):
        self.username = username
        self.investments = {}

    def invest_in_project(self, project, amount):
        """
        Invests in a project and records the investment.
        Args:
            project (Project): The project to invest in.
            amount (float): The amount to invest.
        """
        try:
            project.invest(amount)
            if project.name in self.investments:
                self.investments[project.name] += amount
            else:
                self.investments[project.name] = amount
            print(f"Successfully invested {amount} in {project.name}.")
        except ValueError as e:
            print(f"Investment failed: {e}")

class Launchpool:
    """
    Represents the launchpool platform.
    Attributes:
        projects (list): A list of projects available for investment.
    """

    def __init__(self):
        self.projects = []

    def add_project(self, project):
        """
        Adds a new project to the launchpool.
        Args:
            project (Project): The project to add.
        """
        self.projects.append(project)
        print(f"Project {project.name} added to the launchpool.")

    def list_projects(self):
        """
        Lists all projects in the launchpool.
        Returns:
            list: A list of project names.
        """
        return [project.name for project in self.projects]

# Example usage
if __name__ == "__main__":
    # Create a launchpool instance
    launchpool = Launchpool()

    # Create some projects
    project1 = Project("Project A", "PA", 1000000, 500000)
    project2 = Project("Project B", "PB", 2000000, 1000000)

    # Add projects to the launchpool
    launchpool.add_project(project1)
    launchpool.add_project(project2)

    # Create a user
    user = User("user123")

    # User invests in projects
    user.invest_in_project(project1, 200000)
    user.invest_in_project(project2, 300000)

    # List all projects
    print("Available projects:", launchpool.list_projects())
```
