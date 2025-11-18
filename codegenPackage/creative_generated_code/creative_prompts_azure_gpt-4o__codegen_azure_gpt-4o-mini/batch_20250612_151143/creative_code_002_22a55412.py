"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-e39.pages.dev
Prompt: Create a function to calculate rewards based on the Ancient8 staking lock-up periods (e.g., no lockup, 30 days, 60 days, 180 days).
Generated: DETERMINISTIC_22a55412ca7d9437
Batch ID: 20250612_151143
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    def __init__(self):
        # Define reward rates based on lock-up periods as a dictionary
        self.reward_rates = {
            'none': 0.0,    # No lock-up
            '30_days': 0.05, # 5% reward for 30 days
            '60_days': 0.10, # 10% reward for 60 days
            '180_days': 0.20 # 20% reward for 180 days
        }

    def calculate_rewards(self, amount: float, lockup_period: str) -> float:
        """
        Calculate the staking rewards based on the amount and lock-up period.

        Args:
            amount (float): The amount of tokens staked.
            lockup_period (str): The lock-up period - options are 'none', '30_days', '60_days', '180_days'.

        Returns:
            float: The rewards calculated based on the lock-up period.

        Raises:
            ValueError: If the lock-up period is not recognized or amount is negative.
        """
        if amount < 0:
            raise ValueError("The staking amount cannot be negative.")
        
        if lockup_period not in self.reward_rates:
            raise ValueError("Invalid lock-up period. Valid options are: 'none', '30_days', '60_days', '180_days'.")

        # Calculate the rewards based on the reward rate for the specified lock-up period
        reward_rate = self.reward_rates[lockup_period]
        rewards = amount * reward_rate

        return rewards

# Example usage
if __name__ == "__main__":
    calculator = StakingRewardsCalculator()
    
    try:
        amount_staked = 1000.0  # Example amount
        lockup = '60_days'      # Example lock-up period
        rewards = calculator.calculate_rewards(amount_staked, lockup)
        print(f"Staking {amount_staked} with a lock-up of {lockup} yields rewards of: {rewards:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
```
