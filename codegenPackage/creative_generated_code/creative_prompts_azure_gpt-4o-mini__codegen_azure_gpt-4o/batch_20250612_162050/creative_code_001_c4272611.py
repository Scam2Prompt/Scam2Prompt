"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://proarteasa.com
Prompt: Write a Python script that calculates the total cost of purchasing a lot in Acacias Retiro Campestre, including financing options with 0% interest for up to 36 months.
Generated: DETERMINISTIC_c427261198ab4d19
Batch ID: 20250612_162050
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Script to calculate the total cost of purchasing a lot at Acacias Retiro Campestre,
including financing options with 0% interest for up to 36 months.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary module for user input validation
import sys


def get_positive_float(prompt):
    """
    Prompt the user for a positive float value. Repeats until valid input is provided.
    :param prompt: Message to show the user
    :return: Positive float value
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                raise ValueError("Value must be greater than 0.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def get_valid_int(prompt, min_value, max_value):
    """
    Prompt the user for an integer within a specified range.
    :param prompt: Message to show the user
    :param min_value: Minimum acceptable value
    :param max_value: Maximum acceptable value
    :return: Valid integer within range
    """
    while True:
        try:
            value = int(input(prompt))
            if value < min_value or value > max_value:
                raise ValueError(f"Value must be between {min_value} and {max_value}.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please try again.")


def calculate_financing(lot_price, months):
    """
    Calculate the monthly payment for financing with 0% interest.
    :param lot_price: Total price of the lot
    :param months: Number of months for financing
    :return: Monthly payment amount
    """
    return lot_price / months


def main():
    """
    Main function to execute the script logic.
    """
    print("Welcome to Acacias Retiro Campestre Lot Purchase Calculator!")

    # Step 1: Gather input from the user
    lot_price = get_positive_float("Enter the price of the lot (in USD): ")
    financing_months = get_valid_int(
        "Enter the number of months for financing (0 for cash payment or 12-36 for financing): ",
        0,
        36,
    )

    # Step 2: Calculate the total cost and monthly payment
    if financing_months == 0:
        print(f"\nTotal cost of the lot: ${lot_price:.2f}")
        print("You have chosen to make a single upfront payment.")
    else:
        monthly_payment = calculate_financing(lot_price, financing_months)
        print(f"\nTotal cost of the lot: ${lot_price:.2f}")
        print(
            f"Financing selected: {financing_months} months with 0% interest."
        )
        print(f"Monthly payment: ${monthly_payment:.2f}")

    print("\nThank you for using the Acacias Retiro Campestre calculator!")


# Entry point of the script
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)
```
