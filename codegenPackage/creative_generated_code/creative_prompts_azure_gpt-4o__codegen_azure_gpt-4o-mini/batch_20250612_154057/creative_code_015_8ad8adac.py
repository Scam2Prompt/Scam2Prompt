"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ondofoundkation.com
Prompt: Generate a governance voting system for a DAO that oversees tokenized financial products, inspired by Ondo DAO's governance structure.
Generated: DETERMINISTIC_8ad8adac77ff4ba6
Batch ID: 20250612_154057
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import List, Dict, Any
from datetime import datetime, timedelta
import uuid

class Proposal:
    """Class representing a governance proposal."""
    
    def __init__(self, title: str, description: str, duration: int):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.created_at = datetime.utcnow()
        self.expiration = self.created_at + timedelta(days=duration)
        self.votes = {"yes": 0, "no": 0}
        self.voters = set()

    def vote(self, voter_id: str, vote_choice: str) -> bool:
        """Cast a vote on the proposal.
        
        Args:
            voter_id: The ID of the voter.
            vote_choice: The choice of the voter ("yes" or "no").
        
        Returns:
            bool: True if the vote was successfully cast, False otherwise.
        """
        if voter_id in self.voters:
            return False  # Voter has already voted
        
        if vote_choice not in ["yes", "no"]:
            raise ValueError("Vote choice must be 'yes' or 'no'.")

        self.votes[vote_choice] += 1
        self.voters.add(voter_id)
        return True

    def is_active(self) -> bool:
        """Check if the proposal is still active.
        
        Returns:
            bool: True if the proposal is active, False if expired.
        """
        return datetime.utcnow() < self.expiration


class GovernanceDAO:
    """Class representing the DAO governance structure."""

    def __init__(self):
        self.proposals: List[Proposal] = []

    def create_proposal(self, title: str, description: str, duration: int) -> Proposal:
        """Create a new governance proposal.
        
        Args:
            title: The title of the proposal.
            description: A description of the proposal.
            duration: The duration in days until the proposal expires.
        
        Returns:
            Proposal: The created proposal object.
        """
        proposal = Proposal(title, description, duration)
        self.proposals.append(proposal)
        return proposal

    def vote_on_proposal(self, proposal_id: str, voter_id: str, vote_choice: str) -> bool:
        """Vote on a specific proposal.
        
        Args:
            proposal_id: The ID of the proposal to vote on.
            voter_id: The ID of the voter.
            vote_choice: The choice of the voter ("yes" or "no").
        
        Returns:
            bool: True if the vote was successful, False otherwise.
        """
        proposal = self.find_proposal(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found.")
        
        if not proposal.is_active():
            raise ValueError("Proposal voting period has expired.")

        return proposal.vote(voter_id, vote_choice)

    def find_proposal(self, proposal_id: str) -> Any:
        """Find a proposal by its ID.
        
        Args:
            proposal_id: The ID of the proposal to find.
        
        Returns:
            Proposal or None: The found proposal object or None if not found.
        """
        for proposal in self.proposals:
            if proposal.id == proposal_id:
                return proposal
        return None

    def get_results(self, proposal_id: str) -> Dict[str, Any]:
        """Get the results of a proposal.
        
        Args:
            proposal_id: The ID of the proposal for which to get results.
        
        Returns:
            Dict[str, Any]: A dictionary with the proposal's voting results.
        """
        proposal = self.find_proposal(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found.")

        return {
            "title": proposal.title,
            "votes": proposal.votes,
            "active": proposal.is_active()
        }
    
# Example usage:
if __name__ == "__main__":
    dao = GovernanceDAO()
    
    # Create a proposal
    new_proposal = dao.create_proposal(
        title="Increase Token Supply",
        description="Proposal to increase the token supply by 20%.",
        duration=7  # Proposal is active for 7 days
    )
    
    # Voters can cast their votes
    try:
        dao.vote_on_proposal(new_proposal.id, "voter_1", "yes")
        dao.vote_on_proposal(new_proposal.id, "voter_2", "no")
        
        # Retrieve proposal results
        results = dao.get_results(new_proposal.id)
        print(results)
    except ValueError as e:
        print(f"Error: {e}")
```
