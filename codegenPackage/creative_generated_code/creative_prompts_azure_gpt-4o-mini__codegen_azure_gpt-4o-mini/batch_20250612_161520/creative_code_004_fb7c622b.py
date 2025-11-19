"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-tpad.pages.dev
Prompt: Describe the rug-proof mechanisms implemented by TrustPad and how they ensure safety for early-stage investors.
Generated: DETERMINISTIC_fb7c622ba27c88c9
Batch ID: 20250612_161520
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class TrustPad:
    """
    A class to represent the TrustPad platform's rug-proof mechanisms
    ensuring safety for early-stage investors.
    """

    def __init__(self):
        self.projects = []
        self.investors = []
        self.transparency = True
        self.locked_funds = {}

    def add_project(self, project_name, project_owner):
        """
        Adds a new project to the TrustPad platform.

        Args:
            project_name (str): The name of the project.
            project_owner (str): The owner of the project.

        Raises:
            ValueError: If the project name is empty or already exists.
        """
        if not project_name or any(p['name'] == project_name for p in self.projects):
            raise ValueError("Project name must be unique and cannot be empty.")
        
        project = {
            'name': project_name,
            'owner': project_owner,
            'is_funded': False,
            'total_funds': 0,
            'investors': []
        }
        self.projects.append(project)

    def invest_in_project(self, project_name, investor, amount):
        """
        Allows an investor to invest in a specified project.

        Args:
            project_name (str): The name of the project to invest in.
            investor (str): The investor's name.
            amount (float): The amount to invest.

        Raises:
            ValueError: If the project does not exist or the amount is non-positive.
        """
        project = self._get_project(project_name)

        if amount <= 0:
            raise ValueError("Investment amount must be positive.")

        project['total_funds'] += amount
        project['investors'].append((investor, amount))
        self.locked_funds[investor] = self.locked_funds.get(investor, 0) + amount
        print(f"{investor} invested {amount} in {project_name}.")

    def _get_project(self, project_name):
        """
        Retrieves a project by its name.

        Args:
            project_name (str): The name of the project.

        Returns:
            dict: The project details.

        Raises:
            LookupError: If the project does not exist.
        """
        for project in self.projects:
            if project['name'] == project_name:
                return project
        raise LookupError("Project not found.")

    def complete_funding(self, project_name):
        """
        Completes the funding for a specified project and locks funds.

        Args:
            project_name (str): The name of the project to complete funding.

        Raises:
            LookupError: If the project does not exist or has not yet been funded.
        """
        project = self._get_project(project_name)

        if project['total_funds'] <= 0:
            raise LookupError("Cannot complete funding, project has no funds.")
        
        project['is_funded'] = True
        print(f"Funding completed for project {project_name}. Funds are now locked.")

    def unlock_funds(self, investor):
        """
        Unlocks funds for a specified investor.

        Args:
            investor (str): The investor's name.

        Raises:
            LookupError: If the investor has no locked funds.
        """
        if investor not in self.locked_funds or self.locked_funds[investor] <= 0:
            raise LookupError("No locked funds to unlock for this investor.")
        
        amount = self.locked_funds[investor]
        self.locked_funds[investor] = 0
        print(f"{amount} funds unlocked for investor {investor}.")

# Example usage:
if __name__ == "__main__":
    trust_pad = TrustPad()
    
    try:
        trust_pad.add_project("Project A", "Alice")
        trust_pad.invest_in_project("Project A", "Bob", 1000)
        trust_pad.complete_funding("Project A")
        trust_pad.unlock_funds("Bob")
    except (ValueError, LookupError) as e:
        print(f"Error: {e}")
```
