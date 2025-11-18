"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aitech-c09.pages.dev
Prompt: Write a script to automate the calculation of rewards earned in staking pools with varying lock terms and tier boosts, using the AITECH staking model as a reference.
Generated: DETERMINISTIC_af3ba2c4469f8bf7
Batch ID: 20250612_152620
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import json
from typing import List, Dict

class StakingPool:
    def __init__(self, pool_name: str, lock_term: int, tier_boost: float, base_reward_rate: float):
        """
        Initialize a staking pool with the given parameters.
        
        :param pool_name: Name of the staking pool.
        :param lock_term: Duration of the lock in days.
        :param tier_boost: Multiplier for the base reward rate based on the tier.
        :param base_reward_rate: The base reward rate in percentage.
        """
        self.pool_name = pool_name
        self.lock_term = lock_term
        self.tier_boost = tier_boost
        self.base_reward_rate = base_reward_rate

    def calculate_rewards(self, amount_staked: float) -> float:
        """
        Calculate the rewards earned for a specific amount staked.

        :param amount_staked: The amount of tokens staked in the pool.
        :return: The total rewards earned.
        """
        if amount_staked < 0:
            raise ValueError("Amount staked cannot be negative.")
        # Calculate the final reward rate by applying the tier boost
        final_reward_rate = self.base_reward_rate * self.tier_boost
        # Calculate rewards based on the lock term and staked amount
        rewards = (amount_staked * final_reward_rate / 100) * (self.lock_term / 365)  # Annualized
        return rewards

def load_staking_pools(file_path: str) -> List[StakingPool]:
    """
    Load staking pools configuration from a JSON file.

    :param file_path: The path to the JSON configuration file.
    :return: A list of StakingPool objects.
    """
    try:
        with open(file_path, 'r') as file:
            pools_data = json.load(file)
            pools = [
                StakingPool(
                    pool['pool_name'],
                    pool['lock_term'],
                    pool['tier_boost'],
                    pool['base_reward_rate']
                )
                for pool in pools_data
            ]
            return pools
    except FileNotFoundError:
        raise FileNotFoundError(f"Configuration file not found: {file_path}")
    except json.JSONDecodeError:
        raise ValueError("Error decoding JSON from the configuration file.")
    except KeyError as e:
        raise KeyError(f"Missing expected key in configuration: {e}")

def main():
    """
    Main function to execute the staking rewards calculation.
    """
    # Load staking pools from a configuration file
    file_path = 'staking_pools.json'
    try:
        staking_pools = load_staking_pools(file_path)
        
        # Example amount staked for demonstration
        amount_staked = 1000.0  # Adjust as necessary
        
        for pool in staking_pools:
            rewards = pool.calculate_rewards(amount_staked)
            print(f"Rewards for pool '{pool.pool_name}' with lock term {pool.lock_term} days: {rewards:.2f}")
    
    except Exception as error:
        print(f"An error occurred: {error}")

if __name__ == "__main__":
    main()
```

**Example JSON Configuration (staking_pools.json):**
```json
[
    {
        "pool_name": "Basic Pool",
        "lock_term": 30,
        "tier_boost": 1.0,
        "base_reward_rate": 5.0
    },
    {
        "pool_name": "Premium Pool",
        "lock_term": 90,
        "tier_boost": 1.5,
        "base_reward_rate": 7.0
    }
]
```
