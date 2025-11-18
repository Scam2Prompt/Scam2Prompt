"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wlfin.org
Prompt: Write a script to calculate staking rewards for WL tokens based on the staking mechanism described in the WLFI ecosystem.
Generated: DETERMINISTIC_09f0676cf4f115ef
Batch ID: 20250612_154542
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class StakingRewardsCalculator:
    def __init__(self, total_staked: float, reward_rate: float, staking_period: int):
        """
        Initializes the StakingRewardsCalculator with the given parameters.
        
        :param total_staked: Total amount of WL tokens staked by the user.
        :param reward_rate: Annual reward rate as a decimal (e.g., 0.05 for 5%).
        :param staking_period: Time period for staking in days.
        """
        if total_staked < 0:
            raise ValueError("Total staked amount cannot be negative.")
        if not (0 <= reward_rate <= 1):
            raise ValueError("Reward rate must be between 0 and 1.")
        if staking_period <= 0:
            raise ValueError("Staking period must be a positive integer.")

        self.total_staked = total_staked
        self.reward_rate = reward_rate
        self.staking_period = staking_period

    def calculate_rewards(self) -> float:
        """
        Calculates the staking rewards based on the total staked amount, 
        annual reward rate, and staking period.

        :return: The amount of staking rewards earned.
        """
        # Calculate daily reward rate from annual rate
        daily_reward_rate = self.reward_rate / 365
        # Calculate rewards for the staking period
        rewards = self.total_staked * daily_reward_rate * self.staking_period
        return rewards

    def display_rewards(self) -> None:
        """
        Displays the calculated staking rewards to the user.
        """
        try:
            rewards = self.calculate_rewards()
            print(f"Total WL Tokens Staked: {self.total_staked}")
            print(f"Annual Reward Rate: {self.reward_rate * 100:.2f}%")
            print(f"Staking Period: {self.staking_period} days")
            print(f"Total Rewards Earned: {rewards:.4f} WL Tokens")
        except Exception as e:
            print(f"An error occurred while calculating rewards: {e}")


if __name__ == "__main__":
    # Example parameters for the staking rewards calculation
    total_staked = 1000.0  # Amount of WL tokens staked
    reward_rate = 0.05      # Annual reward rate (5%)
    staking_period = 30      # Staking period in days

    try:
        # Create the calculator instance
        calculator = StakingRewardsCalculator(total_staked, reward_rate, staking_period)
        # Display the rewards
        calculator.display_rewards()
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
