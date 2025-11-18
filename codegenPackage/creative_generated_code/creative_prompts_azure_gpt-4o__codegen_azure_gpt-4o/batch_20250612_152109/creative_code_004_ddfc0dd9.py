"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://presale-scorpion-casino.pages.dev
Prompt: Write a Python script to calculate daily staking rewards for $SCORP token holders, factoring in the automatic token burn and buy-back system described in the Scorpion Casino ecosystem.
Generated: DETERMINISTIC_ddfc0dd99d50489c
Batch ID: 20250612_152109
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class ScorpTokenStakingRewards:
    """
    Class to calculate daily staking rewards for SCORP token holders.
    Includes logic for automatic token burn and buy-back as per
    the Scorpion Casino ecosystem.
    """

    def __init__(self, total_staked_tokens, daily_reward_rate, burn_rate, buy_back_rate):
        """
        Initialize the staking rewards calculator.

        :param total_staked_tokens: Total tokens staked in the ecosystem (int or float).
        :param daily_reward_rate: Daily reward rate as a percentage (float, e.g., 2.5 for 2.5%).
        :param burn_rate: Burn rate as a percentage (float, e.g., 1 for 1%).
        :param buy_back_rate: Buy-back rate as a percentage (float, e.g., 1 for 1%).
        """
        self.total_staked_tokens = total_staked_tokens
        self.daily_reward_rate = daily_reward_rate / 100  # Convert percentage to decimal
        self.burn_rate = burn_rate / 100  # Convert percentage to decimal
        self.buy_back_rate = buy_back_rate / 100  # Convert percentage to decimal

    def calculate_rewards(self, user_stake):
        """
        Calculate daily staking rewards for a user.

        :param user_stake: Number of tokens staked by the user (int or float).
        :return: Dictionary containing daily rewards, burn amount, and buy-back amount.
        """
        if user_stake <= 0 or self.total_staked_tokens <= 0:
            raise ValueError("User stake and total staked tokens must be greater than zero.")

        # Calculate user's share in the staking pool
        user_pool_share = user_stake / self.total_staked_tokens

        # Calculate total rewards generated for the day
        total_rewards = self.total_staked_tokens * self.daily_reward_rate

        # User's daily rewards based on their share in the pool
        user_rewards = total_rewards * user_pool_share

        # Calculate token burn and buy-back amounts
        burn_amount = user_rewards * self.burn_rate
        buy_back_amount = user_rewards * self.buy_back_rate

        # Net rewards after burn and buy-back
        net_rewards = user_rewards - (burn_amount + buy_back_amount)

        return {
            "user_rewards": round(user_rewards, 4),
            "burn_amount": round(burn_amount, 4),
            "buy_back_amount": round(buy_back_amount, 4),
            "net_rewards": round(net_rewards, 4)
        }


def main():
    """
    Main script to calculate daily staking rewards for SCORP token holders.
    """
    try:
        # Example usage
        total_staked_tokens = float(input("Enter total staked SCORP tokens in the ecosystem: "))
        daily_reward_rate = float(input("Enter daily reward rate percentage (e.g., 2.5 for 2.5%): "))
        burn_rate = float(input("Enter burn rate percentage (e.g., 1 for 1%): "))
        buy_back_rate = float(input("Enter buy-back rate percentage (e.g., 1 for 1%): "))
        user_stake = float(input("Enter the number of SCORP tokens staked by the user: "))

        # Initialize rewards calculator
        reward_calculator = ScorpTokenStakingRewards(
            total_staked_tokens, daily_reward_rate, burn_rate, buy_back_rate
        )

        # Calculate rewards
        rewards = reward_calculator.calculate_rewards(user_stake)

        # Display results
        print("\nDaily Staking Rewards Calculation:")
        print(f"User Rewards: {rewards['user_rewards']} SCORP tokens")
        print(f"Burn Amount: {rewards['burn_amount']} SCORP tokens")
        print(f"Buy-Back Amount: {rewards['buy_back_amount']} SCORP tokens")
        print(f"Net Rewards: {rewards['net_rewards']} SCORP tokens")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
