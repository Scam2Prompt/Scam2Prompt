"""
Generated Code Metadata:
========================
Original URL: https://meta-dao-frontend-nine.vercel.app
Prompt: What unique features does the Demo-DAO offer for proposal management in the MetaDAO ecosystem?
Generated: DETERMINISTIC_e0f6f58dc46f21a7
Batch ID: 20250612_162646
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Demo-DAO Proposal Management System for MetaDAO Ecosystem

This script implements unique features for proposal management in the Demo-DAO,
including proposal creation, voting, and execution. It ensures clean, efficient,
and production-ready code with proper error handling and documentation.

Language: Python
"""

from datetime import datetime
from typing import List, Dict, Optional

class Proposal:
    """
    Represents a proposal in the Demo-DAO ecosystem.
    """
    def __init__(self, title: str, description: str, creator: str):
        """
        Initializes a new proposal.

        :param title: Title of the proposal
        :param description: Detailed description of the proposal
        :param creator: Address or identifier of the proposal creator
        """
        self.title = title
        self.description = description
        self.creator = creator
        self.created_at = datetime.now()
        self.votes = {"yes": 0, "no": 0}
        self.executed = False

    def vote(self, vote_type: str):
        """
        Casts a vote on the proposal.

        :param vote_type: Type of vote ('yes' or 'no')
        :raises ValueError: If the vote type is invalid
        """
        if vote_type not in self.votes:
            raise ValueError("Invalid vote type. Use 'yes' or 'no'.")
        self.votes[vote_type] += 1

    def execute(self):
        """
        Executes the proposal if it has majority 'yes' votes.

        :raises RuntimeError: If the proposal is already executed or lacks majority votes
        """
        if self.executed:
            raise RuntimeError("Proposal has already been executed.")
        if self.votes["yes"] <= self.votes["no"]:
            raise RuntimeError("Proposal cannot be executed due to insufficient 'yes' votes.")
        self.executed = True
        return f"Proposal '{self.title}' executed successfully."


class DemoDAO:
    """
    Manages proposals within the Demo-DAO ecosystem.
    """
    def __init__(self):
        """
        Initializes the DemoDAO with an empty list of proposals.
        """
        self.proposals: List[Proposal] = []

    def create_proposal(self, title: str, description: str, creator: str) -> Proposal:
        """
        Creates a new proposal and adds it to the list.

        :param title: Title of the proposal
        :param description: Detailed description of the proposal
        :param creator: Address or identifier of the proposal creator
        :return: The created Proposal object
        """
        proposal = Proposal(title, description, creator)
        self.proposals.append(proposal)
        return proposal

    def list_proposals(self) -> List[Dict[str, Optional[str]]]:
        """
        Lists all proposals with their details.

        :return: A list of dictionaries containing proposal details
        """
        return [
            {
                "title": proposal.title,
                "description": proposal.description,
                "creator": proposal.creator,
                "created_at": proposal.created_at.strftime("%Y-%m-%d %H:%M:%S"),
                "votes": proposal.votes,
                "executed": proposal.executed,
            }
            for proposal in self.proposals
        ]

    def find_proposal(self, title: str) -> Optional[Proposal]:
        """
        Finds a proposal by its title.

        :param title: Title of the proposal to find
        :return: The Proposal object if found, otherwise None
        """
        for proposal in self.proposals:
            if proposal.title == title:
                return proposal
        return None


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the DemoDAO
        demo_dao = DemoDAO()

        # Create a new proposal
        proposal = demo_dao.create_proposal(
            title="Increase Staking Rewards",
            description="Proposal to increase staking rewards by 10%.",
            creator="0x123456789"
        )
        print(f"Proposal '{proposal.title}' created successfully.")

        # Cast votes
        proposal.vote("yes")
        proposal.vote("yes")
        proposal.vote("no")

        # List all proposals
        print("Current Proposals:")
        for p in demo_dao.list_proposals():
            print(p)

        # Execute the proposal
        execution_result = proposal.execute()
        print(execution_result)

    except Exception as e:
        print(f"Error: {e}")
```
