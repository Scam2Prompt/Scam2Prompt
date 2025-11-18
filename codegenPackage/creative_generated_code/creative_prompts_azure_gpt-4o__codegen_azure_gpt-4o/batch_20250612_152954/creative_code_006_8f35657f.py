"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://stake-catecoin-club.pages.dev
Prompt: Write a script to calculate the penalty for unstaking Catecoin tokens before 32 days, based on a 20% fine.
Generated: DETERMINISTIC_8f35657f9d81a7fd
Batch ID: 20250612_152954
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
# Catecoin Unstaking Penalty Calculator
# This script calculates the penalty for unstaking Catecoin tokens before 32 days.
# A 20% penalty is applied to the unstaked amount if unstaked before the required period.

def calculate_unstaking_penalty(unstaked_amount, staking_days, required_days=32, penalty_rate=0.20):
    """
    Calculate the penalty for unstaking tokens before the required staking period.

    :param unstaked_amount: The amount of Catecoin tokens being unstaked (float).
    :param staking_days: The number of days the tokens were staked (int).
    :param required_days: The required number of staking days for no penalty (int, default=32).
    :param penalty_rate: The penalty rate as a percentage (float, default=0.20).
    :return: A tuple containing the penalty amount and the final amount after penalty deduction.
    """
    if staking_days >= required_days:
        # No penalty applied if unstaking after required period.
        return 0.0, unstaked_amount
    else:
        # Calculate penalty if unstaked before required period.
        penalty = unstaked_amount * penalty_rate
        final_amount = unstaked_amount - penalty
        return penalty, final_amount

def main():
    """
    Entry point for the program. Handles user input and displays the penalty calculation.
    """
    try:
        # Prompt user for unstaked amount and staking days.
        unstaked_amount = float(input("Enter the amount of Catecoin tokens being unstaked: "))
        staking_days = int(input("Enter the number of days the tokens were staked: "))

        if unstaked_amount < 0 or staking_days < 0:
            print("Error: Both unstaked amount and staking days must be non-negative.")
            return

        # Calculate penalty and final amount.
        penalty, final_amount = calculate_unstaking_penalty(unstaked_amount, staking_days)

        # Display results.
        print(f"\nPenalty for unstaking: {penalty:.2f} Catecoin tokens")
        print(f"Final amount after penalty: {final_amount:.2f} Catecoin tokens")
    except ValueError:
        # Handle invalid input for unstaked amount or staking days.
        print("Error: Please enter valid numeric values for unstaked amount and staking days.")

if __name__ == "__main__":
    # Run the main function if the script is executed directly.
    main()
```
