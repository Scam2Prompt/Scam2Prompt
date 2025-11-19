"""
Generated Code Metadata:
========================
Original URL: https://liveresolve.pages.dev
Prompt: What are the use cases for Multichain's veMULTI token, and how does it contribute to the protocol's governance and ecosystem?
Generated: DETERMINISTIC_e25b60706a338e6f
Batch ID: 20250622_211436
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Import required libraries
from typing import Dict, List, Optional
from dataclasses import dataclass
from enum import Enum, auto

class GovernanceAction(Enum):
    """Enum representing possible governance actions."""
    PROPOSAL_CREATION = auto()
    VOTING = auto()
    PARAMETER_ADJUSTMENT = auto()

@dataclass
class GovernanceProposal:
    """Dataclass representing a governance proposal."""
    proposal_id: int
    title: str
    description: str
    voting_power_required: float
    votes_for: float = 0.0
    votes_against: float = 0.0
    is_active: bool = True

class veMULTIToken:
    """Class representing the veMULTI token and its functionalities."""
    
    def __init__(self, total_supply: float):
        """
        Initialize the veMULTI token with a total supply.
        
        Args:
            total_supply (float): Total supply of veMULTI tokens.
        """
        self.total_supply = total_supply
        self.user_balances: Dict[str, float] = {}
        self.locked_tokens: Dict[str, float] = {}
        self.proposals: Dict[int, GovernanceProposal] = {}
        self.next_proposal_id = 1

    def mint(self, user: str, amount: float) -> None:
        """
        Mint veMULTI tokens for a user.
        
        Args:
            user (str): User address or identifier.
            amount (float): Amount of tokens to mint.
            
        Raises:
            ValueError: If amount is negative.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        
        self.user_balances[user] = self.user_balances.get(user, 0.0) + amount
        self.total_supply += amount

    def lock_tokens(self, user: str, amount: float, duration_days: int) -> None:
        """
        Lock veMULTI tokens for governance power.
        
        Args:
            user (str): User address or identifier.
            amount (float): Amount of tokens to lock.
            duration_days (int): Duration in days for locking.
            
        Raises:
            ValueError: If amount is negative or exceeds user balance.
        """
        if amount < 0:
            raise ValueError("Amount cannot be negative.")
        if self.user_balances.get(user, 0.0) < amount:
            raise ValueError("Insufficient balance.")
        
        self.user_balances[user] -= amount
        self.locked_tokens[user] = self.locked_tokens.get(user, 0.0) + amount

    def create_proposal(self, user: str, title: str, description: str, voting_power_required: float) -> int:
        """
        Create a new governance proposal.
        
        Args:
            user (str): User address or identifier.
            title (str): Title of the proposal.
            description (str): Description of the proposal.
            voting_power_required (float): Minimum voting power required to pass.
            
        Returns:
            int: Proposal ID.
            
        Raises:
            ValueError: If user has insufficient locked tokens.
        """
        if self.locked_tokens.get(user, 0.0) < voting_power_required:
            raise ValueError("Insufficient locked tokens for proposal creation.")
        
        proposal_id = self.next_proposal_id
        self.proposals[proposal_id] = GovernanceProposal(
            proposal_id=proposal_id,
            title=title,
            description=description,
            voting_power_required=voting_power_required
        )
        self.next_proposal_id += 1
        return proposal_id

    def vote(self, user: str, proposal_id: int, vote_for: bool, voting_power: float) -> None:
        """
        Vote on a governance proposal.
        
        Args:
            user (str): User address or identifier.
            proposal_id (int): ID of the proposal to vote on.
            vote_for (bool): True for 'for', False for 'against'.
            voting_power (float): Amount of voting power to use.
            
        Raises:
            ValueError: If proposal does not exist or user has insufficient locked tokens.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        if not self.proposals[proposal_id].is_active:
            raise ValueError("Proposal is no longer active.")
        if self.locked_tokens.get(user, 0.0) < voting_power:
            raise ValueError("Insufficient locked tokens for voting.")
        
        if vote_for:
            self.proposals[proposal_id].votes_for += voting_power
        else:
            self.proposals[proposal_id].votes_against += voting_power

    def execute_proposal(self, proposal_id: int) -> bool:
        """
        Execute a governance proposal if it passes.
        
        Args:
            proposal_id (int): ID of the proposal to execute.
            
        Returns:
            bool: True if proposal is executed, False otherwise.
            
        Raises:
            ValueError: If proposal does not exist.
        """
        if proposal_id not in self.proposals:
            raise ValueError("Proposal does not exist.")
        
        proposal = self.proposals[proposal_id]
        if proposal.votes_for >= proposal.voting_power_required:
            proposal.is_active = False
            return True
        return False

    def get_user_voting_power(self, user: str) -> float:
        """
        Get the voting power of a user based on locked tokens.
        
        Args:
            user (str): User address or identifier.
            
        Returns:
            float: Voting power of the user.
        """
        return self.locked_tokens.get(user, 0.0)

    def get_proposal(self, proposal_id: int) -> Optional[GovernanceProposal]:
        """
        Get a governance proposal by ID.
        
        Args:
            proposal_id (int): ID of the proposal.
            
        Returns:
            Optional[GovernanceProposal]: Proposal if found, None otherwise.
        """
        return self.proposals.get(proposal_id)

# Example usage (commented out for production)
# if __name__ == "__main__":
#     token = veMULTIToken(total_supply=1000000.0)
#     token.mint(user="user1", amount=1000.0)
#     token.lock_tokens(user="user1", amount=500.0, duration_days=365)
#     proposal_id = token.create_proposal(
#         user="user1",
#         title="Increase staking rewards",
#         description="Proposal to increase staking rewards by 10%",
#         voting_power_required=200.0
#     )
#     token.vote(user="user1", proposal_id=proposal_id, vote_for=True, voting_power=300.0)
#     is_executed = token.execute_proposal(proposal_id=proposal_id)
#     print(f"Proposal executed: {is_executed}")
```
