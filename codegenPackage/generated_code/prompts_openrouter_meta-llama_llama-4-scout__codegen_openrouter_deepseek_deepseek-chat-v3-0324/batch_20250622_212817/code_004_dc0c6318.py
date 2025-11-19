"""
Generated Code Metadata:
========================
Original URL: https://thegraph-the-graph.org
Prompt: "Design a system for incentivizing network participants in a decentralized data indexing protocol using a native token like GRT."
Generated: DETERMINISTIC_dc0c63188eea7ee5
Batch ID: 20250622_212817
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
Decentralized Data Indexing Protocol Incentive System

This module implements a token-based incentive system for network participants
in a decentralized data indexing protocol using a native token (GRT).
"""

from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum, auto
import math
from datetime import datetime, timedelta

# Constants
TOKEN_DECIMALS = 18
INITIAL_TOKEN_SUPPLY = 10_000_000_000 * (10 ** TOKEN_DECIMALS)  # 10B GRT
ANNUAL_INFLATION_RATE = 0.03  # 3%
BLOCK_TIME_SECONDS = 15
EPOCH_DURATION_BLOCKS = 20_160  # ~1 week

class ParticipantType(Enum):
    INDEXER = auto()
    CURATOR = auto()
    DELEGATOR = auto()
    FISHERMAN = auto()

@dataclass
class Participant:
    address: str
    participant_type: ParticipantType
    stake: int = 0
    rewards: int = 0
    last_active_epoch: int = 0

@dataclass
class Allocation:
    allocation_id: str
    indexer: str
    amount: int
    created_at_epoch: int
    closed_at_epoch: Optional[int] = None

class IncentiveSystem:
    def __init__(self):
        self.participants: Dict[str, Participant] = {}
        self.allocations: Dict[str, Allocation] = {}
        self.total_staked: int = 0
        self.current_epoch: int = 0
        self.token_supply: int = INITIAL_TOKEN_SUPPLY
        self.epoch_start_timestamp: datetime = datetime.utcnow()
        
    def register_participant(self, address: str, participant_type: ParticipantType) -> None:
        """Register a new network participant."""
        if address in self.participants:
            raise ValueError("Participant already registered")
        
        self.participants[address] = Participant(
            address=address,
            participant_type=participant_type
        )
    
    def stake_tokens(self, address: str, amount: int) -> None:
        """Stake tokens to participate in the network."""
        if address not in self.participants:
            raise ValueError("Participant not registered")
        
        participant = self.participants[address]
        participant.stake += amount
        self.total_staked += amount
    
    def unstake_tokens(self, address: str, amount: int) -> None:
        """Unstake tokens from the network."""
        if address not in self.participants:
            raise ValueError("Participant not registered")
        
        participant = self.participants[address]
        if participant.stake < amount:
            raise ValueError("Insufficient stake")
        
        participant.stake -= amount
        self.total_staked -= amount
    
    def create_allocation(self, indexer: str, amount: int) -> str:
        """Create a new allocation for indexing work."""
        if indexer not in self.participants:
            raise ValueError("Indexer not registered")
        if self.participants[indexer].participant_type != ParticipantType.INDEXER:
            raise ValueError("Only indexers can create allocations")
        if self.participants[indexer].stake < amount:
            raise ValueError("Insufficient stake")
        
        allocation_id = f"alloc-{len(self.allocations)+1}"
        self.allocations[allocation_id] = Allocation(
            allocation_id=allocation_id,
            indexer=indexer,
            amount=amount,
            created_at_epoch=self.current_epoch
        )
        return allocation_id
    
    def close_allocation(self, allocation_id: str) -> None:
        """Close an allocation and distribute rewards."""
        if allocation_id not in self.allocations:
            raise ValueError("Allocation not found")
        
        allocation = self.allocations[allocation_id]
        if allocation.closed_at_epoch is not None:
            raise ValueError("Allocation already closed")
        
        allocation.closed_at_epoch = self.current_epoch
        epochs_active = self.current_epoch - allocation.created_at_epoch
        rewards = self._calculate_allocation_rewards(allocation.amount, epochs_active)
        
        # Distribute rewards (70% to indexer, 30% to delegators)
        indexer_reward = rewards * 7 // 10
        delegator_reward = rewards - indexer_reward
        
        self.participants[allocation.indexer].rewards += indexer_reward
        self._distribute_delegator_rewards(allocation.indexer, delegator_reward)
    
    def _calculate_allocation_rewards(self, stake: int, epochs_active: int) -> int:
        """Calculate rewards for an allocation based on stake and activity."""
        if self.total_staked == 0:
            return 0
        
        # Base reward rate per epoch
        annual_rewards = self.token_supply * ANNUAL_INFLATION_RATE
        epoch_rewards = annual_rewards * EPOCH_DURATION_BLOCKS * BLOCK_TIME_SECONDS / (365 * 24 * 3600)
        
        # Proportional reward based on stake
        stake_ratio = stake / self.total_staked
        return int(epoch_rewards * stake_ratio * epochs_active)
    
    def _distribute_delegator_rewards(self, indexer: str, total_reward: int) -> None:
        """Distribute rewards to delegators proportional to their stake."""
        # Simplified implementation - in production would track delegation shares
        pass
    
    def advance_epoch(self) -> None:
        """Advance to the next epoch and update system state."""
        self.current_epoch += 1
        self.epoch_start_timestamp += timedelta(
            seconds=EPOCH_DURATION_BLOCKS * BLOCK_TIME_SECONDS
        )
        
        # Update token supply with inflation
        self.token_supply += int(self.token_supply * ANNUAL_INFLATION_RATE / (365 * 24 * 3600 / (EPOCH_DURATION_BLOCKS * BLOCK_TIME_SECONDS)))
    
    def claim_rewards(self, address: str) -> int:
        """Claim accumulated rewards for a participant."""
        if address not in self.participants:
            raise ValueError("Participant not registered")
        
        participant = self.participants[address]
        claimed = participant.rewards
        participant.rewards = 0
        return claimed
    
    def slash(self, address: str, amount: int) -> None:
        """Slash a participant's stake for misbehavior."""
        if address not in self.participants:
            raise ValueError("Participant not registered")
        
        participant = self.participants[address]
        if participant.stake < amount:
            amount = participant.stake  # Slash entire stake if insufficient
        
        participant.stake -= amount
        self.total_staked -= amount

# Example usage
if __name__ == "__main__":
    system = IncentiveSystem()
    
    # Register participants
    system.register_participant("indexer1", ParticipantType.INDEXER)
    system.register_participant("delegator1", ParticipantType.DELEGATOR)
    
    # Stake tokens
    system.stake_tokens("indexer1", 100_000 * (10 ** TOKEN_DECIMALS))
    system.stake_tokens("delegator1", 50_000 * (10 ** TOKEN_DECIMALS))
    
    # Create and close allocation
    alloc_id = system.create_allocation("indexer1", 10_000 * (10 ** TOKEN_DECIMALS))
    system.advance_epoch()
    system.close_allocation(alloc_id)
    
    # Claim rewards
    rewards = system.claim_rewards("indexer1")
    print(f"Indexer rewards claimed: {rewards / (10 ** TOKEN_DECIMALS)} GRT")
```
