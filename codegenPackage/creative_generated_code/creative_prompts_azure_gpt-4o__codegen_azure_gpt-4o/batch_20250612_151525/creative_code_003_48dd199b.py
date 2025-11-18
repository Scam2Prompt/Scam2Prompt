"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://ahmetiwealth.com
Prompt: Create a function in Python that implements the "Pay Yourself First" financial strategy, inspired by the philosophy discussed on Ahmeti Wealth Management's website.
Generated: DETERMINISTIC_48dd199bc780b525
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def pay_yourself_first(total_income, savings_percentage, fixed_expenses, variable_expenses):
    """
    Implements the 'Pay Yourself First' financial strategy.

    Parameters:
    - total_income (float): The total monthly income.
    - savings_percentage (float): The percentage of income to save (e.g., 20 for 20%).
    - fixed_expenses (float): Total fixed monthly expenses.
    - variable_expenses (float): Total variable monthly expenses.

    Returns:
    - dict: A dictionary containing the allocated amounts for:
        - Savings
        - Fixed Expenses
        - Variable Expenses
        - Remaining Balance
    """
    try:
        # Input validation
        if total_income < 0 or savings_percentage < 0 or fixed_expenses < 0 or variable_expenses < 0:
            raise ValueError("All inputs must be non-negative numbers.")

        if savings_percentage > 100:
            raise ValueError("Savings percentage cannot exceed 100.")

        # Calculate savings amount
        savings_amount = (savings_percentage / 100) * total_income

        # Ensure there's enough income to cover savings and expenses
        if savings_amount + fixed_expenses + variable_expenses > total_income:
            raise ValueError(
                "Total expenses and savings exceed total income. Adjust your percentages or expenses."
            )

        # Calculate remaining balance after savings and expenses
        remaining_balance = total_income - (savings_amount + fixed_expenses + variable_expenses)

        # Return the allocation breakdown
        return {
            "Savings": round(savings_amount, 2),
            "Fixed Expenses": round(fixed_expenses, 2),
            "Variable Expenses": round(variable_expenses, 2),
            "Remaining Balance": round(remaining_balance, 2),
        }

    except ValueError as ve:
        # Handle and report invalid input or logical errors
        return {"Error": str(ve)}

    except Exception as e:
        # Handle unexpected errors
        return {"Error": f"An unexpected error occurred: {str(e)}"}


# Example usage
if __name__ == "__main__":
    # Replace these values with actual inputs
    total_income = 5000
    savings_percentage = 20
    fixed_expenses = 2000
    variable_expenses = 1500

    result = pay_yourself_first(total_income, savings_percentage, fixed_expenses, variable_expenses)
    print(result)
```
