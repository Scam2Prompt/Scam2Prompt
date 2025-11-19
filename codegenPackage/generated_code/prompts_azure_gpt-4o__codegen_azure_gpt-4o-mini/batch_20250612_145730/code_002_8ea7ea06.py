"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Generate a grant proposal template in Python based on the techniques outlined in PDMA's Grant Writing Professional course.
Generated: DETERMINISTIC_8ea7ea06d3a86df6
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from datetime import datetime

class GrantProposal:
    """
    A class to represent a grant proposal.

    Attributes:
        title (str): The title of the grant proposal.
        applicant (str): The name of the applicant.
        organization (str): The name of the organization applying for the grant.
        amount_requested (float): The amount of funding requested.
        project_description (str): A description of the project.
        objectives (list): A list of project objectives.
        timeline (dict): A timeline of project milestones.
        budget (dict): A detailed budget for the project.
        created_at (datetime): The date and time the proposal was created.
    """

    def __init__(self, title, applicant, organization, amount_requested, project_description):
        """
        Initializes a new GrantProposal instance.

        Args:
            title (str): The title of the grant proposal.
            applicant (str): The name of the applicant.
            organization (str): The name of the organization applying for the grant.
            amount_requested (float): The amount of funding requested.
            project_description (str): A description of the project.
        """
        self.title = title
        self.applicant = applicant
        self.organization = organization
        self.amount_requested = amount_requested
        self.project_description = project_description
        self.objectives = []
        self.timeline = {}
        self.budget = {}
        self.created_at = datetime.now()

    def add_objective(self, objective):
        """
        Adds an objective to the grant proposal.

        Args:
            objective (str): An objective of the project.
        """
        self.objectives.append(objective)

    def set_timeline(self, milestone, date):
        """
        Sets a project milestone in the timeline.

        Args:
            milestone (str): The name of the milestone.
            date (str): The date of the milestone in 'YYYY-MM-DD' format.
        """
        try:
            datetime.strptime(date, '%Y-%m-%d')  # Validate date format
            self.timeline[milestone] = date
        except ValueError as e:
            print(f"Error: {e}. Please provide the date in 'YYYY-MM-DD' format.")

    def add_budget_item(self, item, cost):
        """
        Adds a budget item to the grant proposal.

        Args:
            item (str): The name of the budget item.
            cost (float): The cost of the budget item.
        """
        if cost < 0:
            print("Error: Cost cannot be negative.")
            return
        self.budget[item] = cost

    def to_json(self):
        """
        Converts the grant proposal to a JSON string.

        Returns:
            str: A JSON representation of the grant proposal.
        """
        proposal_dict = {
            "title": self.title,
            "applicant": self.applicant,
            "organization": self.organization,
            "amount_requested": self.amount_requested,
            "project_description": self.project_description,
            "objectives": self.objectives,
            "timeline": self.timeline,
            "budget": self.budget,
            "created_at": self.created_at.isoformat()
        }
        return json.dumps(proposal_dict, indent=4)

# Example usage
if __name__ == "__main__":
    try:
        proposal = GrantProposal(
            title="Innovative Community Project",
            applicant="Jane Doe",
            organization="Community Development Org",
            amount_requested=50000,
            project_description="A project aimed at improving community engagement through technology."
        )

        proposal.add_objective("Increase community participation by 30%")
        proposal.set_timeline("Project Start", "2024-01-01")
        proposal.set_timeline("Project End", "2024-12-31")
        proposal.add_budget_item("Personnel Costs", 20000)
        proposal.add_budget_item("Materials", 15000)
        proposal.add_budget_item("Marketing", 5000)

        print(proposal.to_json())
    except Exception as e:
        print(f"An error occurred: {e}")
```
