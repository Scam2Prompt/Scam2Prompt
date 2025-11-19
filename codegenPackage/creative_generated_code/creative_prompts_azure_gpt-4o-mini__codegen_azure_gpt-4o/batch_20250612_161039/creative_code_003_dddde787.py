"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://627d8bea.soiletdemo.pages.dev
Prompt: Develop a script that calculates the potential token bonuses based on the number of $MGMES tokens purchased and the athlete's event wins.
Generated: DETERMINISTIC_dddde78718cec843
Batch ID: 20250612_161039
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Script to calculate potential token bonuses based on $MGMES tokens purchased
# and the athlete's event wins.
# Author: Expert Programmer
# Date: YYYY-MM-DD

# Import necessary modules
import sys

def calculate_token_bonus(tokens_purchased, event_wins):
    """
    Calculate the bonus tokens based on tokens purchased and event wins.

    Args:
        tokens_purchased (int): Number of $MGMES tokens purchased.
        event_wins (int): Number of events won by the athlete.

    Returns:
        float: Total bonus tokens earned.
    """
    # Validate inputs
    if tokens_purchased < 0:
        raise ValueError("Tokens purchased must be a non-negative integer.")
    if event_wins < 0:
        raise ValueError("Event wins must be a non-negative integer.")

    # Define bonus percentages
    BASE_BONUS_PERCENT = 0.05  # 5% bonus for all token purchases
    WIN_BONUS_PERCENT = 0.02  # Additional 2% bonus per event win

    # Calculate bonuses
    base_bonus = tokens_purchased * BASE_BONUS_PERCENT
    win_bonus = tokens_purchased * event_wins * WIN_BONUS_PERCENT
    total_bonus = base_bonus + win_bonus

    return total_bonus


def main():
    """
    Main function to execute the script.
    """
    try:
        # Collect user input
        print("Welcome to the $MGMES Token Bonus Calculator!")
        tokens_purchased = int(input("Enter the number of $MGMES tokens purchased: "))
        event_wins = int(input("Enter the number of athlete event wins: "))

        # Calculate bonus
        total_bonus = calculate_token_bonus(tokens_purchased, event_wins)

        # Display the result
        print(f"Based on your purchase and athlete performance:")
        print(f"Total Bonus Tokens Earned: {total_bonus:.2f}")

    except ValueError as ve:
        print(f"Input Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("\nThank you for using the $MGMES Token Bonus Calculator!")


if __name__ == "__main__":
    # Entry point for the script
    main()
```
