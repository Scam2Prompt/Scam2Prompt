"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claimdoge-live.pages.dev
Prompt: Write code to simulate the monthly and daily reward calculations for DOGE20 staking, using the formula provided on the Dogecoin20 platform.
Generated: DETERMINISTIC_3d44844c37e7fb30
Batch ID: 20250612_153400
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class Doge20Staking:
    """
    A class to simulate the monthly and daily reward calculations for DOGE20 staking.
    """

    def __init__(self, stake_amount: float, reward_rate: float):
        """
        Initializes the Doge20Staking instance.

        :param stake_amount: The amount of DOGE20 staked.
        :param reward_rate: The annual reward rate as a decimal (e.g., 0.05 for 5%).
        """
        if stake_amount < 0:
            raise ValueError("Stake amount must be non-negative.")
        if not (0 <= reward_rate <= 1):
            raise ValueError("Reward rate must be between 0 and 1.")
        
        self.stake_amount = stake_amount
        self.reward_rate = reward_rate

    def calculate_daily_reward(self) -> float:
        """
        Calculates the daily reward based on the stake amount and reward rate.

        :return: The daily reward amount.
        """
        daily_reward = (self.stake_amount * self.reward_rate) / 365
        return daily_reward

    def calculate_monthly_reward(self) -> float:
        """
        Calculates the monthly reward based on the stake amount and reward rate.

        :return: The monthly reward amount.
        """
        monthly_reward = (self.stake_amount * self.reward_rate) / 12
        return monthly_reward

    def display_rewards(self):
        """
        Displays the daily and monthly rewards.
        """
        try:
            daily_reward = self.calculate_daily_reward()
            monthly_reward = self.calculate_monthly_reward()
            print(f"Daily Reward: {daily_reward:.4f} DOGE20")
            print(f"Monthly Reward: {monthly_reward:.4f} DOGE20")
        except Exception as e:
            print(f"An error occurred while calculating rewards: {e}")

# Example usage:
if __name__ == "__main__":
    try:
        stake_amount = float(input("Enter the amount of DOGE20 staked: "))
        reward_rate = float(input("Enter the annual reward rate (as a decimal): "))
        
        staking = Doge20Staking(stake_amount, reward_rate)
        staking.display_rewards()
        
    except ValueError as ve:
        print(f"Input error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
```
