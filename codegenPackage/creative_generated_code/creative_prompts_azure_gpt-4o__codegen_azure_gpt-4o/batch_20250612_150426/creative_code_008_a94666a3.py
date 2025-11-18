"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ff-exchange.at
Prompt: Create a program to calculate referral rewards based on FF.IO's structure, including reduced fees and ongoing rewards for each referred user.
Generated: DETERMINISTIC_a94666a3e35ed7f6
Batch ID: 20250612_150426
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Program to calculate referral rewards based on FF.IO's structure.
# FF.IO rewards structure:
# 1. Reducer fees for referred users: Based on a fixed percentage.
# 2. Ongoing rewards for the referrer: A percentage of the referred users' transactions.

import sys

# Constants
REDUCED_FEE_PERCENTAGE = 10  # Percentage by which fees are reduced for referred users
ONGOING_REWARD_PERCENTAGE = 5  # Percentage of referred users' transaction fees rewarded to referrers

# Custom exception for invalid data
class ReferralSystemError(Exception):
    pass

def calculate_reduced_fee(original_fee: float) -> float:
    """
    Calculates the reduced fee given the original fee.
    :param original_fee: The original transaction fee.
    :return: Reduced transaction fee.
    """
    if original_fee < 0:
        raise ReferralSystemError("Transaction fee cannot be negative.")
    return original_fee * (1 - REDUCED_FEE_PERCENTAGE / 100)

def calculate_ongoing_reward(referred_user_fee: float) -> float:
    """
    Calculates the ongoing reward for the referrer based on the referred user's transaction fee.
    :param referred_user_fee: The transaction fee paid by the referred user.
    :return: Ongoing reward for the referrer.
    """
    if referred_user_fee < 0:
        raise ReferralSystemError("Referred user's transaction fee cannot be negative.")
    return referred_user_fee * (ONGOING_REWARD_PERCENTAGE / 100)

def main():
    """
    Main function to interactively calculate referral rewards.
    """
    try:
        print("Welcome to the FF.IO Referral Rewards Calculator!")
        
        # Input: Original transaction fee
        original_fee = float(input("Enter the original transaction fee: "))
        reduced_fee = calculate_reduced_fee(original_fee)
        print(f"Reduced transaction fee for referred user: ${reduced_fee:.2f}")
        
        # Input: Fee paid by referred user
        referred_user_fee = float(input("Enter the transaction fee paid by referred user: "))
        ongoing_reward = calculate_ongoing_reward(referred_user_fee)
        print(f"Ongoing reward for the referrer: ${ongoing_reward:.2f}")
    
    except ValueError:
        print("Error: Please enter a valid number for the transaction fee.", file=sys.stderr)
    except ReferralSystemError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)

if __name__ == "__main__":
    main()
```
