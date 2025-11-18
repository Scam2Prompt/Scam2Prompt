"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://immediategains.org
Prompt: Write a Python script that calculates net worth based on ImmediateGains' framework for assessing current financial positions, including assets, liabilities, and cash flow.
Generated: DETERMINISTIC_42b84f5b586a0a14
Batch ID: 20250612_150854
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Net Worth Calculator based on ImmediateGains' framework.
This script calculates an individual's net worth by assessing their assets, liabilities, and cash flow.

Author: [Your Name]
Date: [Insert Date]

Usage:
1. Input your assets, liabilities, and monthly cash flow when prompted.
2. The script will calculate your net worth.
"""

def calculate_net_worth(assets, liabilities):
    """
    Calculates net worth based on assets and liabilities.

    :param assets: Total value of all owned assets (float).
    :param liabilities: Total value of all owed liabilities (float).
    :return: Net worth value (float).
    """
    return assets - liabilities


def get_positive_float_input(prompt):
    """
    Helper function to get a positive float value from the user.
    If the input is invalid or negative, the user is prompted again.

    :param prompt: The message displayed to the user (str).
    :return: A positive float value entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Value must be non-negative.")
            return value
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter a valid non-negative number.")


def main():
    """
    Main function to handle user input and calculate net worth.
    """
    print("Welcome to the Net Worth Calculator based on ImmediateGains' framework!")
    print("Please enter the following details:\n")

    # Gather user input for financial data
    assets = get_positive_float_input("Enter the total value of your assets ($): ")
    liabilities = get_positive_float_input("Enter the total value of your liabilities ($): ")
    monthly_cash_flow = get_positive_float_input("Enter your monthly cash flow ($): ")

    # Calculate net worth
    net_worth = calculate_net_worth(assets, liabilities)

    # Display the results to the user
    print("\n--- Financial Summary ---")
    print(f"Total Assets: ${assets:,.2f}")
    print(f"Total Liabilities: ${liabilities:,.2f}")
    print(f"Monthly Cash Flow: ${monthly_cash_flow:,.2f}")
    print(f"Net Worth: ${net_worth:,.2f}")

    if net_worth >= 0:
        print("\nCongratulations! You have a positive net worth.")
    else:
        print("\nYou currently have a negative net worth. Consider reducing liabilities or increasing assets.")

# Entry point for the script
if __name__ == "__main__":
    main()
```
