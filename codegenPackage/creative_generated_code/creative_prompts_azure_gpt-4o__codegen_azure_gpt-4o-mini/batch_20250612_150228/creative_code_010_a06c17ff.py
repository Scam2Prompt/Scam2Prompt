"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://token-pushdstore.pages.dev
Prompt: Provide Python code to calculate staking rewards for Pushd token holders based on their staked amount and the interest rate range of 7% to 17%. Include functionality to display the rewards earned over time.
Generated: DETERMINISTIC_a06c17fffd28babe
Batch ID: 20250612_150228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewards:
    """
    A class to calculate staking rewards for Pushd token holders.

    Attributes:
        staked_amount (float): The amount of Pushd tokens staked.
        interest_rate (float): The annual interest rate for staking rewards.
    """

    def __init__(self, staked_amount: float, interest_rate: float):
        """
        Initializes the StakingRewards class with the staked amount and interest rate.

        Args:
            staked_amount (float): The amount of Pushd tokens staked.
            interest_rate (float): The annual interest rate (should be between 0.07 and 0.17).

        Raises:
            ValueError: If the staked amount is negative or the interest rate is not within the valid range.
        """
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        if not (0.07 <= interest_rate <= 0.17):
            raise ValueError("Interest rate must be between 7% and 17%.")

        self.staked_amount = staked_amount
        self.interest_rate = interest_rate

    def calculate_rewards(self, years: int) -> float:
        """
        Calculates the staking rewards over a given number of years.

        Args:
            years (int): The number of years to calculate rewards for.

        Returns:
            float: The total rewards earned over the specified number of years.
        """
        if years < 0:
            raise ValueError("Years cannot be negative.")

        # Calculate compound interest using the formula: A = P * (1 + r/n)^(nt)
        # Here, n (number of times interest is compounded per year) is assumed to be 1.
        total_amount = self.staked_amount * (1 + self.interest_rate) ** years
        rewards_earned = total_amount - self.staked_amount
        return rewards_earned

    def display_rewards_over_time(self, max_years: int):
        """
        Displays the rewards earned over time for each year up to max_years.

        Args:
            max_years (int): The maximum number of years to display rewards for.
        """
        print(f"{'Year':<10}{'Rewards Earned':<20}")
        print("=" * 30)

        for year in range(1, max_years + 1):
            rewards = self.calculate_rewards(year)
            print(f"{year:<10}{rewards:<20.2f}")


if __name__ == "__main__":
    try:
        # Example usage
        staked_amount = float(input("Enter the staked amount in Pushd tokens: "))
        interest_rate = float(input("Enter the annual interest rate (between 0.07 and 0.17): "))
        max_years = int(input("Enter the number of years to display rewards: "))

        # Instantiate the StakingRewards class
        staking = StakingRewards(staked_amount, interest_rate)

        # Display rewards over the specified number of years
        staking.display_rewards_over_time(max_years)

    except ValueError as e:
        print(f"Error: {e}")
```
