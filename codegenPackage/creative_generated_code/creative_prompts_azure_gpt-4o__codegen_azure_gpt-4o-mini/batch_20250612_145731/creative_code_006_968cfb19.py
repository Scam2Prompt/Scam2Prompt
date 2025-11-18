"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://metazeechain.pages.dev
Prompt: Create a voting mechanism for decentralized community governance, referencing the Community Governance feature on MetazeeChain.
Generated: DETERMINISTIC_968cfb19abd5b050
Batch ID: 20250612_145731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
from typing import Dict, List, Optional
import json

class VotingMechanism:
    def __init__(self):
        """Initialize the voting mechanism with an empty list of proposals and an empty voter registry."""
        self.proposals: List[Dict] = []
        self.voter_registry: Dict[str, bool] = {}  # Keeps track of who has voted

    def create_proposal(self, title: str, description: str) -> None:
        """
        Create a new proposal.

        Args:
            title (str): The title of the proposal.
            description (str): The description of the proposal.

        Raises:
            ValueError: If the title or description is empty.
        """
        if not title or not description:
            raise ValueError("Title and description cannot be empty.")

        proposal = {
            'id': len(self.proposals) + 1,
            'title': title,
            'description': description,
            'votes_for': 0,
            'votes_against': 0,
            'voted_users': set()  # Track users who have voted on this proposal
        }
        self.proposals.append(proposal)

    def vote(self, user_id: str, proposal_id: int, vote: str) -> None:
        """
        Vote on a proposal.

        Args:
            user_id (str): The ID of the user voting.
            proposal_id (int): The ID of the proposal.
            vote (str): The vote type, either "for" or "against".

        Raises:
            ValueError: If the proposal ID is invalid or if the user has already voted.
        """
        # Check if proposal exists
        if proposal_id < 1 or proposal_id > len(self.proposals):
            raise ValueError("Invalid proposal ID.")

        proposal = self.proposals[proposal_id - 1]

        # Check if user has already voted
        if user_id in proposal['voted_users']:
            raise ValueError("User has already voted on this proposal.")

        # Process the vote
        if vote.lower() == "for":
            proposal['votes_for'] += 1
        elif vote.lower() == "against":
            proposal['votes_against'] += 1
        else:
            raise ValueError("Vote must be either 'for' or 'against'.")

        # Mark user as having voted
        proposal['voted_users'].add(user_id)

    def get_results(self, proposal_id: int) -> Optional[Dict]:
        """
        Get the voting results for a proposal.

        Args:
            proposal_id (int): The ID of the proposal.

        Returns:
            Optional[Dict]: A dictionary containing the results of the proposal or None if not found.
        """
        if proposal_id < 1 or proposal_id > len(self.proposals):
            return None
        
        proposal = self.proposals[proposal_id - 1]
        return {
            'title': proposal['title'],
            'votes_for': proposal['votes_for'],
            'votes_against': proposal['votes_against'],
            'total_votes': proposal['votes_for'] + proposal['votes_against']
        }

    def to_json(self) -> str:
        """Convert the current state of proposals to a JSON string."""
        return json.dumps(self.proposals, indent=4)

# Example usage
if __name__ == "__main__":
    voting = VotingMechanism()
    
    # Create proposals
    voting.create_proposal("Increase Budget", "Proposal to increase the community budget by 20%.")
    voting.create_proposal("Community Event", "Proposal to hold a community event next month.")
    
    # Users vote
    try:
        voting.vote("user1", 1, "for")
        voting.vote("user2", 1, "against")
        voting.vote("user1", 2, "for")  # user1 votes on a different proposal
    except ValueError as e:
        print(f"Error: {e}")

    # Get results
    results = voting.get_results(1)
    print("Results for Proposal 1:", results)

    # Export to JSON
    print("Voting State JSON:", voting.to_json())
```
