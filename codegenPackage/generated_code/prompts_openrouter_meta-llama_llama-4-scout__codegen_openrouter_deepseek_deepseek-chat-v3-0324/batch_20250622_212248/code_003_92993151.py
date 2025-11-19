"""
Generated Code Metadata:
========================
Original URL: https://curatesai.vip
Prompt: Design a tokenomics system for a cryptocurrency content platform, including token allocation, utility, and governance mechanisms.
Generated: DETERMINISTIC_92993151b28cafd9
Batch ID: 20250622_212248
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# Tokenomics System for Cryptocurrency Content Platform

import math
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum, auto

class TokenAllocationCategory(Enum):
    """Categories for token allocation"""
    COMMUNITY_REWARDS = auto()
    TEAM = auto()
    ADVISORS = auto()
    ECOSYSTEM_DEVELOPMENT = auto()
    LIQUIDITY = auto()
    TREASURY = auto()

@dataclass
class TokenAllocation:
    """Represents a token allocation with category and percentage"""
    category: TokenAllocationCategory
    percentage: float
    vesting_period: Optional[int] = None  # in months
    cliff_period: Optional[int] = None    # in months

class TokenUtility(Enum):
    """Utility functions of the token"""
    CONTENT_CREATION = auto()
    CONTENT_CURATION = auto()
    STAKING = auto()
    GOVERNANCE = auto()
    PLATFORM_FEES = auto()
    PREMIUM_ACCESS = auto()

class GovernanceProposalType(Enum):
    """Types of governance proposals"""
    PARAMETER_CHANGE = auto()
    FUNDING_REQUEST = auto()
    PROTOCOL_UPGRADE = auto()
    EMERGENCY = auto()

@dataclass
class GovernanceProposal:
    """Represents a governance proposal"""
    proposal_id: int
    proposal_type: GovernanceProposalType
    title: str
    description: str
    voting_period: int  # in days
    voting_threshold: float  # percentage of tokens needed to pass
    created_by: str
    created_at: int  # timestamp

class TokenomicsSystem:
    """Implements tokenomics for cryptocurrency content platform"""
    
    def __init__(self, total_supply: int):
        self.total_supply = total_supply
        self.allocations: Dict[TokenAllocationCategory, TokenAllocation] = {}
        self.token_utilities: List[TokenUtility] = []
        self.governance_proposals: List[GovernanceProposal] = []
        self.next_proposal_id = 1
        
    def add_allocation(self, allocation: TokenAllocation) -> None:
        """Add a token allocation category"""
        if sum(a.percentage for a in self.allocations.values()) + allocation.percentage > 100:
            raise ValueError("Total allocation cannot exceed 100%")
        self.allocations[allocation.category] = allocation
    
    def calculate_allocation_amount(self, category: TokenAllocationCategory) -> int:
        """Calculate the token amount for a given allocation category"""
        if category not in self.allocations:
            raise ValueError(f"Category {category} not found in allocations")
        return math.floor(self.total_supply * self.allocations[category].percentage / 100)
    
    def add_token_utility(self, utility: TokenUtility) -> None:
        """Add a token utility function"""
        if utility not in self.token_utilities:
            self.token_utilities.append(utility)
    
    def has_utility(self, utility: TokenUtility) -> bool:
        """Check if token has a specific utility"""
        return utility in self.token_utilities
    
    def create_governance_proposal(
        self,
        proposal_type: GovernanceProposalType,
        title: str,
        description: str,
        voting_period: int,
        voting_threshold: float,
        creator: str,
        timestamp: int
    ) -> GovernanceProposal:
        """Create a new governance proposal"""
        proposal = GovernanceProposal(
            proposal_id=self.next_proposal_id,
            proposal_type=proposal_type,
            title=title,
            description=description,
            voting_period=voting_period,
            voting_threshold=voting_threshold,
            created_by=creator,
            created_at=timestamp
        )
        self.governance_proposals.append(proposal)
        self.next_proposal_id += 1
        return proposal
    
    def get_proposal(self, proposal_id: int) -> GovernanceProposal:
        """Retrieve a governance proposal by ID"""
        for proposal in self.governance_proposals:
            if proposal.proposal_id == proposal_id:
                return proposal
        raise ValueError(f"Proposal with ID {proposal_id} not found")
    
    def calculate_voting_power(self, token_balance: float, staked_tokens: float) -> float:
        """Calculate voting power based on token balance and staked tokens"""
        return token_balance + (staked_tokens * 1.5)  # Staked tokens have 1.5x voting power
    
    def check_proposal_pass(self, votes_for: float, votes_against: float, threshold: float) -> bool:
        """Check if a proposal passes based on votes and threshold"""
        total_votes = votes_for + votes_against
        if total_votes == 0:
            return False
        return (votes_for / total_votes) >= threshold

# Example usage
if __name__ == "__main__":
    # Initialize tokenomics system with 1 billion tokens
    tokenomics = TokenomicsSystem(total_supply=1_000_000_000)
    
    # Set token allocations
    tokenomics.add_allocation(TokenAllocation(
        category=TokenAllocationCategory.COMMUNITY_REWARDS,
        percentage=40,
        vesting_period=36,
        cliff_period=12
    ))
    tokenomics.add_allocation(TokenAllocation(
        category=TokenAllocationCategory.TEAM,
        percentage=15,
        vesting_period=48,
        cliff_period=12
    ))
    tokenomics.add_allocation(TokenAllocation(
        category=TokenAllocationCategory.ADVISORS,
        percentage=5,
        vesting_period=24,
        cliff_period=6
    ))
    tokenomics.add_allocation(TokenAllocation(
        category=TokenAllocationCategory.ECOSYSTEM_DEVELOPMENT,
        percentage=20,
        vesting_period=36
    ))
    tokenomics.add_allocation(TokenAllocation(
        category=TokenAllocationCategory.LIQUIDITY,
        percentage=10,
        vesting_period=6
    ))
    tokenomics.add_allocation(TokenAllocation(
        category=TokenAllocationCategory.TREASURY,
        percentage=10
    ))
    
    # Add token utilities
    tokenomics.add_token_utility(TokenUtility.CONTENT_CREATION)
    tokenomics.add_token_utility(TokenUtility.CONTENT_CURATION)
    tokenomics.add_token_utility(TokenUtility.STAKING)
    tokenomics.add_token_utility(TokenUtility.GOVERNANCE)
    tokenomics.add_token_utility(TokenUtility.PLATFORM_FEES)
    tokenomics.add_token_utility(TokenUtility.PREMIUM_ACCESS)
    
    # Create a governance proposal
    proposal = tokenomics.create_governance_proposal(
        proposal_type=GovernanceProposalType.PARAMETER_CHANGE,
        title="Adjust staking rewards",
        description="Proposal to increase staking rewards by 2%",
        voting_period=7,
        voting_threshold=0.6,
        creator="0xCreatorAddress",
        timestamp=1234567890
    )
    
    # Simulate voting
    votes_for = 500_000  # tokens voting for
    votes_against = 300_000  # tokens voting against
    threshold = 0.6
    
    # Check if proposal passes
    passed = tokenomics.check_proposal_pass(votes_for, votes_against, threshold)
    print(f"Proposal passed: {passed}")
```
