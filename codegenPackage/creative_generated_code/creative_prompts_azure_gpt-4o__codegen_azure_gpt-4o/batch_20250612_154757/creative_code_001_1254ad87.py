"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://doge20claim-dashboard.pages.dev
Prompt: Generate code to calculate staking rewards for DOGE20 based on the percentage of the staking pool and dynamic annual returns, as described on the Dogecoin20 website.
Generated: DETERMINISTIC_1254ad879f3829de
Batch ID: 20250612_154757
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for DOGE20 based on the percentage of the staking pool
    and dynamic annual returns.
    """
    def __init__(self, annual_returns: float, total_stake_pool: float):
        """
        Initializes the staking rewards calculator.

        :param annual_returns: Annual returns in percentage (e.g., 5.0 for 5%).
        :param total_stake_pool: Total value of the staking pool in DOGE20.
        """
        if annual_returns <= 0 or total_stake_pool <= 0:
            raise ValueError("Annual returns and total stake pool must be positive values.")
        self.annual_returns = annual_returns
        self.total_stake_pool = total_stake_pool

    def calculate_rewards(self, user_stake: float) -> float:
        """
        Calculates the staking rewards for a user.

        :param user_stake: The amount staked by the user in DOGE20.
        :return: The calculated staking rewards for the user in DOGE20.
        """
        if user_stake <= 0 or user_stake > self.total_stake_pool:
            raise ValueError("User stake must be positive and within the staking pool's range.")
        
        # Calculate the percentage share in the staking pool
        user_share_percentage = user_stake / self.total_stake_pool
        
        # Calculate the annual rewards based on the user's share
        annual_rewards = user_share_percentage * (self.annual_returns / 100) * self.total_stake_pool
        
        return annual_rewards

def main():
    """
    Main function to handle user input and calculate staking rewards.
    """
    try:
        # Input annual returns (in percentage), total staking pool, and user stake
        annual_returns = float(input("Enter the annual returns (in %): "))
        total_stake_pool = float(input("Enter the total stake pool (in DOGE20): "))
        user_stake = float(input("Enter the amount you have staked (in DOGE20): "))

        # Instantiate the calculator and calculate rewards
        calculator = StakingRewardsCalculator(annual_returns, total_stake_pool)
        rewards = calculator.calculate_rewards(user_stake)

        # Display the calculated rewards
        print(f"Your annual staking rewards are: {rewards:.2f} DOGE20")
    
    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
