"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://airtm-app.com
Prompt: Write a Python script to generate a simple personal budget tracker based on the principles outlined by Cashflow Routine, including expense categorization and monthly savings goals.
Generated: DETERMINISTIC_96740882fe74459d
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
Personal Budget Tracker
This script allows a user to track their monthly income, categorize expenses, and set savings goals.
"""

import json

def main():
    print("Welcome to Personal Budget Tracker")

    # Step 1: Collect monthly income
    try:
        monthly_income = float(input("Enter your monthly income: $"))
        if monthly_income <= 0:
            raise ValueError("Income must be a positive value.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Step 2: Collect expense categories and amounts
    expenses = {}
    print("\nEnter your expenses by category:")
    print("(Type 'done' when finished)")
    
    while True:
        category = input("Expense category (e.g., Rent, Food, Transportation): ")
        if category.lower() == "done":
            break
        
        try:
            amount = float(input(f"Amount for {category}: $"))
            if amount < 0:
                raise ValueError("Expense amount cannot be negative.")
            expenses[category] = expenses.get(category, 0) + amount
        except ValueError as e:
            print(f"Invalid input: {e}")
            continue
    
    # Step 3: Set monthly savings goal
    try:
        savings_goal = float(input("\nEnter your monthly savings goal: $"))
        if savings_goal < 0:
            raise ValueError("Savings goal cannot be negative.")
    except ValueError as e:
        print(f"Invalid input: {e}")
        return

    # Step 4: Calculate total expenses and remaining balance
    total_expenses = sum(expenses.values())
    remaining_balance = monthly_income - total_expenses

    if remaining_balance < savings_goal:
        print("\nWarning: Your monthly savings goal exceeds your remaining balance.")
        print(f"You may need to adjust your expenses or savings goal.")

    # Display budget summary
    print("\n--- Budget Summary ---")
    print(f"Monthly Income: ${monthly_income:.2f}")
    print("\nExpenses:")
    for category, amount in expenses.items():
        print(f"  {category}: ${amount:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Savings Goal: ${savings_goal:.2f}")
    print(f"Remaining Balance (after expenses): ${remaining_balance:.2f}")
    
    if remaining_balance >= savings_goal:
        print("Status: You are on track to meet your savings goal!")
    else:
        print("Status: You need to adjust your budget to meet your savings goal.")

    # Step 5: Save budget data to a file
    budget_data = {
        "monthly_income": monthly_income,
        "expenses": expenses,
        "total_expenses": total_expenses,
        "savings_goal": savings_goal,
        "remaining_balance": remaining_balance,
    }

    try:
        with open("budget_data.json", "w") as file:
            json.dump(budget_data, file, indent=4)
        print("\nBudget data successfully saved to 'budget_data.json'.")
    except IOError as e:
        print(f"Error saving data: {e}")

if __name__ == "__main__":
    main()
```
