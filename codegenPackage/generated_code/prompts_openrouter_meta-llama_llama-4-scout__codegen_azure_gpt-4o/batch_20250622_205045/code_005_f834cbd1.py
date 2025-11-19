"""
Generated Code Metadata:
========================
Original URL: https://hispanicservices.com
Prompt: Develop a basic profit and loss statement template for a small business, including fields for revenue, expenses, and net income.
Generated: DETERMINISTIC_f834cbd152b18c2a
Batch ID: 20250622_205045
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# profit_loss_statement.py

# Import necessary modules
import sys

def calculate_net_income(revenue, expenses):
    """
    Calculate net income based on revenue and expenses.

    Parameters:
        revenue (float): Total revenue of the business.
        expenses (float): Total expenses of the business.

    Returns:
        float: Net income (revenue - expenses).
    """
    try:
        # Ensure inputs are valid numbers
        revenue = float(revenue)
        expenses = float(expenses)
        return revenue - expenses
    except ValueError:
        raise ValueError("Revenue and expenses must be valid numbers.")

def main():
    """
    Main function to generate a basic profit and loss statement.
    """
    print("Welcome to the Profit and Loss Statement Generator")
    print("Please enter the following details:\n")

    try:
        # Get user input for revenue and expenses
        revenue = input("Enter total revenue: ")
        expenses = input("Enter total expenses: ")

        # Calculate net income
        net_income = calculate_net_income(revenue, expenses)

        # Display the profit and loss statement
        print("\n--- Profit and Loss Statement ---")
        print(f"Total Revenue: ${float(revenue):,.2f}")
        print(f"Total Expenses: ${float(expenses):,.2f}")
        print(f"Net Income: ${net_income:,.2f}")
        print("---------------------------------")

    except ValueError as e:
        # Handle invalid input errors
        print(f"Error: {e}")
        sys.exit(1)
    except Exception as e:
        # Handle unexpected errors
        print(f"An unexpected error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Entry point of the program
    main()
```
