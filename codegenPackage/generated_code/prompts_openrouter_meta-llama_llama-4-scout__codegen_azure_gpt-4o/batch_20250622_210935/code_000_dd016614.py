"""
Generated Code Metadata:
========================
Original URL: https://maisemprestimos.online
Prompt: Write a Python script to calculate an individual's debt-to-income ratio, considering their monthly expenses and income, based on the 30% rule mentioned in this guide.
Generated: DETERMINISTIC_dd0166146130b17f
Batch ID: 20250622_210935
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
"""
Debt-to-Income Ratio Calculator

This script calculates an individual's debt-to-income (DTI) ratio based on their monthly expenses and income.
It also evaluates whether the DTI ratio adheres to the 30% rule, which suggests that debt should not exceed 30% of income.

Usage:
- Provide monthly income and monthly debt expenses as inputs.
- The script will calculate the DTI ratio and provide feedback based on the 30% rule.

Author: Expert Programmer
"""

def calculate_dti_ratio(monthly_income, monthly_expenses):
    """
    Calculate the Debt-to-Income (DTI) ratio.

    Args:
        monthly_income (float): The individual's monthly income.
        monthly_expenses (float): The individual's monthly debt-related expenses.

    Returns:
        float: The DTI ratio as a percentage.
    """
    try:
        # Ensure inputs are valid numbers
        if monthly_income <= 0:
            raise ValueError("Monthly income must be greater than zero.")
        if monthly_expenses < 0:
            raise ValueError("Monthly expenses cannot be negative.")

        # Calculate DTI ratio
        dti_ratio = (monthly_expenses / monthly_income) * 100
        return round(dti_ratio, 2)
    except ZeroDivisionError:
        raise ValueError("Monthly income cannot be zero.")
    except TypeError:
        raise ValueError("Inputs must be numeric values.")

def evaluate_dti_ratio(dti_ratio):
    """
    Evaluate the DTI ratio based on the 30% rule.

    Args:
        dti_ratio (float): The calculated DTI ratio.

    Returns:
        str: A message indicating whether the DTI ratio is within acceptable limits.
    """
    if dti_ratio <= 30:
        return "Your debt-to-income ratio is within the recommended limit of 30%."
    else:
        return "Your debt-to-income ratio exceeds the recommended limit of 30%. Consider reducing your debt."

def main():
    """
    Main function to execute the DTI ratio calculation and evaluation.
    """
    print("Welcome to the Debt-to-Income Ratio Calculator!")
    
    try:
        # Get user inputs
        monthly_income = float(input("Enter your monthly income: "))
        monthly_expenses = float(input("Enter your monthly debt-related expenses: "))

        # Calculate DTI ratio
        dti_ratio = calculate_dti_ratio(monthly_income, monthly_expenses)

        # Display results
        print(f"\nYour Debt-to-Income (DTI) Ratio: {dti_ratio}%")
        print(evaluate_dti_ratio(dti_ratio))
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
```
