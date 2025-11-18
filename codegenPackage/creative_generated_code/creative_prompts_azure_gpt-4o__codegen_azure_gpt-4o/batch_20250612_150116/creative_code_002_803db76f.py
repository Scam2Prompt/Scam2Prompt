"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://aspiregaininvest.com
Prompt: Create a Python script to calculate affiliate rewards for a two-level partnership program, as described on AspireGain Invest's website (5% for first-level referrals and 5% for second-level referrals).
Generated: DETERMINISTIC_803db76f779b154b
Batch ID: 20250612_150116
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_affiliate_rewards(total_amount, first_level_percentage=0.05, second_level_percentage=0.05):
    """
    Calculate affiliate rewards for a two-level partnership program.
    
    Args:
        total_amount (float): The total earnings involved in the affiliate program.
        first_level_percentage (float): Reward percentage for first-level referrals.
        second_level_percentage (float): Reward percentage for second-level referrals.
        
    Returns:
        dict: A dictionary containing rewards for first-level and second-level referrals.
    """
    try:
        # Validate input
        if total_amount < 0:
            raise ValueError("Total amount cannot be negative.")
        if not (0 <= first_level_percentage <= 1) or not (0 <= second_level_percentage <= 1):
            raise ValueError("Reward percentages must be between 0 and 1.")
        
        # Calculate rewards
        first_level_reward = total_amount * first_level_percentage
        second_level_reward = total_amount * second_level_percentage
        
        return {
            "first_level_reward": round(first_level_reward, 2),
            "second_level_reward": round(second_level_reward, 2)
        }
    except ValueError as ve:
        print(f"ValueError: {ve}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    # Example usage: Modify inputs as needed
    try:
        # Input total amount from user
        total_amount = float(input("Enter the total amount of earnings: "))
        
        # Calculate rewards
        rewards = calculate_affiliate_rewards(total_amount)
        if rewards:
            print(f"First-Level Referral Reward: ${rewards['first_level_reward']}")
            print(f"Second-Level Referral Reward: ${rewards['second_level_reward']}")
        else:
            print("Failed to calculate rewards due to input errors.")
    except ValueError:
        print("Invalid input. Please enter a valid number for total amount.", file=sys.stderr)
```
