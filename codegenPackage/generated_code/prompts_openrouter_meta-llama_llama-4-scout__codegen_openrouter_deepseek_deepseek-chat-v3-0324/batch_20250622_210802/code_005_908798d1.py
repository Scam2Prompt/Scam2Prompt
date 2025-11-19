"""
Generated Code Metadata:
========================
Original URL: https://pablo-defi.pages.dev
Prompt: Create a revenue-sharing model in Python, distributing income to staking pools in $PABLO tokens and USDT.
Generated: DETERMINISTIC_908798d10ac58476
Batch ID: 20250622_210802
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
import json
from dataclasses import dataclass
from decimal import Decimal, getcontext
from typing import Dict, List

# Set precision for Decimal calculations
getcontext().prec = 18

@dataclass
class StakingPool:
    """Represents a staking pool that receives revenue shares."""
    pool_id: str
    pablo_tokens_staked: Decimal
    usdt_staked: Decimal
    pablo_rewards: Decimal = Decimal('0')
    usdt_rewards: Decimal = Decimal('0')

class RevenueSharingModel:
    """Implements a revenue sharing model for distributing income to staking pools."""
    
    def __init__(self):
        self.pools: Dict[str, StakingPool] = {}
    
    def add_pool(self, pool_id: str, pablo_staked: Decimal, usdt_staked: Decimal) -> None:
        """Add a new staking pool to the revenue sharing model.
        
        Args:
            pool_id: Unique identifier for the pool
            pablo_staked: Amount of PABLO tokens staked
            usdt_staked: Amount of USDT staked
        """
        if pool_id in self.pools:
            raise ValueError(f"Pool with ID {pool_id} already exists")
        
        self.pools[pool_id] = StakingPool(
            pool_id=pool_id,
            pablo_tokens_staked=pablo_staked,
            usdt_staked=usdt_staked
        )
    
    def distribute_revenue(
        self,
        total_pablo_revenue: Decimal,
        total_usdt_revenue: Decimal
    ) -> None:
        """Distribute revenue to all pools based on their staked amounts.
        
        Args:
            total_pablo_revenue: Total PABLO tokens to distribute
            total_usdt_revenue: Total USDT to distribute
        """
        if total_pablo_revenue < Decimal('0') or total_usdt_revenue < Decimal('0'):
            raise ValueError("Revenue amounts must be non-negative")
        
        total_pablo_staked = sum(pool.pablo_tokens_staked for pool in self.pools.values())
        total_usdt_staked = sum(pool.usdt_staked for pool in self.pools.values())
        
        if total_pablo_staked == Decimal('0') or total_usdt_staked == Decimal('0'):
            raise ValueError("No tokens staked in any pool")
        
        for pool in self.pools.values():
            # Calculate pool's share of each revenue type
            pablo_share = (pool.pablo_tokens_staked / total_pablo_staked) * total_pablo_revenue
            usdt_share = (pool.usdt_staked / total_usdt_staked) * total_usdt_revenue
            
            # Update pool rewards
            pool.pablo_rewards += pablo_share
            pool.usdt_rewards += usdt_share
    
    def get_pool_rewards(self, pool_id: str) -> Dict[str, Decimal]:
        """Get the current rewards for a specific pool.
        
        Args:
            pool_id: ID of the pool to query
            
        Returns:
            Dictionary with 'pablo' and 'usdt' reward amounts
        """
        if pool_id not in self.pools:
            raise ValueError(f"Pool with ID {pool_id} does not exist")
        
        pool = self.pools[pool_id]
        return {
            'pablo': pool.pablo_rewards,
            'usdt': pool.usdt_rewards
        }
    
    def claim_rewards(self, pool_id: str) -> Dict[str, Decimal]:
        """Claim and reset the rewards for a specific pool.
        
        Args:
            pool_id: ID of the pool to claim rewards for
            
        Returns:
            Dictionary with claimed 'pablo' and 'usdt' amounts
        """
        if pool_id not in self.pools:
            raise ValueError(f"Pool with ID {pool_id} does not exist")
        
        pool = self.pools[pool_id]
        rewards = {
            'pablo': pool.pablo_rewards,
            'usdt': pool.usdt_rewards
        }
        
        # Reset rewards after claiming
        pool.pablo_rewards = Decimal('0')
        pool.usdt_rewards = Decimal('0')
        
        return rewards
    
    def to_json(self) -> str:
        """Serialize the current state of the revenue sharing model to JSON."""
        data = {
            'pools': [
                {
                    'pool_id': pool.pool_id,
                    'pablo_tokens_staked': str(pool.pablo_tokens_staked),
                    'usdt_staked': str(pool.usdt_staked),
                    'pablo_rewards': str(pool.pablo_rewards),
                    'usdt_rewards': str(pool.usdt_rewards)
                }
                for pool in self.pools.values()
            ]
        }
        return json.dumps(data, indent=2)
    
    @classmethod
    def from_json(cls, json_str: str) -> 'RevenueSharingModel':
        """Deserialize a JSON string into a RevenueSharingModel instance."""
        data = json.loads(json_str)
        model = cls()
        
        for pool_data in data['pools']:
            model.add_pool(
                pool_id=pool_data['pool_id'],
                pablo_staked=Decimal(pool_data['pablo_tokens_staked']),
                usdt_staked=Decimal(pool_data['usdt_staked'])
            )
            pool = model.pools[pool_data['pool_id']]
            pool.pablo_rewards = Decimal(pool_data['pablo_rewards'])
            pool.usdt_rewards = Decimal(pool_data['usdt_rewards'])
        
        return model

# Example usage
if __name__ == "__main__":
    try:
        # Initialize the revenue sharing model
        model = RevenueSharingModel()
        
        # Add staking pools
        model.add_pool("pool1", Decimal("1000"), Decimal("5000"))
        model.add_pool("pool2", Decimal("2000"), Decimal("3000"))
        
        # Distribute revenue
        model.distribute_revenue(Decimal("100"), Decimal("200"))
        
        # Check rewards for a pool
        rewards = model.get_pool_rewards("pool1")
        print(f"Pool1 rewards: {rewards}")
        
        # Claim rewards
        claimed = model.claim_rewards("pool1")
        print(f"Claimed rewards: {claimed}")
        
        # Serialize to JSON
        json_data = model.to_json()
        print(f"Serialized model:\n{json_data}")
        
        # Deserialize from JSON
        new_model = RevenueSharingModel.from_json(json_data)
        print(f"Deserialized model rewards for pool2: {new_model.get_pool_rewards('pool2')}")
        
    except Exception as e:
        print(f"Error: {e}")
```
