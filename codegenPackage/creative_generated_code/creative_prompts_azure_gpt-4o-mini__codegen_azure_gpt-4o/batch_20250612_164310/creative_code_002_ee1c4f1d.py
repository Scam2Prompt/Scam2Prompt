"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Create a Python script that simulates the "Pay Yourself First" strategy in personal finance, inspired by the guidelines from Ahmeti Wealth Management.
Generated: DETERMINISTIC_ee1c4f1d9eeded1a
Batch ID: 20250612_164310
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Pay Yourself First Strategy Simulator
This script simulates the "Pay Yourself First" personal finance strategy. It calculates savings 
based on a predetermined percentage of income and allocates the remainder to expenses.
Inspired by Ahmeti Wealth Management guidelines.

Author: Professional software developer
Date: YYYY-MM-DD
"""

import sys

def get_float_input(prompt):
    """
    Safely gets a float input from the user with error handling.
    :param prompt: The message to display to the user for input.
    :return: A valid float value.
    """
    while True:
        try:
            value = float(input(prompt))
            if value < 0:
                raise ValueError("Input must be a positive number.")
            return value
        except ValueError as e:
            print(f"Error: {e}. Please try again.")

def pay_yourself_first(income, savings_rate):
    """
    Calculates savings and expenses based on the "Pay Yourself First" strategy.
    :param income: Monthly income in float.
    :param savings_rate: Percentage of income to save (0-100).
    :return: Tuple containing savings and remaining income for expenses.
    """
    if savings_rate < 0 or savings_rate > 100:
        raise ValueError("Savings rate must be between 0 and 100.")
    
    savings = income * (savings_rate / 100)
    expenses = income - savings
    return savings, expenses

def main():
    """
    Main function to simulate the "Pay Yourself First" strategy.
    """
    print("Welcome to the Pay Yourself First Simulator!")
    
    # Get user inputs
    income = get_float_input("Enter your monthly income: $")
    savings_rate = get_float_input("Enter the percentage of income you want to save (0-100): ")
    
    try:
        # Calculate savings and expenses
        savings, expenses = pay_yourself_first(income, savings_rate)
        
        # Output the results
        print("\nResults:")
        print(f"Monthly income: ${income:.2f}")
        print(f"Savings rate: {savings_rate:.2f}%")
        print(f"Amount saved: ${savings:.2f}")
        print(f"Remaining for expenses: ${expenses:.2f}")
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
```
