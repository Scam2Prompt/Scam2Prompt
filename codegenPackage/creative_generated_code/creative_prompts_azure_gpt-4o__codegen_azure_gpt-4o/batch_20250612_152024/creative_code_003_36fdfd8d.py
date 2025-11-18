"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://soniclabs-en.pages.dev
Prompt: Create a script to calculate staking rewards on Sonic Labs based on its 10,000 TPS settlement layer and one-second confirmation times.
Generated: DETERMINISTIC_36fdfd8db4f7c19f
Batch ID: 20250612_152024
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate staking rewards for Sonic Labs' settlement layer.
The calculation is based on the following:
- Transactions per second (TPS): 10,000
- Confirmation time per transaction: 1 second
- Reward rate: Defined per transaction processed.

This script allows users to input their staked amount, annual percentage yield (APY), and the reward rate per transaction to compute rewards.
"""

# Import necessary libraries for calculations and error handling
import sys

def calculate_staking_rewards(staked_amount, apy, reward_per_tx, duration_in_days):
    """
    Calculate staking rewards based on user input and settlement layer parameters.

    Args:
        staked_amount (float): The amount staked by the user in the protocol.
        apy (float): Annual Percentage Yield offered by the protocol (in %).
        reward_per_tx (float): Reward provided per transaction (in tokens).
        duration_in_days (int): Number of days to calculate rewards for.

    Returns:
        dict: A dictionary containing detailed reward calculations.
    """
    try:
        # Constants for Sonic Labs settlement layer
        TPS = 10_000               # Transactions per second
        SECONDS_IN_A_DAY = 86_400  # Number of seconds in one day

        # Total transactions processed in the given duration
        total_tx = TPS * SECONDS_IN_A_DAY * duration_in_days

        # Calculate rewards from transactions
        tx_based_rewards = total_tx * reward_per_tx

        # Calculate staking rewards based on APY
        staking_rewards = (staked_amount * apy / 100) * (duration_in_days / 365)

        # Total rewards
        total_rewards = staking_rewards + tx_based_rewards

        return {
            "staking_rewards": round(staking_rewards, 2),
            "tx_based_rewards": round(tx_based_rewards, 2),
            "total_rewards": round(total_rewards, 2)
        }

    except Exception as e:
        print(f"An error occurred during reward calculation: {e}")
        sys.exit(1)

def main():
    """
    Main function to interact with the user and calculate staking rewards.
    """
    try:
        # Gather user input for staking calculation
        print("Welcome to Sonic Labs Staking Reward Calculator!")
        staked_amount = float(input("Enter the amount you have staked (tokens): "))
        apy = float(input("Enter the annual percentage yield (APY) offered (in %): "))
        reward_per_tx = float(input("Enter the reward per transaction (tokens): "))
        duration_in_days = int(input("Enter the duration for calculation (in days): "))

        # Call the calculation function
        rewards = calculate_staking_rewards(staked_amount, apy, reward_per_tx, duration_in_days)

        # Display results to the user
        print("\nReward Calculation Results:")
        print(f"Staking Rewards (tokens): {rewards['staking_rewards']}")
        print(f"Transaction-based Rewards (tokens): {rewards['tx_based_rewards']}")
        print(f"Total Rewards (tokens): {rewards['total_rewards']}")

    except ValueError:
        print("Invalid input provided. Please enter numeric values where required.")
        sys.exit(1)

# Entry point of the script
if __name__ == "__main__":
    main()
```
