"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://multichainfixsolution.pages.dev
Prompt: Generate code for staking pool management that combines computational resources from multiple stakeholders, as described in the DebugDappNode decentralized ecosystem.
Generated: DETERMINISTIC_0a0c84b525f2a8fe
Batch ID: 20250612_145731
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import threading
from typing import Dict, List

class StakingPool:
    """
    A class to manage a staking pool that combines computational resources 
    from multiple stakeholders in a decentralized ecosystem.
    """
    
    def __init__(self):
        """
        Initialize the staking pool with an empty pool and a lock for
        thread-safety.
        """
        self.pool = {}  # Dictionary to store stakeholder data: {stakeholder_id: resource_amount}
        self.lock = threading.Lock()

    def add_stakeholder(self, stakeholder_id: str, resource_amount: float) -> None:
        """
        Add a stakeholder and their computational resources to the pool.
        
        :param stakeholder_id: Unique identifier for the stakeholder.
        :param resource_amount: Amount of computational resources contributed.
        """
        if resource_amount <= 0:
            raise ValueError("Resource amount must be greater than zero.")
        
        with self.lock:
            if stakeholder_id in self.pool:
                # Increment resource amount if stakeholder already exists
                self.pool[stakeholder_id] += resource_amount
            else:
                self.pool[stakeholder_id] = resource_amount

    def remove_stakeholder(self, stakeholder_id: str) -> None:
        """
        Remove a stakeholder from the pool.
        
        :param stakeholder_id: Unique identifier for the stakeholder.
        """
        with self.lock:
            if stakeholder_id in self.pool:
                del self.pool[stakeholder_id]
            else:
                raise KeyError(f"Stakeholder ID '{stakeholder_id}' not found in the pool.")

    def get_total_resources(self) -> float:
        """
        Calculate the total computational resources in the pool.
        
        :return: Total computational resources as a float.
        """
        with self.lock:
            return sum(self.pool.values())

    def get_stakeholder_share(self, stakeholder_id: str) -> float:
        """
        Get the percentage share of the pool for a stakeholder.
        
        :param stakeholder_id: Unique identifier for the stakeholder.
        :return: Percentage share as a float in the range [0, 100].
        """
        with self.lock:
            if stakeholder_id not in self.pool:
                raise KeyError(f"Stakeholder ID '{stakeholder_id}' not found in the pool.")
            
            total_resources = self.get_total_resources()
            if total_resources == 0:
                return 0.0
            
            stakeholder_resources = self.pool[stakeholder_id]
            return (stakeholder_resources / total_resources) * 100

    def distribute_rewards(self, total_reward: float) -> Dict[str, float]:
        """
        Distribute rewards proportionally to stakeholders based on their share of the pool.
        
        :param total_reward: Total reward to be distributed.
        :return: Dictionary of rewards for each stakeholder: {stakeholder_id: reward_amount}.
        """
        if total_reward < 0:
            raise ValueError("Total reward must be non-negative.")
        
        with self.lock:
            total_resources = self.get_total_resources()
            if total_resources == 0:
                return {stakeholder_id: 0.0 for stakeholder_id in self.pool.keys()}
            
            rewards = {
                stakeholder_id: (resource_amount / total_resources) * total_reward
                for stakeholder_id, resource_amount in self.pool.items()
            }
            return rewards


# Example usage (can be removed in production code)
if __name__ == "__main__":
    # Create a new staking pool
    staking_pool = StakingPool()

    # Add stakeholders
    staking_pool.add_stakeholder("Alice", 100.0)
    staking_pool.add_stakeholder("Bob", 50.0)
    staking_pool.add_stakeholder("Charlie", 150.0)

    # Display total resources
    print(f"Total Resources: {staking_pool.get_total_resources()}")

    # Display stakeholder shares
    print(f"Alice's Share: {staking_pool.get_stakeholder_share('Alice')}%")
    print(f"Bob's Share: {staking_pool.get_stakeholder_share('Bob')}%")
    print(f"Charlie's Share: {staking_pool.get_stakeholder_share('Charlie')}%")

    # Distribute rewards
    rewards = staking_pool.distribute_rewards(1000.0)
    print(f"Rewards: {rewards}")

    # Remove a stakeholder
    staking_pool.remove_stakeholder("Bob")
    print(f"Total Resources after Bob's removal: {staking_pool.get_total_resources()}")
```
