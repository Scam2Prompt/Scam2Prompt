"""
Generated Code Metadata:
========================
Original URL: https://earns-pupstoken.pages.dev
Prompt: How can I implement a community voting mechanism for a memecoin like $PUPS, based on the principles outlined in the Earns PUPS Token documentation?
Generated: DETERMINISTIC_3b6a80a07d4e0b2a
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from typing import List, Dict, Optional
from datetime import datetime, timedelta
from enum import Enum
import hashlib

# Database simulation (in production, use a real database)
class Database:
    def __init__(self):
        self.proposals = {}
        self.votes = {}
        self.users = {}
        self.token_balances = {}
    
    def get_proposal(self, proposal_id: str) -> Optional[Dict]:
        return self.proposals.get(proposal_id)
    
    def create_proposal(self, proposal_data: Dict) -> str:
        proposal_id = hashlib.sha256(json.dumps(proposal_data).encode()).hexdigest()[:16]
        self.proposals[proposal_id] = proposal_data
        return proposal_id
    
    def record_vote(self, user_id: str, proposal_id: str, vote: str, weight: int):
        if proposal_id not in self.votes:
            self.votes[proposal_id] = {}
        self.votes[proposal_id][user_id] = {"vote": vote, "weight": weight}
    
    def get_user_token_balance(self, user_id: str) -> int:
        return self.token_balances.get(user_id, 0)
    
    def get_proposal_votes(self, proposal_id: str) -> Dict:
        return self.votes.get(proposal_id, {})

# Voting system implementation
class VoteOption(Enum):
    FOR = "FOR"
    AGAINST = "AGAINST"
    ABSTAIN = "ABSTAIN"

class VotingSystem:
    def __init__(self, db: Database):
        self.db = db
        self.min_voting_period = timedelta(days=1)
        self.quorum_percentage = 0.1  # 10% of total supply
        self.majority_percentage = 0.51  # 51% of votes
    
    def create_proposal(
        self,
        title: str,
        description: str,
        creator_id: str,
        voting_period: timedelta = None
    ) -> str:
        """Create a new voting proposal."""
        if not title or not description:
            raise ValueError("Title and description are required")
        
        if voting_period and voting_period < self.min_voting_period:
            raise ValueError(f"Voting period must be at least {self.min_voting_period}")
        
        proposal_data = {
            "title": title,
            "description": description,
            "creator_id": creator_id,
            "created_at": datetime.utcnow().isoformat(),
            "voting_period": (voting_period or self.min_voting_period).total_seconds(),
            "status": "active",
            "total_supply_at_creation": self._get_total_supply()
        }
        
        proposal_id = self.db.create_proposal(proposal_data)
        return proposal_id
    
    def vote(
        self,
        user_id: str,
        proposal_id: str,
        vote: VoteOption,
        token_amount: int = None
    ) -> bool:
        """Cast a vote on a proposal."""
        proposal = self.db.get_proposal(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found")
        
        if proposal["status"] != "active":
            raise ValueError("Voting is closed for this proposal")
        
        if datetime.utcnow() > self._get_voting_end_time(proposal):
            raise ValueError("Voting period has ended")
        
        user_balance = self.db.get_user_token_balance(user_id)
        if user_balance <= 0:
            raise ValueError("User has no voting power")
        
        # Use specified token amount or full balance
        vote_weight = token_amount if token_amount is not None else user_balance
        if vote_weight > user_balance:
            raise ValueError("Cannot vote with more tokens than balance")
        
        self.db.record_vote(user_id, proposal_id, vote.value, vote_weight)
        return True
    
    def tally_votes(self, proposal_id: str) -> Dict:
        """Calculate and return voting results."""
        proposal = self.db.get_proposal(proposal_id)
        if not proposal:
            raise ValueError("Proposal not found")
        
        votes = self.db.get_proposal_votes(proposal_id)
        total_votes = sum(v["weight"] for v in votes.values())
        
        for_votes = sum(v["weight"] for v in votes.values() if v["vote"] == VoteOption.FOR.value)
        against_votes = sum(v["weight"] for v in votes.values() if v["vote"] == VoteOption.AGAINST.value)
        
        total_supply = proposal["total_supply_at_creation"]
        quorum = total_supply * self.quorum_percentage
        
        passed = (
            total_votes >= quorum and 
            for_votes > (for_votes + against_votes) * self.majority_percentage
        )
        
        return {
            "total_votes": total_votes,
            "for_votes": for_votes,
            "against_votes": against_votes,
            "abstain_votes": total_votes - for_votes - against_votes,
            "quorum_required": quorum,
            "quorum_reached": total_votes >= quorum,
            "passed": passed
        }
    
    def _get_voting_end_time(self, proposal: Dict) -> datetime:
        created_at = datetime.fromisoformat(proposal["created_at"])
        return created_at + timedelta(seconds=proposal["voting_period"])
    
    def _get_total_supply(self) -> int:
        # In a real implementation, this would fetch the actual total supply
        return sum(self.db.token_balances.values())

# Example usage
if __name__ == "__main__":
    db = Database()
    
    # Simulate some users and token balances
    db.token_balances = {
        "user1": 1000,
        "user2": 500,
        "user3": 200
    }
    
    voting_system = VotingSystem(db)
    
    # Create a proposal
    proposal_id = voting_system.create_proposal(
        title="Increase token supply",
        description="Proposal to increase total token supply by 10%",
        creator_id="user1",
        voting_period=timedelta(days=2)
    )
    
    # Users vote
    voting_system.vote("user1", proposal_id, VoteOption.FOR)
    voting_system.vote("user2", proposal_id, VoteOption.AGAINST, token_amount=300)
    voting_system.vote("user3", proposal_id, VoteOption.ABSTAIN)
    
    # Get results
    results = voting_system.tally_votes(proposal_id)
    print(json.dumps(results, indent=2))
```
