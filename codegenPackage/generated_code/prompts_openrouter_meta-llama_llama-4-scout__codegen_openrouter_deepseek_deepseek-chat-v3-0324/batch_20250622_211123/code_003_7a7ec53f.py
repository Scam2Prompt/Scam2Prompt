"""
Generated Code Metadata:
========================
Original URL: https://gifts-usualdao.com
Prompt: Design a revenue allocation system, similar to Usual's revenue switch, that ensures token emissions lag behind revenue growth, and describe how to implement it using a decentralized governance model.
Generated: DETERMINISTIC_7a7ec53f5722816a
Batch ID: 20250622_211123
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# SPDX-License-Identifier: MIT
"""
Revenue Allocation System with Decentralized Governance

Implements a revenue allocation system where token emissions lag behind revenue growth.
Uses a decentralized governance model for parameter adjustments.
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
import math
import time

# Constants
DEFAULT_EMISSION_LAG_FACTOR = 0.8  # Token emissions grow at 80% of revenue growth rate
MIN_EMISSION_RATE = 0.01  # Minimum token emission rate (1%)
MAX_EMISSION_RATE = 0.20  # Maximum token emission rate (20%)
GOVERNANCE_VOTING_PERIOD = 7 * 24 * 60 * 60  # 7 days in seconds
QUORUM_THRESHOLD = 0.30  # 30% of total tokens must participate
APPROVAL_THRESHOLD = 0.60  # 60% approval required for proposals

@dataclass
class RevenueSnapshot:
    timestamp: int
    amount: float
    emission_rate: float

@dataclass
class GovernanceProposal:
    id: int
    proposer: str
    description: str
    parameter: str
    new_value: float
    votes_for: float
    votes_against: float
    created_at: int
    executed: bool

class RevenueAllocator:
    def __init__(self, governance_token: 'GovernanceToken'):
        self.revenue_history: List[RevenueSnapshot] = []
        self.current_emission_rate = MIN_EMISSION_RATE
        self.governance_token = governance_token
        self.proposals: Dict[int, GovernanceProposal] = {}
        self.next_proposal_id = 1

    def record_revenue(self, amount: float) -> None:
        """Record new revenue and adjust emission rate based on growth."""
        if amount <= 0:
            raise ValueError("Revenue amount must be positive")

        current_time = int(time.time())
        new_emission_rate = self._calculate_emission_rate(amount)
        
        snapshot = RevenueSnapshot(
            timestamp=current_time,
            amount=amount,
            emission_rate=new_emission_rate
        )
        self.revenue_history.append(snapshot)
        self.current_emission_rate = new_emission_rate

    def _calculate_emission_rate(self, new_revenue: float) -> float:
        """Calculate new emission rate based on revenue growth."""
        if not self.revenue_history:
            return MIN_EMISSION_RATE

        last_revenue = self.revenue_history[-1].amount
        revenue_growth = (new_revenue - last_revenue) / last_revenue
        
        # Apply lag factor to revenue growth
        emission_growth = revenue_growth * DEFAULT_EMISSION_LAG_FACTOR
        new_rate = self.current_emission_rate * (1 + emission_growth)
        
        # Enforce bounds
        return min(max(new_rate, MIN_EMISSION_RATE), MAX_EMISSION_RATE)

    def create_proposal(
        self,
        proposer: str,
        description: str,
        parameter: str,
        new_value: float
    ) -> int:
        """Create a new governance proposal."""
        valid_parameters = {'emission_lag_factor', 'min_emission_rate', 'max_emission_rate'}
        if parameter not in valid_parameters:
            raise ValueError(f"Invalid parameter. Must be one of: {valid_parameters}")

        proposal = GovernanceProposal(
            id=self.next_proposal_id,
            proposer=proposer,
            description=description,
            parameter=parameter,
            new_value=new_value,
            votes_for=0,
            votes_against=0,
            created_at=int(time.time()),
            executed=False
        )
        
        self.proposals[self.next_proposal_id] = proposal
        self.next_proposal_id += 1
        return proposal.id

    def vote_on_proposal(self, proposal_id: int, voter: str, support: bool, voting_power: float) -> None:
        """Cast a vote on a governance proposal."""
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID")
        
        proposal = self.proposals[proposal_id]
        
        # Check if voting period is still active
        if (time.time() - proposal.created_at) > GOVERNANCE_VOTING_PERIOD:
            raise ValueError("Voting period has ended")
        
        if support:
            proposal.votes_for += voting_power
        else:
            proposal.votes_against += voting_power

    def execute_proposal(self, proposal_id: int) -> None:
        """Execute a proposal if it meets requirements."""
        if proposal_id not in self.proposals:
            raise ValueError("Invalid proposal ID")
        
        proposal = self.proposals[proposal_id]
        
        # Check if already executed
        if proposal.executed:
            raise ValueError("Proposal already executed")
        
        # Check voting period has ended
        if (time.time() - proposal.created_at) <= GOVERNANCE_VOTING_PERIOD:
            raise ValueError("Voting period has not ended")
        
        total_votes = proposal.votes_for + proposal.votes_against
        total_supply = self.governance_token.total_supply()
        
        # Check quorum
        if total_votes < total_supply * QUORUM_THRESHOLD:
            raise ValueError("Quorum not reached")
        
        # Check approval threshold
        if proposal.votes_for / total_votes < APPROVAL_THRESHOLD:
            raise ValueError("Approval threshold not met")
        
        # Execute the proposal
        if proposal.parameter == 'emission_lag_factor':
            global DEFAULT_EMISSION_LAG_FACTOR
            DEFAULT_EMISSION_LAG_FACTOR = proposal.new_value
        elif proposal.parameter == 'min_emission_rate':
            global MIN_EMISSION_RATE
            MIN_EMISSION_RATE = proposal.new_value
        elif proposal.parameter == 'max_emission_rate':
            global MAX_EMISSION_RATE
            MAX_EMISSION_RATE = proposal.new_value
        
        proposal.executed = True

class GovernanceToken:
    def __init__(self):
        self.total_supply_: float = 1_000_000  # Initial supply
        self.balances: Dict[str, float] = {}
    
    def total_supply(self) -> float:
        return self.total_supply_
    
    def balance_of(self, address: str) -> float:
        return self.balances.get(address, 0)
    
    def transfer(self, from_address: str, to_address: str, amount: float) -> None:
        if self.balance_of(from_address) < amount:
            raise ValueError("Insufficient balance")
        
        self.balances[from_address] = self.balance_of(from_address) - amount
        self.balances[to_address] = self.balance_of(to_address) + amount

# Example usage
if __name__ == "__main__":
    # Initialize governance token and allocator
    token = GovernanceToken()
    allocator = RevenueAllocator(token)
    
    # Simulate revenue recording
    allocator.record_revenue(1000)
    allocator.record_revenue(1200)  # 20% growth
    
    # Create and vote on a proposal
    proposal_id = allocator.create_proposal(
        proposer="0x123...",
        description="Increase max emission rate to 25%",
        parameter="max_emission_rate",
        new_value=0.25
    )
    
    # Simulate voting
    try:
        allocator.vote_on_proposal(proposal_id, "0x456...", True, 200000)
        allocator.vote_on_proposal(proposal_id, "0x789...", False, 100000)
        
        # Wait for voting period to end (in real usage)
        # Then execute
        allocator.execute_proposal(proposal_id)
    except ValueError as e:
        print(f"Proposal failed: {e}")
```
