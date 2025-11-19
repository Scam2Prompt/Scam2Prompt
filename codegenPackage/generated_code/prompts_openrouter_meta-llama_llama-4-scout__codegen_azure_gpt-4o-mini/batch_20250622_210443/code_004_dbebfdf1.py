"""
Generated Code Metadata:
========================
Original URL: https://bigwaveinfotech.net
Prompt: "Design a graphics design workflow for managing client proposals from typesetting to production, inspired by BigWaveInfotech's graphics design services."
Generated: DETERMINISTIC_dbebfdf114b2bc31
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import os
import json
from datetime import datetime

class Proposal:
    """
    A class to represent a client proposal in the graphics design workflow.
    """

    def __init__(self, client_name, project_name, details):
        """
        Initializes a new Proposal instance.

        :param client_name: Name of the client
        :param project_name: Name of the project
        :param details: Details of the proposal
        """
        self.client_name = client_name
        self.project_name = project_name
        self.details = details
        self.status = 'Draft'
        self.created_at = datetime.now()
        self.updated_at = self.created_at

    def update_status(self, new_status):
        """
        Updates the status of the proposal.

        :param new_status: New status to set
        """
        valid_statuses = ['Draft', 'Submitted', 'Approved', 'In Production', 'Completed']
        if new_status in valid_statuses:
            self.status = new_status
            self.updated_at = datetime.now()
        else:
            raise ValueError(f"Invalid status: {new_status}. Valid statuses are: {valid_statuses}")

    def to_dict(self):
        """
        Converts the proposal to a dictionary for easy serialization.

        :return: Dictionary representation of the proposal
        """
        return {
            'client_name': self.client_name,
            'project_name': self.project_name,
            'details': self.details,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

class ProposalManager:
    """
    A class to manage multiple proposals.
    """

    def __init__(self, storage_file='proposals.json'):
        """
        Initializes the ProposalManager with a storage file.

        :param storage_file: Path to the JSON file for storing proposals
        """
        self.storage_file = storage_file
        self.proposals = self.load_proposals()

    def load_proposals(self):
        """
        Loads proposals from the storage file.

        :return: List of Proposal instances
        """
        if os.path.exists(self.storage_file):
            with open(self.storage_file, 'r') as file:
                proposals_data = json.load(file)
                return [Proposal(**data) for data in proposals_data]
        return []

    def save_proposals(self):
        """
        Saves the current proposals to the storage file.
        """
        with open(self.storage_file, 'w') as file:
            json.dump([proposal.to_dict() for proposal in self.proposals], file, indent=4)

    def add_proposal(self, client_name, project_name, details):
        """
        Adds a new proposal to the manager.

        :param client_name: Name of the client
        :param project_name: Name of the project
        :param details: Details of the proposal
        """
        new_proposal = Proposal(client_name, project_name, details)
        self.proposals.append(new_proposal)
        self.save_proposals()

    def update_proposal_status(self, project_name, new_status):
        """
        Updates the status of a proposal by project name.

        :param project_name: Name of the project to update
        :param new_status: New status to set
        """
        for proposal in self.proposals:
            if proposal.project_name == project_name:
                proposal.update_status(new_status)
                self.save_proposals()
                return
        raise ValueError(f"No proposal found for project: {project_name}")

    def get_proposals(self):
        """
        Returns all proposals.

        :return: List of Proposal instances
        """
        return self.proposals

# Example usage
if __name__ == "__main__":
    try:
        manager = ProposalManager()
        manager.add_proposal("Client A", "Project X", "Design a new logo.")
        manager.update_proposal_status("Project X", "Submitted")
        for proposal in manager.get_proposals():
            print(proposal.to_dict())
    except Exception as e:
        print(f"An error occurred: {e}")
```
