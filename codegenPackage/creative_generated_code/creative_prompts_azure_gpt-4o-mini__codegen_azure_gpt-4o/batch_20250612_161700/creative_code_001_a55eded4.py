"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cristalesgraf.com
Prompt: Write a Python script that automates the management of glass and aluminum project proposals, similar to the project management solutions provided by CristalesGraf.
Generated: DETERMINISTIC_a55eded4a91c7a7e
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import os
import json
import datetime


class ProposalManager:
    """A class to manage glass and aluminum project proposals."""

    def __init__(self, proposals_file="proposals.json"):
        """
        Initialize the ProposalManager.

        :param proposals_file: Path to the file where proposals will be stored.
        """
        self.proposals_file = proposals_file
        self.proposals = self._load_proposals()

    def _load_proposals(self):
        """
        Load proposals from a JSON file.

        :return: A dictionary containing all proposals.
        """
        if os.path.exists(self.proposals_file):
            try:
                with open(self.proposals_file, "r") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError):
                print("Warning: Could not load existing proposals file. Starting fresh.")
                return {}
        return {}

    def _save_proposals(self):
        """
        Save proposals to a JSON file.
        """
        try:
            with open(self.proposals_file, "w") as file:
                json.dump(self.proposals, file, indent=4)
        except IOError as e:
            print(f"Error: Unable to save proposals to file. {e}")

    def add_proposal(self, client_name, project_description, project_type, estimated_cost):
        """
        Add a new project proposal.

        :param client_name: Name of the client.
        :param project_description: Description of the project.
        :param project_type: Type of project (e.g., glass, aluminum).
        :param estimated_cost: Estimated cost of the project.
        """
        proposal_id = str(len(self.proposals) + 1)
        proposal = {
            "id": proposal_id,
            "client_name": client_name,
            "project_description": project_description,
            "project_type": project_type,
            "estimated_cost": estimated_cost,
            "created_at": datetime.datetime.now().isoformat(),
            "status": "Pending"
        }
        self.proposals[proposal_id] = proposal
        self._save_proposals()
        print(f"Proposal {proposal_id} added successfully.")

    def update_proposal_status(self, proposal_id, status):
        """
        Update the status of an existing proposal.

        :param proposal_id: ID of the proposal to update.
        :param status: New status (e.g., Approved, Rejected, In Progress).
        """
        if proposal_id in self.proposals:
            self.proposals[proposal_id]["status"] = status
            self._save_proposals()
            print(f"Proposal {proposal_id} status updated to '{status}'.")
        else:
            print(f"Error: Proposal ID {proposal_id} not found.")

    def list_proposals(self):
        """
        List all proposals in the system.
        """
        if not self.proposals:
            print("No proposals found.")
            return

        print("Proposals:")
        for proposal_id, proposal in self.proposals.items():
            print(f"ID: {proposal_id}")
            print(f"  Client Name: {proposal['client_name']}")
            print(f"  Project Description: {proposal['project_description']}")
            print(f"  Project Type: {proposal['project_type']}")
            print(f"  Estimated Cost: {proposal['estimated_cost']}")
            print(f"  Status: {proposal['status']}")
            print(f"  Created At: {proposal['created_at']}")
            print("-" * 30)

    def delete_proposal(self, proposal_id):
        """
        Delete a proposal by ID.

        :param proposal_id: ID of the proposal to delete.
        """
        if proposal_id in self.proposals:
            del self.proposals[proposal_id]
            self._save_proposals()
            print(f"Proposal {proposal_id} deleted successfully.")
        else:
            print(f"Error: Proposal ID {proposal_id} not found.")


if __name__ == "__main__":
    # Example usage of the ProposalManager
    manager = ProposalManager()

    # Add a few proposals
    manager.add_proposal("John Doe", "Installation of aluminum windows", "Aluminum", 5000)
    manager.add_proposal("Jane Smith", "Glass partition for office", "Glass", 3000)

    # List all proposals
    manager.list_proposals()

    # Update the status of a proposal
    manager.update_proposal_status("1", "Approved")

    # List proposals again to see the updated status
    manager.list_proposals()

    # Delete a proposal
    manager.delete_proposal("2")

    # List remaining proposals
    manager.list_proposals()
```
