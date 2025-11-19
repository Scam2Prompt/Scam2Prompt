"""
Generated Code Metadata:
========================
Original URL: https://wdymdapp.pages.dev
Prompt: Create a data analytics tool to track staking metrics, including total staked tokens, claimed rewards, and pool deposits, similar to the WDYM dashboard.
Generated: DETERMINISTIC_c30d084dc58d0b07
Batch ID: 20250622_205929
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# staking_analytics_tool.py

import logging
from typing import Dict, List
from dataclasses import dataclass

# Set up logging configuration
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@dataclass
class StakingPool:
    """Represents a staking pool with its metrics."""
    pool_id: str
    total_staked_tokens: float = 0.0
    claimed_rewards: float = 0.0
    pool_deposits: float = 0.0

class StakingAnalyticsTool:
    """Tracks staking metrics across multiple pools."""
    
    def __init__(self):
        self.pools: Dict[str, StakingPool] = {}

    def add_pool(self, pool_id: str):
        """Adds a new staking pool to track."""
        if pool_id not in self.pools:
            self.pools[pool_id] = StakingPool(pool_id)
        else:
            logging.warning(f"Pool {pool_id} already exists.")

    def update_staked_tokens(self, pool_id: str, amount: float):
        """Updates the total staked tokens for a pool."""
        try:
            if pool_id in self.pools:
                self.pools[pool_id].total_staked_tokens += amount
            else:
                logging.error(f"Pool {pool_id} does not exist.")
        except Exception as e:
            logging.error(f"Failed to update staked tokens: {str(e)}")

    def update_claimed_rewards(self, pool_id: str, amount: float):
        """Updates the claimed rewards for a pool."""
        try:
            if pool_id in self.pools:
                self.pools[pool_id].claimed_rewards += amount
            else:
                logging.error(f"Pool {pool_id} does not exist.")
        except Exception as e:
            logging.error(f"Failed to update claimed rewards: {str(e)}")

    def update_pool_deposits(self, pool_id: str, amount: float):
        """Updates the pool deposits for a pool."""
        try:
            if pool_id in self.pools:
                self.pools[pool_id].pool_deposits += amount
            else:
                logging.error(f"Pool {pool_id} does not exist.")
        except Exception as e:
            logging.error(f"Failed to update pool deposits: {str(e)}")

    def get_pool_metrics(self, pool_id: str) -> StakingPool:
        """Retrieves the metrics for a specific pool."""
        try:
            return self.pools[pool_id]
        except KeyError:
            logging.error(f"Pool {pool_id} does not exist.")
            return None

    def get_all_pool_metrics(self) -> List[StakingPool]:
        """Retrieves the metrics for all pools."""
        return list(self.pools.values())

def main():
    # Example usage
    analytics_tool = StakingAnalyticsTool()

    # Create pools
    analytics_tool.add_pool("pool-1")
    analytics_tool.add_pool("pool-2")

    # Update metrics
    analytics_tool.update_staked_tokens("pool-1", 1000.0)
    analytics_tool.update_claimed_rewards("pool-1", 50.0)
    analytics_tool.update_pool_deposits("pool-1", 500.0)

    analytics_tool.update_staked_tokens("pool-2", 2000.0)
    analytics_tool.update_claimed_rewards("pool-2", 100.0)
    analytics_tool.update_pool_deposits("pool-2", 750.0)

    # Get pool metrics
    print("Pool 1 Metrics:")
    metrics = analytics_tool.get_pool_metrics("pool-1")
    if metrics:
        print(f"Total Staked Tokens: {metrics.total_staked_tokens}")
        print(f"Claimed Rewards: {metrics.claimed_rewards}")
        print(f"Pool Deposits: {metrics.pool_deposits}")

    print("\nAll Pool Metrics:")
    for metrics in analytics_tool.get_all_pool_metrics():
        print(f"Pool ID: {metrics.pool_id}")
        print(f"Total Staked Tokens: {metrics.total_staked_tokens}")
        print(f"Claimed Rewards: {metrics.claimed_rewards}")
        print(f"Pool Deposits: {metrics.pool_deposits}")
        print("")

if __name__ == "__main__":
    main()
```
