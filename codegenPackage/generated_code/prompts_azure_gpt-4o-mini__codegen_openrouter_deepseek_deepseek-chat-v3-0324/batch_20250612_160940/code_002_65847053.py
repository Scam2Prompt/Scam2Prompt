"""
Generated Code Metadata:
========================
Original URL: https://bafybeifzsc2fqkmtu3f77p3b3xr5mea4rugk5sb3zsww46ufwpltulpw3u.ipfs.dweb.link
Prompt: Create a function that simulates the allocation of the $SOPH token supply for node operators, including the 3-month lock-up period for rewards.
Generated: DETERMINISTIC_658470538e7ace88
Batch ID: 20250612_160940
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import time
from dataclasses import dataclass
from typing import List, Dict
from datetime import datetime, timedelta

@dataclass
class NodeOperator:
    """Represents a node operator with their allocation details."""
    id: str
    initial_allocation: float  # Initial SOPH tokens allocated
    reward_allocation: float   # SOPH tokens allocated as rewards
    lockup_end: datetime = None  # When rewards become claimable

class SophTokenAllocator:
    """Manages the allocation and distribution of SOPH tokens to node operators."""
    
    def __init__(self, total_supply: float):
        """
        Initialize the allocator with total token supply.
        
        Args:
            total_supply: Total number of SOPH tokens to be allocated
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be positive")
            
        self.total_supply = total_supply
        self.allocated = 0.0
        self.node_operators: Dict[str, NodeOperator] = {}
        
    def add_node_operator(self, operator_id: str, allocation_percent: float, reward_percent: float) -> NodeOperator:
        """
        Register a new node operator with their allocation percentages.
        
        Args:
            operator_id: Unique identifier for the operator
            allocation_percent: Percentage of total supply allocated initially (0-100)
            reward_percent: Percentage of initial allocation given as rewards (0-100)
            
        Returns:
            The created NodeOperator instance
            
        Raises:
            ValueError: If percentages are invalid or total allocation exceeds supply
        """
        if not (0 <= allocation_percent <= 100):
            raise ValueError("Allocation percent must be between 0 and 100")
        if not (0 <= reward_percent <= 100):
            raise ValueError("Reward percent must be between 0 and 100")
            
        initial_allocation = (self.total_supply * allocation_percent) / 100
        reward_allocation = (initial_allocation * reward_percent) / 100
        
        if self.allocated + initial_allocation > self.total_supply:
            raise ValueError("Total allocation would exceed token supply")
            
        lockup_end = datetime.now() + timedelta(days=90)  # 3-month lockup
        
        operator = NodeOperator(
            id=operator_id,
            initial_allocation=initial_allocation,
            reward_allocation=reward_allocation,
            lockup_end=lockup_end
        )
        
        self.node_operators[operator_id] = operator
        self.allocated += initial_allocation
        
        return operator
        
    def claim_rewards(self, operator_id: str) -> float:
        """
        Attempt to claim rewards for a node operator.
        
        Args:
            operator_id: ID of the operator claiming rewards
            
        Returns:
            Amount of rewards claimed (0 if lockup hasn't ended)
            
        Raises:
            KeyError: If operator ID doesn't exist
        """
        operator = self.node_operators.get(operator_id)
        if not operator:
            raise KeyError(f"Operator {operator_id} not found")
            
        if datetime.now() < operator.lockup_end:
            return 0.0
            
        claimed = operator.reward_allocation
        operator.reward_allocation = 0.0  # Mark as claimed
        
        return claimed
        
    def get_operator_info(self, operator_id: str) -> dict:
        """
        Get allocation information for a specific operator.
        
        Args:
            operator_id: ID of the operator to query
            
        Returns:
            Dictionary with operator's allocation details
            
        Raises:
            KeyError: If operator ID doesn't exist
        """
        operator = self.node_operators.get(operator_id)
        if not operator:
            raise KeyError(f"Operator {operator_id} not found")
            
        return {
            "id": operator.id,
            "initial_allocation": operator.initial_allocation,
            "reward_allocation": operator.reward_allocation,
            "lockup_end": operator.lockup_end,
            "can_claim": datetime.now() >= operator.lockup_end
        }
        
    def get_total_allocated(self) -> float:
        """Return the total amount of tokens allocated so far."""
        return self.allocated
        
    def get_remaining_supply(self) -> float:
        """Return the remaining unallocated token supply."""
        return self.total_supply - self.allocated
```
