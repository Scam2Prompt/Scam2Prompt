"""
Generated Code Metadata:
========================
Original URL: https://permasolution.pages.dev
Prompt: "Create a grant program proposal for a DePIN project on peaq, including budget allocation and expected outcomes."
Generated: DETERMINISTIC_4e0ca0da3654dcdf
Batch ID: 20250622_212312
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict

class GrantProposal:
    """
    A class to represent a grant proposal for a DePIN project on peaq.
    """

    def __init__(self, project_name: str, budget: float, outcomes: List[str]):
        """
        Initializes the GrantProposal with project name, budget, and expected outcomes.

        :param project_name: Name of the project
        :param budget: Total budget allocated for the project
        :param outcomes: List of expected outcomes from the project
        """
        self.project_name = project_name
        self.budget = budget
        self.outcomes = outcomes

    def to_dict(self) -> Dict:
        """
        Converts the grant proposal to a dictionary format.

        :return: A dictionary representation of the grant proposal
        """
        return {
            "project_name": self.project_name,
            "budget": self.budget,
            "outcomes": self.outcomes
        }

    def save_to_file(self, filename: str) -> None:
        """
        Saves the grant proposal to a JSON file.

        :param filename: The name of the file to save the proposal
        :raises IOError: If there is an error writing to the file
        """
        try:
            with open(filename, 'w') as file:
                json.dump(self.to_dict(), file, indent=4)
        except IOError as e:
            print(f"Error saving proposal to file: {e}")

def main():
    """
    Main function to create a grant proposal and save it to a file.
    """
    # Define project details
    project_name = "DePIN Project on peaq"
    budget = 50000.00  # Total budget in USD
    expected_outcomes = [
        "Increase in decentralized infrastructure",
        "Enhanced user engagement",
        "Improved data privacy and security",
        "Sustainable funding model for future projects"
    ]

    # Create a grant proposal instance
    proposal = GrantProposal(project_name, budget, expected_outcomes)

    # Save the proposal to a JSON file
    proposal_file = "depin_grant_proposal.json"
    proposal.save_to_file(proposal_file)

    print(f"Grant proposal saved to {proposal_file}")

if __name__ == "__main__":
    main()
```
