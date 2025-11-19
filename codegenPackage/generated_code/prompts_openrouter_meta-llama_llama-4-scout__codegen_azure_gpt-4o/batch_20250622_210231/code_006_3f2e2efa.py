"""
Generated Code Metadata:
========================
Original URL: https://darkblog.pages.dev
Prompt: Develop a basic DAO management tool using the ENS DAO as a reference, including features for proposal management and voting.
Generated: DETERMINISTIC_3f2e2efacdeee7ad
Batch ID: 20250622_210231
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
DAO Management Tool
This script provides basic functionality for managing proposals and voting in a DAO.
It uses the Ethereum Name Service (ENS) DAO as a reference.
"""

import json
from datetime import datetime
from typing import List, Dict, Optional

class Proposal:
    """
    Represents a proposal in the DAO.
    """
    def __init__(self, proposal_id: int, title: str, description: str, creator: str):
        self.proposal_id = proposal_id
        self.title = title
        self.description = description
        self.creator = creator
        self.created_at = datetime.now()
        self.votes = {"yes": 0, "no": 0}
        self.status = "active"  # Status can be 'active', 'approved', or 'rejected'

    def to_dict(self) -> Dict:
        """
        Converts the proposal object to a dictionary for serialization.
        """
        return {
            "proposal_id": self.proposal_id,
            "title": self.title,
            "description": self.description,
            "creator": self.creator,
            "created_at": self.created_at.isoformat(),
            "votes": self.votes,
            "status": self.status,
        }


class DAOManagementTool:
    """
    A basic DAO management tool for handling proposals and voting.
    """
    def __init__(self):
        self.proposals: List[Proposal] = []
        self.next_proposal_id = 1

    def create_proposal(self, title: str, description: str, creator: str) -> Proposal:
        """
        Creates a new proposal and adds it to the list of proposals.
        """
        proposal = Proposal(self.next_proposal_id, title, description, creator)
        self.proposals.append(proposal)
        self.next_proposal_id += 1
        return proposal

    def list_proposals(self) -> List[Dict]:
        """
        Lists all proposals in the DAO.
        """
        return [proposal.to_dict() for proposal in self.proposals]

    def vote_on_proposal(self, proposal_id: int, vote: str) -> Optional[str]:
        """
        Casts a vote on a proposal. Vote can be 'yes' or 'no'.
        """
        proposal = self._find_proposal_by_id(proposal_id)
        if not proposal:
            return "Proposal not found."
        if proposal.status != "active":
            return "Voting is closed for this proposal."
        if vote not in ["yes", "no"]:
            return "Invalid vote. Please vote 'yes' or 'no'."
        proposal.votes[vote] += 1
        return "Vote cast successfully."

    def close_voting(self, proposal_id: int) -> Optional[str]:
        """
        Closes voting for a proposal and determines its status.
        """
        proposal = self._find_proposal_by_id(proposal_id)
        if not proposal:
            return "Proposal not found."
        if proposal.status != "active":
            return "Voting is already closed for this proposal."
        if proposal.votes["yes"] > proposal.votes["no"]:
            proposal.status = "approved"
        else:
            proposal.status = "rejected"
        return f"Voting closed. Proposal status: {proposal.status}"

    def _find_proposal_by_id(self, proposal_id: int) -> Optional[Proposal]:
        """
        Finds a proposal by its ID.
        """
        for proposal in self.proposals:
            if proposal.proposal_id == proposal_id:
                return proposal
        return None

    def save_to_file(self, file_path: str) -> str:
        """
        Saves the current state of proposals to a JSON file.
        """
        try:
            with open(file_path, "w") as file:
                json.dump([proposal.to_dict() for proposal in self.proposals], file, indent=4)
            return "Proposals saved successfully."
        except Exception as e:
            return f"Error saving proposals: {e}"

    def load_from_file(self, file_path: str) -> str:
        """
        Loads proposals from a JSON file.
        """
        try:
            with open(file_path, "r") as file:
                proposals_data = json.load(file)
                self.proposals = [
                    Proposal(
                        proposal_id=proposal["proposal_id"],
                        title=proposal["title"],
                        description=proposal["description"],
                        creator=proposal["creator"],
                    )
                    for proposal in proposals_data
                ]
                for proposal, data in zip(self.proposals, proposals_data):
                    proposal.created_at = datetime.fromisoformat(data["created_at"])
                    proposal.votes = data["votes"]
                    proposal.status = data["status"]
            return "Proposals loaded successfully."
        except Exception as e:
            return f"Error loading proposals: {e}"


# Example usage
if __name__ == "__main__":
    dao_tool = DAOManagementTool()

    # Create a proposal
    proposal = dao_tool.create_proposal(
        title="Increase Treasury Allocation",
        description="Proposal to increase the treasury allocation by 10%.",
        creator="Alice"
    )
    print(f"Created Proposal: {proposal.to_dict()}")

    # List proposals
    print("Proposals:", dao_tool.list_proposals())

    # Vote on a proposal
    print(dao_tool.vote_on_proposal(proposal_id=1, vote="yes"))
    print(dao_tool.vote_on_proposal(proposal_id=1, vote="no"))

    # Close voting
    print(dao_tool.close_voting(proposal_id=1))

    # Save proposals to file
    print(dao_tool.save_to_file("proposals.json"))

    # Load proposals from file
    print(dao_tool.load_from_file("proposals.json"))
    print("Proposals after loading:", dao_tool.list_proposals())
```
