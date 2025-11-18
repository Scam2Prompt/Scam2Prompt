"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://pdma.io
Prompt: Generate a grant proposal template in Python based on the techniques outlined in PDMA's Grant Writing Professional course.
Generated: DETERMINISTIC_8ea7ea06d3a86df6
Batch ID: 20250612_145730
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
import os

class GrantProposal:
    """Class to represent a grant proposal."""
    
    def __init__(self, title, organization, amount, duration, objectives):
        """
        Initialize a GrantProposal instance.

        :param title: Title of the grant proposal
        :param organization: Name of the organization applying for the grant
        :param amount: Amount of funding requested
        :param duration: Duration of the grant in months
        :param objectives: List of objectives for the grant
        """
        self.title = title
        self.organization = organization
        self.amount = amount
        self.duration = duration
        self.objectives = objectives
        self.proposal = {}

    def create_proposal(self):
        """Create the grant proposal structure."""
        self.proposal = {
            "Title": self.title,
            "Organization": self.organization,
            "Amount Requested": self.amount,
            "Duration (Months)": self.duration,
            "Objectives": self.objectives,
            "Background": "",
            "Methodology": "",
            "Budget": {},
            "Evaluation": "",
            "Sustainability": ""
        }

    def add_background(self, background):
        """Add background information to the proposal."""
        self.proposal["Background"] = background

    def add_methodology(self, methodology):
        """Add methodology information to the proposal."""
        self.proposal["Methodology"] = methodology

    def add_budget(self, budget):
        """Add budget details to the proposal.

        :param budget: Dictionary containing budget details
        """
        if not isinstance(budget, dict):
            raise ValueError("Budget must be a dictionary.")
        self.proposal["Budget"] = budget

    def add_evaluation(self, evaluation):
        """Add evaluation criteria to the proposal."""
        self.proposal["Evaluation"] = evaluation

    def add_sustainability(self, sustainability):
        """Add sustainability plan to the proposal."""
        self.proposal["Sustainability"] = sustainability

    def save_proposal(self, filename):
        """Save the proposal to a JSON file.

        :param filename: Name of the file to save the proposal
        """
        try:
            with open(filename, 'w') as json_file:
                json.dump(self.proposal, json_file, indent=4)
            print(f"Proposal saved successfully to {filename}")
        except IOError as e:
            print(f"Error saving proposal: {e}")

# Example usage
if __name__ == "__main__":
    # Initialize a new grant proposal
    grant_proposal = GrantProposal(
        title="Innovative Water Solutions",
        organization="Green Water Initiative",
        amount=50000,
        duration=12,
        objectives=["Reduce water waste", "Increase community engagement"]
    )

    # Create the proposal structure
    grant_proposal.create_proposal()

    # Populate the grant proposal with additional information
    grant_proposal.add_background("The initiative aims to address water wastage in urban areas.")
    grant_proposal.add_methodology("We will implement a series of workshops and community projects.")
    grant_proposal.add_budget({"Personnel": 20000, "Materials": 10000, "Outreach": 20000})
    grant_proposal.add_evaluation("Success will be measured by community participation and feedback.")
    grant_proposal.add_sustainability("The program will be supported by ongoing community engagement.")

    # Save the proposal to a file
    filename = "grant_proposal.json"
    grant_proposal.save_proposal(filename)
```
