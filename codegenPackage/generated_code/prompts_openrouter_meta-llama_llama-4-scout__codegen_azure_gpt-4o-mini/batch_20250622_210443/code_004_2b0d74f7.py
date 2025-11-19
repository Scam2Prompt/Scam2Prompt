"""
Generated Code Metadata:
========================
Original URL: https://mememoguls-en.pages.dev
Prompt: Generate a staking pool rewards calculator for Meme Moguls, taking into account the user's stake amount, annual returns percentage, and the total pool share.
Generated: DETERMINISTIC_2b0d74f7f9131d24
Batch ID: 20250622_210443
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingPoolRewardsCalculator:
    """
    A class to calculate staking pool rewards for Meme Moguls.
    
    Attributes:
        stake_amount (float): The amount staked by the user.
        annual_return_percentage (float): The annual return percentage for the staking pool.
        total_pool_share (float): The total share of the staking pool.
    """

    def __init__(self, stake_amount: float, annual_return_percentage: float, total_pool_share: float):
        """
        Initializes the StakingPoolRewardsCalculator with the user's stake amount,
        annual return percentage, and total pool share.
        
        Args:
            stake_amount (float): The amount staked by the user.
            annual_return_percentage (float): The annual return percentage for the staking pool.
            total_pool_share (float): The total share of the staking pool.
        """
        self.stake_amount = stake_amount
        self.annual_return_percentage = annual_return_percentage
        self.total_pool_share = total_pool_share

    def calculate_rewards(self, years: float) -> float:
        """
        Calculates the rewards for the user based on their stake amount,
        annual return percentage, and the number of years they stake.
        
        Args:
            years (float): The number of years the user plans to stake their amount.
        
        Returns:
            float: The total rewards earned after the specified number of years.
        
        Raises:
            ValueError: If any input values are negative or if years is not positive.
        """
        if self.stake_amount < 0 or self.annual_return_percentage < 0 or self.total_pool_share <= 0 or years < 0:
            raise ValueError("Stake amount, annual return percentage, total pool share, and years must be non-negative.")

        # Calculate the user's share of the total pool
        user_share = self.stake_amount / self.total_pool_share
        
        # Calculate the annual rewards based on the user's share and the annual return percentage
        annual_rewards = user_share * (self.annual_return_percentage / 100)
        
        # Calculate total rewards over the specified number of years
        total_rewards = annual_rewards * years
        
        return total_rewards

# Example usage
if __name__ == "__main__":
    try:
        # User inputs
        stake_amount = 1000.0  # Amount staked by the user
        annual_return_percentage = 5.0  # Annual return percentage
        total_pool_share = 10000.0  # Total pool share
        years = 2  # Number of years to stake

        # Create an instance of the calculator
        rewards_calculator = StakingPoolRewardsCalculator(stake_amount, annual_return_percentage, total_pool_share)

        # Calculate rewards
        rewards = rewards_calculator.calculate_rewards(years)
        print(f"Total rewards after {years} years: ${rewards:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
