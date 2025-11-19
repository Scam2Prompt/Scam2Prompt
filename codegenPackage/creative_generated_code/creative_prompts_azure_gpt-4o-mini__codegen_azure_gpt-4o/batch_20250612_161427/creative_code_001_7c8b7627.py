"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://bitcoinbsc-io.pages.dev
Prompt: Write a Python script that calculates the estimated rewards for staking Bitcoin BSC based on the current staking pool percentage and total supply.
Generated: DETERMINISTIC_7c8b7627bf5b94c9
Batch ID: 20250612_161427
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_rewards(staked_percentage, total_supply, reward_rate):
    """
    Calculate the estimated staking rewards for Bitcoin BSC.

    Parameters:
        staked_percentage (float): The percentage of the staking pool (0-100).
        total_supply (float): The total supply of Bitcoin BSC tokens.
        reward_rate (float): The annual reward rate (e.g., 0.05 for 5%).

    Returns:
        float: Estimated annual rewards based on staking pool participation.
    """
    try:
        # Validate input values
        if not (0 <= staked_percentage <= 100):
            raise ValueError("Staked percentage must be between 0 and 100.")
        if total_supply <= 0:
            raise ValueError("Total supply must be greater than 0.")
        if reward_rate < 0:
            raise ValueError("Reward rate must be non-negative.")

        # Convert percentage to a decimal (e.g., 50% becomes 0.5)
        decimal_staked_percentage = staked_percentage / 100

        # Calculate the staking rewards
        rewards = total_supply * decimal_staked_percentage * reward_rate
        return rewards

    except ValueError as ve:
        # Handle invalid input gracefully
        print(f"Input Error: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        # Handle unexpected errors
        print(f"Unexpected Error: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to collect user inputs and calculate estimated staking rewards.
    """
    try:
        # Collect user inputs
        staked_percentage = float(input("Enter the staking pool percentage (0-100): "))
        total_supply = float(input("Enter the total supply of Bitcoin BSC tokens: "))
        reward_rate = float(input("Enter the annual reward rate (e.g., 0.05 for 5%): "))

        # Calculate rewards
        rewards = calculate_rewards(staked_percentage, total_supply, reward_rate)

        # Display the result if calculation succeeded
        if rewards is not None:
            print(f"Estimated annual rewards: {rewards:.2f} Bitcoin BSC tokens")

    except ValueError:
        print("Invalid input. Please enter numeric values.", file=sys.stderr)
    except Exception as e:
        print(f"Unexpected Error: {e}", file=sys.stderr)


# Entry point of the script
if __name__ == "__main__":
    main()
```
