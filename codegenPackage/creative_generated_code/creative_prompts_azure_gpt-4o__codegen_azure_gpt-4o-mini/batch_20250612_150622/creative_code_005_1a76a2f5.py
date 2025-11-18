"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogeverse-claimportal-xyz.pages.dev
Prompt: Create a script that calculates the percentage of a user's stake in the total staking pool and estimates their monthly and daily rewards based on the dynamic rewards rate.
Generated: DETERMINISTIC_1a76a2f527981c6e
Batch ID: 20250612_150622
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingCalculator:
    def __init__(self, total_stake: float, user_stake: float, daily_rewards_rate: float):
        """
        Initialize the StakingCalculator with the total stake in the pool,
        the user's stake, and the daily rewards rate.

        Args:
            total_stake (float): Total amount staked in the pool.
            user_stake (float): Amount staked by the user.
            daily_rewards_rate (float): Daily rewards rate as a decimal (e.g., 0.05 for 5%).
        """
        if total_stake <= 0:
            raise ValueError("Total stake must be greater than zero.")
        if user_stake < 0:
            raise ValueError("User stake cannot be negative.")
        if daily_rewards_rate < 0:
            raise ValueError("Daily rewards rate cannot be negative.")

        self.total_stake = total_stake
        self.user_stake = user_stake
        self.daily_rewards_rate = daily_rewards_rate

    def calculate_percentage_stake(self) -> float:
        """
        Calculate the percentage of the user's stake in the total staking pool.

        Returns:
            float: Percentage of the user's stake.
        """
        return (self.user_stake / self.total_stake) * 100

    def estimate_daily_rewards(self) -> float:
        """
        Estimate the user's daily rewards based on their stake and the rewards rate.

        Returns:
            float: Estimated daily rewards for the user.
        """
        return self.user_stake * self.daily_rewards_rate

    def estimate_monthly_rewards(self) -> float:
        """
        Estimate the user's monthly rewards based on their stake and the rewards rate.

        Returns:
            float: Estimated monthly rewards for the user.
        """
        daily_rewards = self.estimate_daily_rewards()
        return daily_rewards * 30  # Assuming 30 days in a month

    def display_results(self):
        """
        Display the user's stake percentage, daily rewards, and monthly rewards.
        """
        percentage_stake = self.calculate_percentage_stake()
        daily_rewards = self.estimate_daily_rewards()
        monthly_rewards = self.estimate_monthly_rewards()

        print(f"User's Stake Percentage: {percentage_stake:.2f}%")
        print(f"Estimated Daily Rewards: ${daily_rewards:.2f}")
        print(f"Estimated Monthly Rewards: ${monthly_rewards:.2f}")


if __name__ == "__main__":
    # Example usage:
    try:
        total_stake = float(input("Enter the total stake in the pool: "))
        user_stake = float(input("Enter your stake: "))
        daily_rewards_rate = float(input("Enter the daily rewards rate (as a decimal): "))

        staking_calculator = StakingCalculator(total_stake, user_stake, daily_rewards_rate)
        staking_calculator.display_results()
    except ValueError as e:
        print(f"Error: {e}")
```
