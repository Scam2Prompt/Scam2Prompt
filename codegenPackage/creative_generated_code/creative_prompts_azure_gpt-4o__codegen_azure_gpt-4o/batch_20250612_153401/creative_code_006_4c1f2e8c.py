"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hedgiescoin.pages.dev
Prompt: Create a script to calculate and display the $DYDX fee tier discount for users based on their Hedgie ownership and $DYDX holdings.
Generated: DETERMINISTIC_4c1f2e8ccc2e666c
Batch ID: 20250612_153401
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_dydx_fee_discount(hedgies_owned, dydx_holdings):
    """
    Calculates the $DYDX fee tier discount based on the number of Hedgies owned and $DYDX holdings.

    Parameters:
      hedgies_owned (int): Number of Hedgies owned by the user.
      dydx_holdings (float): Amount of $DYDX holdings in the user's account.

    Returns:
      float: The fee discount percentage.
    """
    # Define thresholds for fee tier discounts
    hedgie_bonus = 0.5  # Each Hedgie owned increases discount by 0.5%
    dydx_tier_discount = [
        (1000, 1.0),  # Holdings >= 1000 $DYDX => 1.0% discount
        (10000, 2.5),  # Holdings >= 10,000 $DYDX => 2.5% discount
        (50000, 5.0),  # Holdings >= 50,000 $DYDX => 5.0% discount
        (100000, 10.0)  # Holdings >= 100,000 $DYDX => 10.0% discount
    ]

    # Determine the $DYDX holdings-based discount
    dydx_discount = 0.0
    for threshold, discount in dydx_tier_discount:
        if dydx_holdings >= threshold:
            dydx_discount = discount
        else:
            break

    # Calculate final discount by adding Hedgie ownership bonus
    hedgie_discount = hedgies_owned * hedgie_bonus
    total_discount = dydx_discount + hedgie_discount

    # Ensure discount does not exceed a maximum threshold (e.g., 100%)
    return min(total_discount, 100.0)

def main():
    """
    Main function to execute the fee discount calculation script.
    """
    try:
        # Input: Number of Hedgies owned
        hedgies_owned = int(input("Enter the number of Hedgies you own: "))
        if hedgies_owned < 0:
            raise ValueError("Hedgies owned cannot be negative.")

        # Input: Amount of $DYDX holdings
        dydx_holdings = float(input("Enter the amount of $DYDX holdings you have: "))
        if dydx_holdings < 0:
            raise ValueError("$DYDX holdings cannot be negative.")

        # Calculate the fee discount
        fee_discount = calculate_dydx_fee_discount(hedgies_owned, dydx_holdings)

        # Display the result
        print(f"Your $DYDX fee tier discount is: {fee_discount:.2f}%")
    except ValueError as ve:
        print(f"Invalid input: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point for the script
    main()
```
