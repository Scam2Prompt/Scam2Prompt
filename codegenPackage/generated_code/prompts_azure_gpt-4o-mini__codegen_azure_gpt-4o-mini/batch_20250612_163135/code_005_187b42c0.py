"""
Generated Code Metadata:
========================
Original URL: https://zealyi.github.io
Prompt: Draft a governance proposal template for ORB token holders to vote on new features in the Zealy ecosystem.
Generated: DETERMINISTIC_187b42c0f9f3a25c
Batch ID: 20250612_163135
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Any

class GovernanceProposal:
    """
    A class to represent a governance proposal for ORB token holders in the Zealy ecosystem.
    """

    def __init__(self, title: str, description: str, features: List[str], proposer: str):
        """
        Initializes a new governance proposal.

        :param title: Title of the proposal
        :param description: Detailed description of the proposal
        :param features: List of new features proposed
        :param proposer: Address of the proposer
        """
        self.title = title
        self.description = description
        self.features = features
        self.proposer = proposer
        self.votes = {"for": 0, "against": 0}
        self.status = "pending"  # Possible statuses: pending, approved, rejected

    def vote(self, vote_type: str) -> None:
        """
        Cast a vote on the proposal.

        :param vote_type: Type of vote ('for' or 'against')
        :raises ValueError: If the vote_type is not valid
        """
        if vote_type not in ["for", "against"]:
            raise ValueError("Invalid vote type. Must be 'for' or 'against'.")
        
        self.votes[vote_type] += 1

    def finalize(self) -> None:
        """
        Finalizes the proposal based on the votes.
        """
        total_votes = self.votes["for"] + self.votes["against"]
        if total_votes == 0:
            raise ValueError("No votes have been cast.")

        # Simple majority rule
        if self.votes["for"] > self.votes["against"]:
            self.status = "approved"
        else:
            self.status = "rejected"

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the proposal to a dictionary format for easy serialization.

        :return: Dictionary representation of the proposal
        """
        return {
            "title": self.title,
            "description": self.description,
            "features": self.features,
            "proposer": self.proposer,
            "votes": self.votes,
            "status": self.status
        }

    def to_json(self) -> str:
        """
        Converts the proposal to a JSON string.

        :return: JSON string representation of the proposal
        """
        return json.dumps(self.to_dict(), indent=4)

# Example usage
if __name__ == "__main__":
    try:
        proposal = GovernanceProposal(
            title="New Feature Proposal",
            description="Proposal to add new features to the Zealy ecosystem.",
            features=["Feature A", "Feature B"],
            proposer="0x1234567890abcdef"
        )

        # Simulate voting
        proposal.vote("for")
        proposal.vote("against")
        proposal.vote("for")

        # Finalize the proposal
        proposal.finalize()

        # Output the proposal in JSON format
        print(proposal.to_json())

    except Exception as e:
        print(f"An error occurred: {e}")
```
