"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://jwzt-dashboards-inqubeta.pages.dev
Prompt: Generate a script to calculate weekly staking rewards for $QUBE tokens based on a reward rate provided by the dashboard.
Generated: DETERMINISTIC_cebaedf93a708faf
Batch ID: 20250612_152358
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Import necessary modules
import sys

def calculate_staking_rewards(staked_amount, reward_rate):
    """
    Calculate weekly staking rewards for QUBE tokens.
    
    Parameters:
        staked_amount (float): The amount of QUBE tokens staked.
        reward_rate (float): Weekly reward rate as a percentage (e.g., 5 for 5%).
        
    Returns:
        float: Weekly reward amount.
    """
    try:
        # Validate inputs
        if staked_amount < 0:
            raise ValueError("Staked amount cannot be negative.")
        if reward_rate < 0:
            raise ValueError("Reward rate cannot be negative.")
        
        # Calculate rewards
        weekly_rewards = (staked_amount * reward_rate) / 100
        return weekly_rewards
    
    except Exception as e:
        # Handle any unforeseen errors
        print(f"Error calculating staking rewards: {e}", file=sys.stderr)
        return None


def main():
    """
    Main function to calculate staking rewards based on user input.
    """
    try:
        # Get user input for staked amount and reward rate
        staked_amount = float(input("Enter the amount of QUBE tokens staked: "))
        reward_rate = float(input("Enter the weekly reward rate (in %): "))
        
        # Calculate rewards
        rewards = calculate_staking_rewards(staked_amount, reward_rate)
        
        if rewards is not None:
            print(f"Your weekly staking rewards are: {rewards:.2f} QUBE tokens.")
        else:
            print("Failed to calculate staking rewards. Please review the input values.")
    
    except ValueError:
        # Handle invalid input types
        print("Invalid input. Please enter numeric values for staked amount and reward rate.", file=sys.stderr)


if __name__ == "__main__":
    # Entry point of the script
    main()
```
