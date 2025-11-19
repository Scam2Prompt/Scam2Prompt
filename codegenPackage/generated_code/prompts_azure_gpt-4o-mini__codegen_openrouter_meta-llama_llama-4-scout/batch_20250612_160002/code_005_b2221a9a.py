"""
Generated Code Metadata:
========================
Original URL: https://pdma.io
Prompt: Write a grant proposal template that aligns with the grant writing techniques taught at PDMA Technologies.
Generated: DETERMINISTIC_b2221a9ab7225328
Batch ID: 20250612_160002
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# grant_proposal_template.py

class GrantProposal:
    """
    A class representing a grant proposal template.

    Attributes:
        project_title (str): The title of the project.
        project_summary (str): A brief summary of the project.
        goals_and_objectives (list): A list of project goals and objectives.
        methodology (str): A description of the project methodology.
        budget (dict): A dictionary containing the project budget.
    """

    def __init__(self, project_title, project_summary, goals_and_objectives, methodology, budget):
        """
        Initializes a GrantProposal object.

        Args:
            project_title (str): The title of the project.
            project_summary (str): A brief summary of the project.
            goals_and_objectives (list): A list of project goals and objectives.
            methodology (str): A description of the project methodology.
            budget (dict): A dictionary containing the project budget.

        Raises:
            TypeError: If any of the input arguments are of the wrong type.
            ValueError: If any of the input arguments are empty or None.
        """
        if not isinstance(project_title, str) or not project_title.strip():
            raise ValueError("Project title must be a non-empty string")
        if not isinstance(project_summary, str) or not project_summary.strip():
            raise ValueError("Project summary must be a non-empty string")
        if not isinstance(goals_and_objectives, list) or not goals_and_objectives:
            raise ValueError("Goals and objectives must be a non-empty list")
        if not isinstance(methodology, str) or not methodology.strip():
            raise ValueError("Methodology must be a non-empty string")
        if not isinstance(budget, dict) or not budget:
            raise ValueError("Budget must be a non-empty dictionary")

        self.project_title = project_title
        self.project_summary = project_summary
        self.goals_and_objectives = goals_and_objectives
        self.methodology = methodology
        self.budget = budget

    def generate_proposal(self):
        """
        Generates a grant proposal template based on the object's attributes.

        Returns:
            str: A string representing the grant proposal template.
        """
        proposal = f"**Grant Proposal: {self.project_title}**\n\n"
        proposal += f"**Project Summary:**\n{self.project_summary}\n\n"
        proposal += "**Goals and Objectives:**\n"
        for i, goal in enumerate(self.goals_and_objectives, start=1):
            proposal += f"{i}. {goal}\n"
        proposal += "\n"
        proposal += f"**Methodology:**\n{self.methodology}\n\n"
        proposal += "**Budget:**\n"
        for category, amount in self.budget.items():
            proposal += f"{category}: ${amount:.2f}\n"
        return proposal


def main():
    try:
        project_title = "Example Project"
        project_summary = "This is an example project."
        goals_and_objectives = ["Goal 1", "Goal 2", "Goal 3"]
        methodology = "This is an example methodology."
        budget = {"Personnel": 100000.0, "Equipment": 50000.0, "Travel": 20000.0}

        proposal = GrantProposal(project_title, project_summary, goals_and_objectives, methodology, budget)
        print(proposal.generate_proposal())
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
