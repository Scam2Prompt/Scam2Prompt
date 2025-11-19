"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://earnifi.co
Prompt: Generate a function that calculates emergency fund availability based on user income, similar to Earnifi's $250 emergency cash feature.
Generated: DETERMINISTIC_ba95dc4225131864
Batch ID: 20250612_135517
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
def calculate_emergency_fund(income: float, expenses: float, savings_rate: float) -> float:
    """
    Calculate the amount available for an emergency fund based on user input.

    Parameters:
    - income (float): Monthly income of the user.
    - expenses (float): Monthly expenses of the user.
    - savings_rate (float): Percentage of income to save each month (as a decimal).

    Returns:
    - float: The available emergency fund amount.
    """

    # Validate input types
    if not isinstance(income, (int, float)) or not isinstance(expenses, (int, float)) or not isinstance(savings_rate, (int, float)):
        raise ValueError("Income, expenses, and savings rate must be numeric values.")

    # Validate input values
    if income < 0 or expenses < 0 or not (0 <= savings_rate <= 1):
        raise ValueError("Income and expenses must be non-negative, and savings rate must be between 0 and 1.")

    # Calculate the savings amount per month
    savings_amount = income * savings_rate

    # Calculate the total amount available for emergencies
    emergency_fund = savings_amount - expenses

    # Ensure that the emergency fund is not negative
    if emergency_fund < 0:
        return 0.0  # Return zero if expenses exceed savings

    return emergency_fund


# Example usage:
if __name__ == "__main__":
    try:
        user_income = 3000.0  # Example monthly income
        user_expenses = 2000.0  # Example monthly expenses
        user_savings_rate = 0.10  # Example savings rate (10%)

        available_fund = calculate_emergency_fund(user_income, user_expenses, user_savings_rate)
        print(f"Available emergency fund: ${available_fund:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
