"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ton-448f1f.webflow.io
Prompt: Write a script to simulate the staking process for Airdrop Nodes and calculate expected rewards in $TONCAP tokens based on user input parameters.
Generated: DETERMINISTIC_7c4c4210f19a749c
Batch ID: 20250612_153915
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

class StakingSimulation:
    """
    Class to simulate the staking process and calculate expected rewards.
    """

    def __init__(self, stake_amount: float, staking_period_days: int, reward_rate: float):
        """
        Initialize the staking simulation parameters.

        :param stake_amount: Amount of tokens staked
        :param staking_period_days: Number of days the tokens are staked
        :param reward_rate: Daily reward rate (percentage as a decimal, e.g., 0.01 for 1%)
        """
        if stake_amount <= 0:
            raise ValueError("Stake amount must be greater than 0.")
        if staking_period_days <= 0:
            raise ValueError("Staking period must be greater than 0 days.")
        if reward_rate <= 0:
            raise ValueError("Reward rate must be greater than 0.")

        self.stake_amount = stake_amount
        self.staking_period_days = staking_period_days
        self.reward_rate = reward_rate

    def calculate_rewards(self) -> float:
        """
        Calculate the expected rewards based on staking parameters.

        :return: Total rewards in $TONCAP tokens
        """
        # Formula: Total Rewards = Stake Amount * Reward Rate * Staking Period
        return self.stake_amount * self.reward_rate * self.staking_period_days


def main():
    """
    Main function to simulate the staking process and calculate rewards.
    """
    try:
        print("Welcome to the Airdrop Node Staking Simulator!")
        print("Please enter the following parameters:")

        # Input parameters from the user
        stake_amount = float(input("Enter the amount of tokens to stake: "))
        staking_period_days = int(input("Enter the staking period (in days): "))
        reward_rate = float(input("Enter the daily reward rate (percentage as a decimal, e.g., 0.01 for 1%): "))

        # Create a staking simulation instance
        staking_simulation = StakingSimulation(stake_amount, staking_period_days, reward_rate)

        # Calculate rewards
        total_rewards = staking_simulation.calculate_rewards()

        # Display results
        print("\n=== Staking Simulation Results ===")
        print(f"Stake Amount: {stake_amount} tokens")
        print(f"Staking Period: {staking_period_days} days")
        print(f"Daily Reward Rate: {reward_rate * 100:.2f}%")
        print(f"Total Expected Rewards: {total_rewards:.2f} $TONCAP tokens")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
```
