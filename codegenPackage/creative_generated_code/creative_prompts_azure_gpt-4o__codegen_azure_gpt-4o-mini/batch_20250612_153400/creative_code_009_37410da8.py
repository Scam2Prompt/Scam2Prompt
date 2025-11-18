"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdoge20live.pages.dev
Prompt: Develop a tool to calculate daily staking rewards for DOGE20 based on the dynamic annual returns percentage and the user's share of the staking pool.
Generated: DETERMINISTIC_37410da8aeaf5136
Batch ID: 20250612_153400
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
    A class to calculate daily staking rewards for DOGE20 based on annual returns percentage 
    and the user's share of the staking pool.
    """

    def __init__(self, annual_return_percentage: float, user_share: float):
        """
        Initializes the StakingCalculator with the annual return percentage and user share.

        :param annual_return_percentage: The dynamic annual returns percentage (as a decimal).
        :param user_share: The user's share of the staking pool (as a decimal).
        """
        if not (0 <= annual_return_percentage <= 100):
            raise ValueError("Annual return percentage must be between 0 and 100.")
        if not (0 <= user_share <= 1):
            raise ValueError("User share must be between 0 and 1.")

        self.annual_return_percentage = annual_return_percentage / 100  # convert to decimal
        self.user_share = user_share

    def calculate_daily_reward(self, total_staked_amount: float) -> float:
        """
        Calculate the daily staking rewards based on total staked amount.

        :param total_staked_amount: The total amount staked in the pool.
        :return: The user's daily staking reward.
        """
        if total_staked_amount <= 0:
            raise ValueError("Total staked amount must be greater than zero.")

        # Calculate the daily return as a decimal
        daily_return = self.annual_return_percentage / 365
        # Calculate the user's reward based on their share
        daily_reward = total_staked_amount * daily_return * self.user_share
        
        return daily_reward

def main():
    """
    Main function to demonstrate the StakingCalculator functionality.
    Adjust the parameters as necessary for testing.
    """
    try:
        # Example parameters
        total_staked_amount = 1000000.0  # Total amount in the staking pool
        annual_return_percentage = 5.0    # Annual return percentage
        user_share = 0.01                  # User's share of the staking pool (1%)

        # Create an instance of the StakingCalculator
        calculator = StakingCalculator(annual_return_percentage, user_share)
        
        # Calculate daily reward
        daily_reward = calculator.calculate_daily_reward(total_staked_amount)
        
        # Output result
        print(f"Daily Staking Reward: {daily_reward:.4f} DOGE20")
    
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
