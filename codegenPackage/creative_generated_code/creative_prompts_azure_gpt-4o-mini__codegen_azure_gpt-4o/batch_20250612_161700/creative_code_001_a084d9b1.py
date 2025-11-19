"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://inmobiliariacapri.com.co
Prompt: Write a Python script that simulates notarial expenses for property purchases, incorporating the specific calculations mentioned in the Inmobiliaria Capri's notarial expense simulator.
Generated: DETERMINISTIC_a084d9b1d5d85c31
Batch ID: 20250612_161700
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Notarial Expense Simulator for Property Purchases
This Python script simulates notarial expenses based on specific calculations used
by Inmobiliaria Capri's notarial expense simulator.

Author: Expert Programmer
Date: 2023-10
"""

import sys

# Constants
PROPERTY_PURCHASE_TAX_RATE = 0.015  # 1.5% of the property value
NOTARY_PUBLIC_FEES_PERCENTAGE = 0.005  # 0.5% of the property value
BASE_NOTARY_FEE = 500  # Fixed base fee for notary services
LEGAL_DOCUMENTATION_FEE = 150  # Fixed fee for legal paperwork

def calculate_notarial_expenses(property_value):
    """
    Calculate the total notarial expenses for a property purchase.

    :param property_value: The total value of the property being purchased.
    :return: A dictionary containing the breakdown of the expenses and the total.
    """
    try:
        if property_value <= 0:
            raise ValueError("Property value must be a positive number.")

        # Calculate individual expenses
        purchase_tax = property_value * PROPERTY_PURCHASE_TAX_RATE
        notary_fees = property_value * NOTARY_PUBLIC_FEES_PERCENTAGE + BASE_NOTARY_FEE
        total_expenses = purchase_tax + notary_fees + LEGAL_DOCUMENTATION_FEE

        # Return a breakdown
        return {
            "Property Value": property_value,
            "Purchase Tax (1.5%)": purchase_tax,
            "Notary Fees (0.5% + Base Fee)": notary_fees,
            "Legal Documentation Fee": LEGAL_DOCUMENTATION_FEE,
            "Total Notarial Expenses": total_expenses
        }
    except ValueError as ve:
        raise ve

def display_expenses(expenses):
    """
    Display the breakdown of notarial expenses in a readable format.

    :param expenses: A dictionary containing the breakdown of expenses.
    """
    print("\nNotarial Expense Breakdown:")
    for key, value in expenses.items():
        print(f"{key}: ${value:,.2f}")

def main():
    """
    Main function to interact with the user and calculate notarial expenses.
    """
    print("Welcome to the Notarial Expense Simulator.")
    try:
        # Get property value from user input
        property_value = float(input("Enter the property value (in USD): "))

        # Calculate expenses
        expenses = calculate_notarial_expenses(property_value)

        # Display results
        display_expenses(expenses)

    except ValueError:
        print("Error: Invalid input. Please enter a numeric property value greater than 0.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
