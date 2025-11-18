"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.staderlabs.fi
Prompt: Write a script to calculate staking rewards for liquid tokens issued by Stader Labs, factoring in yield redirection farming and preferential delegations.
Generated: DETERMINISTIC_4bff611547121aa6
Batch ID: 20250612_153820
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import decimal
from decimal import Decimal

# Set up decimal precision for financial calculations
decimal.getcontext().prec = 28

class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for liquid tokens issued by Stader Labs.
    This includes yield redirection farming and preferential delegations.
    """

    def __init__(self, base_reward_rate, redirection_rate, preferential_boost):
        """
        Initialize the calculator with reward parameters.

        :param base_reward_rate: Annual base reward rate as a percentage (e.g., 5.0 for 5%).
        :param redirection_rate: Yield redirection farming rate as a percentage (e.g., 2.0 for 2%).
        :param preferential_boost: Preferential delegation boost as a percentage (e.g., 1.5 for 1.5%).
        """
        self.base_reward_rate = Decimal(base_reward_rate) / 100
        self.redirection_rate = Decimal(redirection_rate) / 100
        self.preferential_boost = Decimal(preferential_boost) / 100

    def calculate_rewards(self, staked_amount, days_staked):
        """
        Calculate the staking rewards based on the given parameters.

        :param staked_amount: Amount of tokens staked (Decimal or float).
        :param days_staked: Number of days the tokens are staked (int).
        :return: Total rewards earned as a Decimal.
        """
        try:
            # Ensure staked amount is a Decimal for precision
            staked_amount = Decimal(staked_amount)
            
            # Convert days to a fraction of the year
            annual_fraction = Decimal(days_staked) / Decimal(365)
            
            # Calculate base rewards
            base_rewards = staked_amount * self.base_reward_rate * annual_fraction
            
            # Calculate yield redirection farming rewards
            redirection_rewards = staked_amount * self.redirection_rate * annual_fraction
            
            # Calculate preferential delegation boost rewards
            preferential_rewards = staked_amount * self.preferential_boost * annual_fraction
            
            # Sum total rewards
            total_rewards = base_rewards + redirection_rewards + preferential_rewards
            
            return total_rewards
        
        except Exception as e:
            # Handle any errors gracefully
            raise ValueError(f"Error calculating rewards: {e}")

if __name__ == "__main__":
    # Example usage of the StakingRewardsCalculator
    
    # Parameters (these should be dynamically configurable in a real application)
    BASE_REWARD_RATE = 5.0  # Annual base reward rate (percentage)
    REDIRECTION_RATE = 2.0  # Yield redirection rate (percentage)
    PREFERENTIAL_BOOST = 1.5  # Preferential delegation boost (percentage)
    
    # User inputs (these would come from the system or user in a production setting)
    STAKED_AMOUNT = 1000.0  # Amount of tokens staked
    DAYS_STAKED = 30        # Number of days staked

    # Instantiate the calculator
    calculator = StakingRewardsCalculator(BASE_REWARD_RATE, REDIRECTION_RATE, PREFERENTIAL_BOOST)
    
    try:
        # Calculate rewards
        rewards = calculator.calculate_rewards(STAKED_AMOUNT, DAYS_STAKED)
        print(f"Total rewards earned: {rewards:.8f} tokens")
    except ValueError as error:
        print(f"Failed to calculate rewards: {error}")
```
