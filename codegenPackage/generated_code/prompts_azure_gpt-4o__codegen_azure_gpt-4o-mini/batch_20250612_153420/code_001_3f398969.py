"""
Generated Code Metadata:
========================
Original URL: https://metazero.pages.dev
Prompt: Generate code to calculate staking rewards (APR) for MZERO tokens, factoring in a withdrawal lock period of 7 days and an unstake fee of 0%.
Generated: DETERMINISTIC_3f3989698d2186a8
Batch ID: 20250612_153420
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class StakingRewardsCalculator:
    """
    A class to calculate staking rewards for MZERO tokens.
    
    Attributes:
        annual_percentage_rate (float): The annual percentage rate for staking rewards.
        lock_period_days (int): The withdrawal lock period in days.
        unstake_fee (float): The fee charged for unstaking (as a percentage).
    """

    def __init__(self, annual_percentage_rate: float, lock_period_days: int = 7, unstake_fee: float = 0.0):
        """
        Initializes the StakingRewardsCalculator with the given parameters.
        
        Args:
            annual_percentage_rate (float): The annual percentage rate for staking rewards.
            lock_period_days (int): The withdrawal lock period in days (default is 7).
            unstake_fee (float): The fee charged for unstaking (default is 0.0).
        """
        if annual_percentage_rate < 0:
            raise ValueError("Annual percentage rate must be non-negative.")
        if lock_period_days < 0:
            raise ValueError("Lock period days must be non-negative.")
        if not (0 <= unstake_fee <= 1):
            raise ValueError("Unstake fee must be between 0 and 1.")

        self.annual_percentage_rate = annual_percentage_rate
        self.lock_period_days = lock_period_days
        self.unstake_fee = unstake_fee

    def calculate_rewards(self, staked_amount: float, staking_days: int) -> float:
        """
        Calculates the staking rewards based on the staked amount and the number of staking days.
        
        Args:
            staked_amount (float): The amount of MZERO tokens staked.
            staking_days (int): The number of days the tokens have been staked.
        
        Returns:
            float: The calculated rewards.
        
        Raises:
            ValueError: If staked_amount or staking_days are negative.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")
        if staking_days < 0:
            raise ValueError("Staking days must be non-negative.")

        # Calculate the rewards based on the staking days
        if staking_days < self.lock_period_days:
            return 0.0  # No rewards if within the lock period

        # Calculate the daily interest rate
        daily_interest_rate = self.annual_percentage_rate / 365

        # Calculate total rewards
        total_rewards = staked_amount * daily_interest_rate * staking_days

        return total_rewards

    def calculate_final_amount(self, staked_amount: float, staking_days: int) -> float:
        """
        Calculates the final amount after rewards and considering the unstake fee.
        
        Args:
            staked_amount (float): The amount of MZERO tokens staked.
            staking_days (int): The number of days the tokens have been staked.
        
        Returns:
            float: The final amount after rewards and fees.
        """
        rewards = self.calculate_rewards(staked_amount, staking_days)
        final_amount = staked_amount + rewards

        # Apply unstake fee
        final_amount -= final_amount * self.unstake_fee

        return final_amount


# Example usage
if __name__ == "__main__":
    try:
        # Initialize the calculator with an APR of 10%
        calculator = StakingRewardsCalculator(annual_percentage_rate=0.10)

        # Define the staked amount and staking duration
        staked_amount = 1000.0  # Amount of MZERO tokens
        staking_days = 30  # Days staked

        # Calculate rewards and final amount
        rewards = calculator.calculate_rewards(staked_amount, staking_days)
        final_amount = calculator.calculate_final_amount(staked_amount, staking_days)

        print(f"Staked Amount: {staked_amount} MZERO")
        print(f"Rewards Earned: {rewards:.2f} MZERO")
        print(f"Final Amount after Rewards and Fees: {final_amount:.2f} MZERO")

    except ValueError as e:
        print(f"Error: {e}")
```
