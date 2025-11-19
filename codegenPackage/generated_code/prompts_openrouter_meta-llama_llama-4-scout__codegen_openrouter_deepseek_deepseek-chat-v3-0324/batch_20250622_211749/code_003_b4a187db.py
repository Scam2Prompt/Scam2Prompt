"""
Generated Code Metadata:
========================
Original URL: https://virtuals-lite.pages.dev
Prompt: Design a co-ownership model for AI agents on Virtuals Protocol, considering shared revenue distribution.
Generated: DETERMINISTIC_b4a187db894f7294
Batch ID: 20250622_211749
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
Virtuals Protocol AI Agent Co-Ownership Model

This module implements a co-ownership model for AI agents on Virtuals Protocol,
including shared revenue distribution among co-owners.
"""

from dataclasses import dataclass
from typing import List, Dict
from decimal import Decimal, getcontext
import hashlib
import json

# Set precision for decimal operations
getcontext().prec = 18

@dataclass
class CoOwner:
    """Represents a co-owner of an AI agent."""
    address: str
    ownership_percentage: Decimal
    revenue_share: Decimal

@dataclass
class RevenueDistribution:
    """Represents a revenue distribution event."""
    amount: Decimal
    distribution: Dict[str, Decimal]  # address -> amount
    timestamp: int
    transaction_hash: str

class AIAgentCoOwnership:
    """Manages co-ownership and revenue distribution for an AI agent."""
    
    def __init__(self, agent_id: str):
        """
        Initialize a new AI agent co-ownership model.
        
        Args:
            agent_id: Unique identifier for the AI agent
        """
        self.agent_id = agent_id
        self.co_owners: List[CoOwner] = []
        self.revenue_distributions: List[RevenueDistribution] = []
        self.total_ownership = Decimal('0')
        self.total_revenue_share = Decimal('0')
        
    def add_co_owner(self, address: str, ownership_percentage: Decimal, revenue_share: Decimal) -> bool:
        """
        Add a new co-owner to the AI agent.
        
        Args:
            address: Wallet address of the co-owner
            ownership_percentage: Percentage of ownership (0-1)
            revenue_share: Percentage of revenue share (0-1)
            
        Returns:
            bool: True if co-owner was added successfully, False otherwise
            
        Raises:
            ValueError: If ownership percentages exceed 100%
        """
        if not (Decimal('0') <= ownership_percentage <= Decimal('1')):
            raise ValueError("Ownership percentage must be between 0 and 1")
            
        if not (Decimal('0') <= revenue_share <= Decimal('1')):
            raise ValueError("Revenue share must be between 0 and 1")
            
        new_total_ownership = self.total_ownership + ownership_percentage
        new_total_revenue = self.total_revenue_share + revenue_share
        
        if new_total_ownership > Decimal('1'):
            raise ValueError("Total ownership cannot exceed 100%")
            
        self.co_owners.append(CoOwner(
            address=address,
            ownership_percentage=ownership_percentage,
            revenue_share=revenue_share
        ))
        
        self.total_ownership = new_total_ownership
        self.total_revenue_share = new_total_revenue
        return True
    
    def distribute_revenue(self, amount: Decimal, timestamp: int, transaction_hash: str) -> RevenueDistribution:
        """
        Distribute revenue to co-owners according to their revenue shares.
        
        Args:
            amount: Total amount to distribute
            timestamp: Unix timestamp of distribution
            transaction_hash: Blockchain transaction hash
            
        Returns:
            RevenueDistribution: The distribution record
            
        Raises:
            ValueError: If amount is negative or no co-owners exist
        """
        if amount <= Decimal('0'):
            raise ValueError("Amount must be positive")
            
        if not self.co_owners:
            raise ValueError("No co-owners to distribute revenue to")
            
        distribution = {}
        remaining_amount = amount
        
        # Calculate each co-owner's share
        for owner in self.co_owners:
            share = amount * owner.revenue_share
            distribution[owner.address] = share
            remaining_amount -= share
        
        # Handle any remaining amount due to rounding
        if remaining_amount > Decimal('0'):
            # Distribute to the first co-owner (could be modified for different strategies)
            distribution[self.co_owners[0].address] += remaining_amount
        
        # Create and store the distribution record
        dist_record = RevenueDistribution(
            amount=amount,
            distribution=distribution,
            timestamp=timestamp,
            transaction_hash=transaction_hash
        )
        
        self.revenue_distributions.append(dist_record)
        return dist_record
    
    def verify_ownership(self, address: str) -> bool:
        """
        Verify if an address is a co-owner of this agent.
        
        Args:
            address: Wallet address to check
            
        Returns:
            bool: True if address is a co-owner, False otherwise
        """
        return any(owner.address == address for owner in self.co_owners)
    
    def get_co_owner_shares(self) -> Dict[str, Dict[str, Decimal]]:
        """
        Get current ownership and revenue shares for all co-owners.
        
        Returns:
            Dict: Mapping of address to ownership and revenue shares
        """
        return {
            owner.address: {
                'ownership': owner.ownership_percentage,
                'revenue': owner.revenue_share
            }
            for owner in self.co_owners
        }
    
    def to_dict(self) -> Dict:
        """
        Serialize the co-ownership model to a dictionary.
        
        Returns:
            Dict: Serialized representation of the model
        """
        return {
            'agent_id': self.agent_id,
            'co_owners': [
                {
                    'address': owner.address,
                    'ownership_percentage': str(owner.ownership_percentage),
                    'revenue_share': str(owner.revenue_share)
                }
                for owner in self.co_owners
            ],
            'total_ownership': str(self.total_ownership),
            'total_revenue_share': str(self.total_revenue_share),
            'revenue_distributions': [
                {
                    'amount': str(dist.amount),
                    'distribution': {k: str(v) for k, v in dist.distribution.items()},
                    'timestamp': dist.timestamp,
                    'transaction_hash': dist.transaction_hash
                }
                for dist in self.revenue_distributions
            ]
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> 'AIAgentCoOwnership':
        """
        Deserialize a dictionary into an AIAgentCoOwnership instance.
        
        Args:
            data: Serialized co-ownership data
            
        Returns:
            AIAgentCoOwnership: Deserialized instance
        """
        instance = cls(data['agent_id'])
        
        for owner_data in data['co_owners']:
            instance.add_co_owner(
                address=owner_data['address'],
                ownership_percentage=Decimal(owner_data['ownership_percentage']),
                revenue_share=Decimal(owner_data['revenue_share'])
            )
        
        for dist_data in data.get('revenue_distributions', []):
            instance.revenue_distributions.append(RevenueDistribution(
                amount=Decimal(dist_data['amount']),
                distribution={k: Decimal(v) for k, v in dist_data['distribution'].items()},
                timestamp=dist_data['timestamp'],
                transaction_hash=dist_data['transaction_hash']
            ))
        
        return instance
    
    def calculate_checksum(self) -> str:
        """
        Calculate a checksum for the current state of the co-ownership model.
        
        Returns:
            str: SHA-256 checksum of the serialized data
        """
        serialized = json.dumps(self.to_dict(), sort_keys=True).encode('utf-8')
        return hashlib.sha256(serialized).hexdigest()
```
