"""
Generated Code Metadata:
========================
Original URL: https://cristalesgraf.com
Prompt: Write a Python script that automates the management of glass and aluminum project proposals, similar to the project management solutions provided by CristalesGraf.
Generated: DETERMINISTIC_a55eded4a91c7a7e
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
import os
from typing import List, Dict, Any

class ProjectProposalManager:
    """
    A class to manage project proposals for glass and aluminum projects.
    """

    def __init__(self, storage_file: str):
        """
        Initializes the ProjectProposalManager with a specified storage file.

        :param storage_file: Path to the JSON file where proposals are stored.
        """
        self.storage_file = storage_file
        self.proposals = self.load_proposals()

    def load_proposals(self) -> List[Dict[str, Any]]:
        """
        Loads project proposals from the storage file.

        :return: A list of project proposals.
        """
        if not os.path.exists(self.storage_file):
            return []
        with open(self.storage_file, 'r') as file:
            try:
                return json.load(file)
            except json.JSONDecodeError as e:
                print(f"Error loading proposals: {e}")
                return []

    def save_proposals(self) -> None:
        """
        Saves the current list of proposals to the storage file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump(self.proposals, file, indent=4)

    def add_proposal(self, proposal: Dict[str, Any]) -> None:
        """
        Adds a new project proposal to the list and saves it.

        :param proposal: A dictionary containing proposal details.
        """
        self.proposals.append(proposal)
        self.save_proposals()

    def remove_proposal(self, proposal_id: str) -> None:
        """
        Removes a project proposal by its ID and saves the changes.

        :param proposal_id: The ID of the proposal to remove.
        """
        self.proposals = [p for p in self.proposals if p.get('id') != proposal_id]
        self.save_proposals()

    def get_proposals(self) -> List[Dict[str, Any]]:
        """
        Retrieves the list of all project proposals.

        :return: A list of project proposals.
        """
        return self.proposals

    def find_proposal(self, proposal_id: str) -> Dict[str, Any]:
        """
        Finds a project proposal by its ID.

        :param proposal_id: The ID of the proposal to find.
        :return: The proposal if found, otherwise None.
        """
        for proposal in self.proposals:
            if proposal.get('id') == proposal_id:
                return proposal
        return None

def main():
    """
    Main function to demonstrate the usage of ProjectProposalManager.
    """
    manager = ProjectProposalManager('proposals.json')

    # Example usage
    new_proposal = {
        "id": "001",
        "title": "Glass Facade Project",
        "description": "A project to design and install a glass facade.",
        "budget": 50000,
        "status": "pending"
    }

    # Add a new proposal
    manager.add_proposal(new_proposal)

    # Retrieve and print all proposals
    proposals = manager.get_proposals()
    print("Current Proposals:")
    for proposal in proposals:
        print(proposal)

    # Find a specific proposal
    found_proposal = manager.find_proposal("001")
    print("Found Proposal:", found_proposal)

    # Remove a proposal
    manager.remove_proposal("001")
    print("Proposals after removal:", manager.get_proposals())

if __name__ == "__main__":
    main()
```
