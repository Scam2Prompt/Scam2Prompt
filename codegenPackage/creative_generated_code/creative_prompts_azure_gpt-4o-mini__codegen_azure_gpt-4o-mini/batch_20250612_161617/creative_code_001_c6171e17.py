"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://steth-access1.pages.dev
Prompt: Write a code snippet to calculate the estimated rewards based on the current APY of 3.3% for the stETH Pool.
Generated: DETERMINISTIC_c6171e178e6a885e
Batch ID: 20250612_161617
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StETHPool:
    def __init__(self, apy: float):
        """
        Initializes the StETHPool with the given annual percentage yield (APY).

        Args:
            apy (float): The annual percentage yield for the pool, expressed as a decimal.
        """
        if not (0 <= apy <= 1):
            raise ValueError("APY must be between 0 and 1.")
        self.apy = apy

    def calculate_rewards(self, staked_amount: float, duration_in_days: int) -> float:
        """
        Calculates the estimated rewards based on the staked amount and duration.

        Args:
            staked_amount (float): The amount of stETH staked.
            duration_in_days (int): The duration for which the amount is staked, in days.

        Returns:
            float: The estimated rewards earned over the specified duration.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount must be non-negative.")
        if duration_in_days < 0:
            raise ValueError("Duration in days must be non-negative.")

        # Calculate daily APY
        daily_apy = self.apy / 365
        # Calculate rewards
        rewards = staked_amount * daily_apy * duration_in_days
        return rewards


def main():
    try:
        # Instantiate the StETHPool with a 3.3% APY
        pool = StETHPool(apy=0.033)
        
        # Example staked amount and duration
        staked_amount = 1000.0  # Amount in stETH
        duration_in_days = 30   # Duration in days

        # Calculate estimated rewards
        estimated_rewards = pool.calculate_rewards(staked_amount, duration_in_days)
        
        print(f"Estimated rewards for staking {staked_amount} stETH for {duration_in_days} days: {estimated_rewards:.2f} stETH")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```
