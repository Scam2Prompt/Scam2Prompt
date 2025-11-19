"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://dogecoin20-s.pages.dev
Prompt: Describe how to implement a rewards calculator for DOGE20 that reflects its fixed supply and staking rewards structure.
Generated: DETERMINISTIC_30e95451d080d598
Batch ID: 20250612_161500
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class RewardsCalculator:
    """
    A class to calculate staking rewards for DOGE20 based on fixed supply and staking distribution.
    """

    def __init__(self, total_supply: float, annual_reward_rate: float):
        """
        Initializes the rewards calculator.

        :param total_supply: The total supply of DOGE20 tokens.
        :param annual_reward_rate: The annual reward rate as a percentage (e.g., 5 for 5%).
        """
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than zero.")
        if not (0 <= annual_reward_rate <= 100):
            raise ValueError("Annual reward rate must be between 0 and 100.")

        self.total_supply = total_supply
        self.annual_reward_rate = annual_reward_rate

    def calculate_rewards(self, staked_amount: float, staking_duration: int) -> float:
        """
        Calculates the staking rewards for a given staked amount over a specified duration.

        :param staked_amount: The amount of DOGE20 tokens staked.
        :param staking_duration: The duration for which the tokens are staked, in years.
        :return: The amount of rewards earned during the staking period.
        """
        if staked_amount <= 0:
            raise ValueError("Staked amount must be greater than zero.")
        if staking_duration < 0:
            raise ValueError("Staking duration cannot be negative.")

        # Calculate annual rewards
        annual_rewards = (self.annual_reward_rate / 100) * staked_amount
        # Calculate total rewards over the staking duration
        total_rewards = annual_rewards * staking_duration

        return total_rewards

    def display_rewards(self, staked_amount: float, staking_duration: int):
        """
        Displays the calculated rewards in a user-friendly format.

        :param staked_amount: The amount of DOGE20 tokens staked.
        :param staking_duration: The duration for which the tokens are staked, in years.
        """
        try:
            rewards = self.calculate_rewards(staked_amount, staking_duration)
            print(f"For staking {staked_amount} DOGE20 for {staking_duration} years, "
                  f"the estimated rewards are: {rewards:.2f} DOGE20.")
        except ValueError as e:
            print(f"Error: {e}")


# Example usage:
if __name__ == "__main__":
    try:
        # Initialize the rewards calculator with total supply and annual reward rate.
        calculator = RewardsCalculator(total_supply=21_000_000, annual_reward_rate=5)

        # Example of calculating and displaying rewards.
        calculator.display_rewards(staked_amount=1000, staking_duration=2)
    except Exception as e:
        print(f"An error occurred during initialization: {e}")
```
