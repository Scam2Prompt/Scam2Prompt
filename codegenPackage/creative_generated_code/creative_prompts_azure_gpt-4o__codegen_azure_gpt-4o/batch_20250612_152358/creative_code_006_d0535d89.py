"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://wienerdogai-claim.pages.dev
Prompt: Develop a Python script to calculate the percentage of $WAI tokens staked and the total rewards earned, based on the tokenomics data provided by WienerAI.
Generated: DETERMINISTIC_d0535d896670cc1c
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Python Script to Calculate Percentage of $WAI Tokens Staked and Total Rewards Earned
# Based on Tokenomics Data Provided by WienerAI

# Import necessary modules
import sys

def calculate_staking_percentage(total_tokens, staked_tokens):
    """
    Calculate the percentage of $WAI tokens staked.

    Parameters:
        total_tokens (float): Total number of $WAI tokens in circulation.
        staked_tokens (float): Number of $WAI tokens staked.

    Returns:
        float: Percentage of staked tokens.
    """
    try:
        if total_tokens <= 0:
            raise ValueError("Total tokens must be greater than zero.")
        
        percentage_staked = (staked_tokens / total_tokens) * 100
        return round(percentage_staked, 2)
    except ZeroDivisionError:
        raise ValueError("Total tokens cannot be zero.")
    except Exception as e:
        raise RuntimeError(f"An error occurred during calculation: {e}")

def calculate_total_rewards(staked_tokens, reward_rate):
    """
    Calculate the total rewards earned based on the number of tokens staked.

    Parameters:
        staked_tokens (float): Number of $WAI tokens staked.
        reward_rate (float): Reward rate per token (e.g., 0.05 for 5% rewards).

    Returns:
        float: Total rewards earned.
    """
    try:
        if staked_tokens < 0 or reward_rate < 0:
            raise ValueError("Staked tokens and reward rate must be non-negative.")

        total_rewards = staked_tokens * reward_rate
        return round(total_rewards, 2)
    except Exception as e:
        raise RuntimeError(f"An error occurred during calculation: {e}")

def main():
    """
    Main function to execute the staking and rewards calculation.
    """
    try:
        # Input data (replace these with actual tokenomics data from WienerAI)
        total_tokens = float(input("Enter the total number of $WAI tokens in circulation: "))
        staked_tokens = float(input("Enter the number of $WAI tokens staked: "))
        reward_rate = float(input("Enter the reward rate per token (e.g., 0.05 for 5%): "))

        # Calculate percentage of tokens staked
        percentage_staked = calculate_staking_percentage(total_tokens, staked_tokens)
        print(f"Percentage of $WAI tokens staked: {percentage_staked}%")

        # Calculate total rewards earned
        total_rewards = calculate_total_rewards(staked_tokens, reward_rate)
        print(f"Total rewards earned: {total_rewards} $WAI tokens")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except RuntimeError as re:
        print(f"Runtime Error: {re}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Execute the script
    main()
```
