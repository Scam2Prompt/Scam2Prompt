"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: Create a Python program that calculates monthly savings based on tracked expenses and income, adhering to the budgeting strategies outlined by Cashflow Routine.
Generated: DETERMINISTIC_a3f222fdd9c3c1d4
Batch ID: 20250612_154313
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import sys

def calculate_monthly_savings(income, expenses):
    """
    Calculate monthly savings by subtracting total expenses from income.
    
    Args:
        income (float): Total monthly income.
        expenses (dict): Dictionary containing expense categories and their amounts.
    
    Returns:
        float: Monthly savings amount.
    """
    try:
        total_expenses = sum(expenses.values())
        monthly_savings = income - total_expenses
        return monthly_savings
    except Exception as e:
        print(f"Error calculating savings: {e}", file=sys.stderr)
        return None

def get_user_input():
    """
    Collect user input for income and expenses from the console.

    Returns:
        tuple: Monthly income (float) and expenses (dict).
    """
    try:
        # Get monthly income
        income = float(input("Enter your monthly income: "))
        
        # Get monthly expenses
        expenses = {}
        print("Enter your expenses (type 'done' to finish):")
        while True:
            category = input("Expense category (e.g., Rent, Food): ")
            if category.lower() == 'done':
                break
            try:
                amount = float(input(f"Amount for {category}: "))
                expenses[category] = amount
            except ValueError:
                print("Invalid amount. Please enter a valid number.")
        
        return income, expenses
    except ValueError:
        print("Invalid income input. Please enter a valid number.", file=sys.stderr)
        return None, None

def main():
    """
    Main function to run the monthly savings calculation program.
    """
    print("Welcome to Cashflow Routine's Monthly Savings Calculator!")
    
    income, expenses = get_user_input()
    
    # Ensure valid inputs were received
    if income is None or expenses is None:
        print("Failed to collect valid inputs. Exiting program.", file=sys.stderr)
        return
    
    # Calculate savings
    savings = calculate_monthly_savings(income, expenses)
    if savings is not None:
        print("\n--- Monthly Savings Report ---")
        print(f"Total Income: ${income:.2f}")
        print(f"Total Expenses: ${sum(expenses.values()):.2f}")
        print(f"Monthly Savings: ${savings:.2f}")
        if savings > 0:
            print("Congratulations! You are saving money.")
        elif savings < 0:
            print("Warning: You are spending more than your income.")
        else:
            print("You are breaking even this month.")
    else:
        print("An error occurred while calculating savings.", file=sys.stderr)

if __name__ == "__main__":
    main()
```
