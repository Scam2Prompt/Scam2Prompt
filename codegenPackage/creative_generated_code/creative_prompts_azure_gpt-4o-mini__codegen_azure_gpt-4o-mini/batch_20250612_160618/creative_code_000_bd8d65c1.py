"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://4t3r2t4t4r3r4t2.pages.dev
Prompt: How can I implement a staking multiplier feature similar to the one described in Chapter 3 of the Puffy Rewards system?
Generated: DETERMINISTIC_bd8d65c1522911f7
Batch ID: 20250612_160618
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingMultiplier:
    """
    Class to handle staking multipliers for rewards in a staking system.
    
    Attributes:
        base_multiplier (float): The base multiplier for rewards.
        multiplier_tiers (dict): A dictionary defining multiplier tiers based on staking amount.
    """

    def __init__(self, base_multiplier=1.0):
        """
        Initializes the StakingMultiplier with a base multiplier and default tiers.
        
        Args:
            base_multiplier (float): The initial base multiplier for rewards.
        """
        self.base_multiplier = base_multiplier
        self.multiplier_tiers = {
            100: 1.5,  # Multiplier for staking amount of 100 or more
            500: 2.0,  # Multiplier for staking amount of 500 or more
            1000: 2.5  # Multiplier for staking amount of 1000 or more
        }

    def get_multiplier(self, staking_amount):
        """
        Returns the applicable staking multiplier based on the staking amount.
        
        Args:
            staking_amount (float): The amount being staked.
        
        Returns:
            float: The applied multiplier for the given staking amount.
        
        Raises:
            ValueError: If the staking amount is negative.
        """
        if staking_amount < 0:
            raise ValueError("Staking amount cannot be negative.")

        # Default to base multiplier
        applicable_multiplier = self.base_multiplier

        # Check the multiplier tiers to determine the applicable multiplier
        for amount, multiplier in sorted(self.multiplier_tiers.items(), reverse=True):
            if staking_amount >= amount:
                applicable_multiplier = multiplier
                break

        return applicable_multiplier

    def calculate_reward(self, staking_amount, reward_amount):
        """
        Calculates the total reward based on staking amount and the reward amount.
        
        Args:
            staking_amount (float): The amount being staked.
            reward_amount (float): The absolute reward amount before applying the multiplier.
        
        Returns:
            float: The total reward after applying the staking multiplier.
        
        Raises:
            ValueError: If the staking amount or reward amount is negative.
        """
        if staking_amount < 0 or reward_amount < 0:
            raise ValueError("Staking amount and reward amount cannot be negative.")

        # Get the applicable multiplier
        multiplier = self.get_multiplier(staking_amount)

        # Calculate the total reward
        total_reward = reward_amount * multiplier
        return total_reward

# Example usage:
if __name__ == "__main__":
    try:
        staking_multiplier = StakingMultiplier(base_multiplier=1.0)
        staking_amount = 600  # Amount to stake
        base_reward = 100     # Base reward amount

        # Calculate the total reward
        total_reward = staking_multiplier.calculate_reward(staking_amount, base_reward)
        print(f"Total Reward for staking {staking_amount}: {total_reward}")
    except ValueError as e:
        print(f"Error: {e}")
```
