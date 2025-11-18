"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-jindo-coin.pages.dev
Prompt: Write a Python script to calculate the bonus percentage (e.g., 30% bonus or 500% maximum bonus) for Jindo token purchases based on the promotional events described on the website.
Generated: DETERMINISTIC_499ffe4db7b2a842
Batch ID: 20250612_150040
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate bonus percentages for Jindo token purchases based on promotional events.
This script uses predefined event rules to determine the bonus percentage based on user inputs.
"""

# Import required libraries
import sys

def calculate_bonus(purchase_amount, promo_event):
    """
    Calculate bonus percentage based on the promotional event and purchase amount.

    Args:
        purchase_amount (float): The amount of tokens purchased.
        promo_event (str): The promotional event name.

    Returns:
        float: The calculated bonus percentage.
    """
    # Define promotional event rules
    promo_rules = {
        "early_bird": {"base_bonus": 0.30, "max_bonus": 5.00},  # 30% base bonus, 500% max bonus
        "holiday_special": {"base_bonus": 0.20, "max_bonus": 3.00},  # 20% base bonus, 300% max bonus
        "regular_sale": {"base_bonus": 0.10, "max_bonus": 1.00},  # 10% base bonus, 100% max bonus
    }

    # Verify the promotional event exists
    if promo_event not in promo_rules:
        raise ValueError(f"Invalid promotional event: {promo_event}")

    # Get the event's rules
    event_rules = promo_rules[promo_event]

    # Calculate the bonus
    base_bonus = purchase_amount * event_rules["base_bonus"]
    max_bonus = purchase_amount * event_rules["max_bonus"]

    # Ensure the calculated bonus does not exceed the maximum bonus
    bonus_percentage = min(base_bonus, max_bonus)

    return bonus_percentage

def main():
    """
    Main function to handle user input and execute the bonus calculation.
    """
    try:
        # Collect user input
        purchase_amount = float(input("Enter the purchase amount (in tokens): "))
        promo_event = input("Enter the promotional event name (e.g., early_bird, holiday_special, regular_sale): ").strip().lower()

        # Verify the purchase amount is positive
        if purchase_amount <= 0:
            raise ValueError("Purchase amount must be a positive number.")

        # Calculate the bonus percentage
        bonus_percentage = calculate_bonus(purchase_amount, promo_event)

        # Display the result to the user
        print(f"The bonus percentage for your purchase is: {bonus_percentage:.2f}%")

    except ValueError as ve:
        print(f"Error: {ve}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

# Run the script only if executed directly
if __name__ == "__main__":
    main()
```
