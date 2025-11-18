"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://web-tpad.pages.dev
Prompt: Generate Python code to calculate staking rewards based on TrustPad's staking levels and pool weights for $TPAD tokens.
Generated: DETERMINISTIC_7dcf1b9f753cbe15
Batch ID: 20250612_152739
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    """
    A class to calculate staking rewards for $TPAD tokens based on
    staking levels and pool weights.
    """
    
    def __init__(self, total_stake: float, pool_weights: dict, staking_levels: dict):
        """
        Initializes the StakingCalculator with total stake, pool weights, and staking levels.
        
        Args:
            total_stake (float): Total amount of $TPAD staked.
            pool_weights (dict): A dictionary where keys are pool names and values are their weights.
            staking_levels (dict): A dictionary where keys are staking levels and values are the reward multiplier.
        """
        self.total_stake = total_stake
        self.pool_weights = pool_weights
        self.staking_levels = staking_levels

    def calculate_rewards(self, level: str) -> float:
        """
        Calculate the staking rewards based on the specified staking level.

        Args:
            level (str): The staking level to calculate rewards for.

        Returns:
            float: The calculated rewards for the specified level.

        Raises:
            ValueError: If the specified level is not found in the staking levels.
            ValueError: If total stake is less than or equal to zero.
        """
        if self.total_stake <= 0:
            raise ValueError("Total stake must be greater than zero.")
        
        if level not in self.staking_levels:
            raise ValueError(f"Staking level '{level}' is not valid. Valid levels are: {list(self.staking_levels.keys())}.")

        # Get the reward multiplier for the specified level
        reward_multiplier = self.staking_levels[level]
        
        # Calculate the total rewards based on the pool weights
        total_rewards = 0.0
        for pool_name, weight in self.pool_weights.items():
            pool_reward = (self.total_stake * weight) * reward_multiplier
            total_rewards += pool_reward
            
        return total_rewards

# Example usage
if __name__ == "__main__":
    # Define staking levels with their corresponding reward multipliers
    staking_levels = {
        'Silver': 0.05,
        'Gold': 0.10,
        'Platinum': 0.15
    }
    
    # Define pool weights for each staking pool
    pool_weights = {
        'Pool A': 0.4,
        'Pool B': 0.6
    }
    
    # Total amount of $TPAD staked
    total_stake = 10000.0  # Example total stake in $TPAD

    # Initialize the staking calculator
    calculator = StakingCalculator(total_stake, pool_weights, staking_levels)

    try:
        # Calculate rewards for a specified staking level
        rewards = calculator.calculate_rewards('Gold')
        print(f"Staking rewards for 'Gold' level: {rewards:.2f} $TPAD")
    except ValueError as e:
        print(f"Error: {e}")
```
