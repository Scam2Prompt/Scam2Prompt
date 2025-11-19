"""
Generated Code Metadata:
========================
Original URL: https://gorodshansona.ru
Prompt: "Discuss the role of the IMX token in the Immutable X ecosystem, including its use in governance and the distribution of tokens."
Generated: DETERMINISTIC_af782710dd83e478
Batch ID: 20250622_212320
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
IMX Token Role in Immutable X Ecosystem

This script demonstrates the role of the IMX token in the Immutable X ecosystem,
including governance participation and token distribution mechanisms.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass
import random

@dataclass
class GovernanceProposal:
    """Represents a governance proposal in the Immutable X ecosystem."""
    id: int
    title: str
    description: str
    votes_for: int = 0
    votes_against: int = 0
    status: str = "pending"  # pending, approved, rejected

@dataclass
class User:
    """Represents a user in the Immutable X ecosystem."""
    address: str
    imx_balance: float
    staked_imx: float = 0.0

class ImmutableXEcosystem:
    """Simulates the Immutable X ecosystem and IMX token functionality."""
    
    def __init__(self):
        self.users: Dict[str, User] = {}
        self.proposals: List[GovernanceProposal] = []
        self.total_supply: float = 1_000_000_000  # Example total supply
        self.distributed_tokens: float = 0
    
    def register_user(self, address: str, initial_balance: float = 0) -> None:
        """Register a new user with an initial IMX token balance."""
        if address in self.users:
            raise ValueError("User already registered")
        self.users[address] = User(address=address, imx_balance=initial_balance)
        self.distributed_tokens += initial_balance
    
    def stake_tokens(self, address: str, amount: float) -> None:
        """Stake IMX tokens for governance participation."""
        if address not in self.users:
            raise ValueError("User not registered")
        if amount > self.users[address].imx_balance:
            raise ValueError("Insufficient balance")
        
        self.users[address].imx_balance -= amount
        self.users[address].staked_imx += amount
    
    def unstake_tokens(self, address: str, amount: float) -> None:
        """Unstake IMX tokens."""
        if address not in self.users:
            raise ValueError("User not registered")
        if amount > self.users[address].staked_imx:
            raise ValueError("Insufficient staked amount")
        
        self.users[address].staked_imx -= amount
        self.users[address].imx_balance += amount
    
    def create_proposal(self, title: str, description: str) -> int:
        """Create a new governance proposal."""
        proposal_id = len(self.proposals) + 1
        self.proposals.append(
            GovernanceProposal(
                id=proposal_id,
                title=title,
                description=description
            )
        )
        return proposal_id
    
    def vote_on_proposal(self, address: str, proposal_id: int, vote_for: bool) -> None:
        """Vote on a governance proposal using staked IMX tokens."""
        if address not in self.users:
            raise ValueError("User not registered")
        if self.users[address].staked_imx <= 0:
            raise ValueError("No staked tokens to vote with")
        
        proposal = next((p for p in self.proposals if p.id == proposal_id), None)
        if not proposal:
            raise ValueError("Proposal not found")
        if proposal.status != "pending":
            raise ValueError("Voting closed for this proposal")
        
        voting_power = self.users[address].staked_imx
        if vote_for:
            proposal.votes_for += voting_power
        else:
            proposal.votes_against += voting_power
    
    def distribute_tokens(self, address: str, amount: float) -> None:
        """Distribute IMX tokens to a user (simulating rewards or allocations)."""
        if address not in self.users:
            raise ValueError("User not registered")
        if self.distributed_tokens + amount > self.total_supply:
            raise ValueError("Exceeds total token supply")
        
        self.users[address].imx_balance += amount
        self.distributed_tokens += amount
    
    def get_proposal_status(self, proposal_id: int) -> Optional[GovernanceProposal]:
        """Get the current status of a proposal."""
        return next((p for p in self.proposals if p.id == proposal_id), None)

# Example usage
if __name__ == "__main__":
    ecosystem = ImmutableXEcosystem()
    
    # Register users
    ecosystem.register_user("user1", 1000)
    ecosystem.register_user("user2", 500)
    
    # Stake tokens
    ecosystem.stake_tokens("user1", 500)
    ecosystem.stake_tokens("user2", 200)
    
    # Create proposal
    proposal_id = ecosystem.create_proposal(
        "Protocol Upgrade",
        "Upgrade to version 2.0 with new features"
    )
    
    # Vote on proposal
    ecosystem.vote_on_proposal("user1", proposal_id, True)
    ecosystem.vote_on_proposal("user2", proposal_id, False)
    
    # Distribute tokens (simulating rewards)
    ecosystem.distribute_tokens("user1", 50)
    ecosystem.distribute_tokens("user2", 25)
    
    # Check proposal status
    proposal = ecosystem.get_proposal_status(proposal_id)
    print(f"Proposal {proposal_id} status: For={proposal.votes_for}, Against={proposal.votes_against}")
```
