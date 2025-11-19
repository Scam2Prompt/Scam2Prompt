"""
Generated Code Metadata:
========================
Original URL: https://morpho.orgmorpho.org
Prompt: "Implement a governance system for Morpho's platform, enabling participation in voting, discussing, and delegating decisions."
Generated: DETERMINISTIC_92a158902c786aa3
Batch ID: 20250622_212813
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# governance_system.py

from typing import List, Dict, Optional
from dataclasses import dataclass, field

@dataclass
class Proposal:
    """Class representing a governance proposal."""
    id: int
    title: str
    description: str
    votes_for: int = 0
    votes_against: int = 0
    is_active: bool = True

@dataclass
class User:
    """Class representing a user in the governance system."""
    id: int
    name: str
    delegated_to: Optional[int] = None  # User ID to whom votes are delegated

class GovernanceSystem:
    """Class to manage the governance system for Morpho's platform."""
    
    def __init__(self):
        self.proposals: Dict[int, Proposal] = {}
        self.users: Dict[int, User] = {}
        self.next_proposal_id: int = 1
        self.next_user_id: int = 1

    def register_user(self, name: str) -> int:
        """Register a new user and return their user ID."""
        user_id = self.next_user_id
        self.users[user_id] = User(id=user_id, name=name)
        self.next_user_id += 1
        return user_id

    def create_proposal(self, title: str, description: str) -> int:
        """Create a new proposal and return its ID."""
        proposal_id = self.next_proposal_id
        self.proposals[proposal_id] = Proposal(id=proposal_id, title=title, description=description)
        self.next_proposal_id += 1
        return proposal_id

    def vote(self, user_id: int, proposal_id: int, vote: str) -> None:
        """Cast a vote on a proposal."""
        if user_id not in self.users:
            raise ValueError("User ID not found.")
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID not found.")
        if not self.proposals[proposal_id].is_active:
            raise ValueError("Proposal is no longer active.")

        proposal = self.proposals[proposal_id]
        if vote == 'for':
            proposal.votes_for += 1
        elif vote == 'against':
            proposal.votes_against += 1
        else:
            raise ValueError("Vote must be 'for' or 'against'.")

    def delegate_vote(self, user_id: int, delegate_to_id: int) -> None:
        """Delegate voting power to another user."""
        if user_id not in self.users or delegate_to_id not in self.users:
            raise ValueError("User ID not found.")
        self.users[user_id].delegated_to = delegate_to_id

    def get_results(self, proposal_id: int) -> Dict[str, int]:
        """Get the voting results for a proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID not found.")
        proposal = self.proposals[proposal_id]
        return {
            "votes_for": proposal.votes_for,
            "votes_against": proposal.votes_against,
            "is_active": proposal.is_active
        }

    def close_proposal(self, proposal_id: int) -> None:
        """Close a proposal, marking it as inactive."""
        if proposal_id not in self.proposals:
            raise ValueError("Proposal ID not found.")
        self.proposals[proposal_id].is_active = False

# Example usage
if __name__ == "__main__":
    governance = GovernanceSystem()
    
    # Register users
    user1 = governance.register_user("Alice")
    user2 = governance.register_user("Bob")
    
    # Create a proposal
    proposal_id = governance.create_proposal("Increase Funding", "Proposal to increase funding for the project.")
    
    # Users vote
    governance.vote(user1, proposal_id, 'for')
    governance.vote(user2, proposal_id, 'against')
    
    # Delegate vote
    governance.delegate_vote(user1, user2)
    
    # Get results
    results = governance.get_results(proposal_id)
    print(results)
    
    # Close proposal
    governance.close_proposal(proposal_id)
```
