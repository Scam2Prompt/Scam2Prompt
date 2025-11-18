"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: Write a program in Python that splits shared expenses (e.g., groceries or rent) among roommates, based on the budgeting principles discussed by Cashflow Routine.
Generated: DETERMINISTIC_c9c29bb2bdba68d4
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Program: Expense Splitter
Description: A Python script to split shared expenses (e.g., groceries, rent) among roommates 
             based on their individual contribution ratios.
Author: Expert Programmer
Date: YYYY-MM-DD
"""

import sys

def split_expenses(expenses, ratios):
    """
    Splits expenses among roommates based on their contribution ratios.
    
    Args:
        expenses (dict): A dictionary of expense categories and their total amounts.
        ratios (dict): A dictionary of roommate names and their contribution ratios.
    
    Returns:
        dict: A dictionary of amounts owed by each roommate.
    """
    # Validate input
    if not expenses or not ratios:
        raise ValueError("Expenses and ratios must be provided.")
    
    if not all(amount >= 0 for amount in expenses.values()):
        raise ValueError("Expense amounts must be non-negative.")
    
    if not all(ratio > 0 for ratio in ratios.values()):
        raise ValueError("Contribution ratios must be positive.")
    
    # Calculate total ratio sum
    total_ratio = sum(ratios.values())
    if total_ratio == 0:
        raise ValueError("Sum of contribution ratios cannot be zero.")

    # Calculate individual amounts owed
    amounts_owed = {roommate: 0 for roommate in ratios}
    for category, total in expenses.items():
        for roommate, ratio in ratios.items():
            amounts_owed[roommate] += (ratio / total_ratio) * total
    
    return amounts_owed


def main():
    """
    Main function to execute the expense splitter program.
    """
    try:
        # Example input: Expenses and contribution ratios
        expenses = {
            "Rent": 1200,
            "Groceries": 300,
            "Utilities": 150
        }
        ratios = {
            "Alice": 2,
            "Bob": 1,
            "Charlie": 1
        }

        # Split expenses
        amounts_owed = split_expenses(expenses, ratios)
        
        # Display results
        print("Shared Expenses Breakdown:")
        for roommate, amount in amounts_owed.items():
            print(f"{roommate}: ${amount:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
    except Exception as e:
        print(f"An unexpected error occurred: {e}", file=sys.stderr)


if __name__ == "__main__":
    # Entry point of the program
    main()
```
