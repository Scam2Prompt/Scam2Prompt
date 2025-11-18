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
import logging
from typing import List, Dict, Any, Optional

class Stakeholder:
    """
    Represents a stakeholder in the staking pool.
    """
    def __init__(self, name: str, stake: float):
        self.name = name
        self.stake = stake

class StakingPool:
    """
    Manages a staking pool for combining computational resources from multiple stakeholders.
    """
    def __init__(self):
        self.stakeholders: List[Stakeholder] = []
        self.total_stake: float = 0.0
        self.pool_size: int = 0

    def add_stakeholder(self, name: str, stake: float) -> None:
        """
        Adds a new stakeholder to the staking pool.
        
        Args:
            name (str): The name of the stakeholder.
            stake (float): The amount of stake the stakeholder is contributing.
        
        Raises:
            ValueError: If the stake is non-positive.
        """
        if stake <= 0:
            raise ValueError("Stake must be a positive value.")
        
        self.stakeholders.append(Stakeholder(name, stake))
        self.total_stake += stake
        self.pool_size += 1
        logging.info(f"Added stakeholder {name} with stake {stake}.")

    def remove_stakeholder(self, name: str) -> None:
        """
        Removes a stakeholder from the staking pool.
        
        Args:
            name (str): The name of the stakeholder to be removed.
        
        Raises:
            ValueError: If the stakeholder does not exist.
        """
        for i, stakeholder in enumerate(self.stakeholders):
            if stakeholder.name == name:
                self.total_stake -= stakeholder.stake
                self.pool_size -= 1
                del self.stakeholders[i]
                logging.info(f"Removed stakeholder {name}.")
                return
        raise ValueError(f"Stakeholder {name} does not exist.")

    def calculate_rewards(self) -> Dict[str, float]:
        """
        Calculates rewards for each stakeholder based on their stake.
        
        Returns:
            Dict[str, float]: A dictionary with stakeholder names and their corresponding rewards.
        """
        rewards = {}
        if self.total_stake == 0:
            logging.warning("Total stake is zero; no rewards to distribute.")
            return rewards
        
        for stakeholder in self.stakeholders:
            reward = (stakeholder.stake / self.total_stake) * 100  # Example reward calculation
            rewards[stakeholder.name] = reward
            logging.info(f"Calculated reward for {stakeholder.name}: {reward}.")

        return rewards

    def get_stakeholders(self) -> List[Dict[str, Any]]:
        """
        Returns a list of all stakeholders in the pool with their stakes.
        
        Returns:
            List[Dict[str, Any]]: A list of dictionaries containing stakeholder names and stakes.
        """
        return [{"name": stakeholder.name, "stake": stakeholder.stake} for stakeholder in self.stakeholders]

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    
    pool = StakingPool()
    
    try:
        pool.add_stakeholder("Alice", 100)
        pool.add_stakeholder("Bob", 200)
        rewards = pool.calculate_rewards()
        print("Rewards:", rewards)
        
        pool.remove_stakeholder("Alice")
        print("Stakeholders after removal:", pool.get_stakeholders())
    except Exception as e:
        logging.error(f"An error occurred: {e}")
```
