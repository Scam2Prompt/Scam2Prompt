"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://juridiskklinik.se
Prompt: Develop a program that calculates property division according to Swedish "Sambolagen" (cohabitation law), as described on juridiskklinik.se.
Generated: DETERMINISTIC_dd93f00a41f91664
Batch ID: 20250612_152249
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Property Division Calculator for Swedish Sambolagen (Cohabitation Law)

This script calculates division of shared property according to the principles
of Sambolagen, which governs the division of joint property for cohabiting couples
in Sweden.

Author: Expert Programmer
Date: YYYY-MM-DD
"""

# Import necessary modules
import sys

def get_float_input(prompt):
    """
    Helper function to get float input from the user
    with basic error handling.

    :param prompt: Prompt to display to the user
    :return: Valid float value
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError as e:
            print(f"Error: {e}. Please enter a valid number.")

def calculate_division(person1_assets, person2_assets, person1_debts, person2_debts):
    """
    Calculates the division of property according to Sambolagen.

    :param person1_assets: Total assets of Person 1
    :param person2_assets: Total assets of Person 2
    :param person1_debts: Total debts of Person 1
    :param person2_debts: Total debts of Person 2
    :return: Tuple of shares for Person 1 and Person 2
    """
    # Net assets calculation
    person1_net_assets = person1_assets - person1_debts
    person2_net_assets = person2_assets - person2_debts

    # Ensure net assets are non-negative (debts cannot exceed assets in this calculation)
    person1_net_assets = max(person1_net_assets, 0)
    person2_net_assets = max(person2_net_assets, 0)

    # Total shared property
    total_shared_property = person1_net_assets + person2_net_assets

    # Division of property equally
    equal_share = total_shared_property / 2

    # Calculate the final shares
    person1_share = equal_share - person1_net_assets
    person2_share = equal_share - person2_net_assets

    return person1_share, person2_share

def main():
    """
    Main function to execute the property division calculator.
    """
    print("Welcome to the Sambolagen Property Division Calculator.")
    print("Please enter the financial details for both individuals.\n")

    # Get inputs for Person 1
    print("Enter details for Person 1:")
    person1_assets = get_float_input("  Total assets: ")
    person1_debts = get_float_input("  Total debts: ")

    # Get inputs for Person 2
    print("\nEnter details for Person 2:")
    person2_assets = get_float_input("  Total assets: ")
    person2_debts = get_float_input("  Total debts: ")

    # Calculate property division
    try:
        person1_share, person2_share = calculate_division(person1_assets, person2_assets, person1_debts, person2_debts)

        # Display results
        print("\nProperty Division Results:")
        print(f"  Person 1 owes: {person1_share:.2f} SEK (positive means receiving money, negative means owing money)")
        print(f"  Person 2 owes: {person2_share:.2f} SEK (positive means receiving money, negative means owing money)")
    except Exception as e:
        print(f"An error occurred during calculation: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
