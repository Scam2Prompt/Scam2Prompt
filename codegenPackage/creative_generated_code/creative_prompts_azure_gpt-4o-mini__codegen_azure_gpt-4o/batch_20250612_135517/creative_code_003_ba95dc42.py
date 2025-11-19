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
def calculate_emergency_fund_availability(income, fixed_expenses, discretionary_expenses=0, desired_emergency_fund=250):
    """
    Calculates the availability of an emergency fund based on user income and expenses.

    Parameters:
    income (float): Monthly income of the user.
    fixed_expenses (float): Fixed monthly expenses that are unavoidable.
    discretionary_expenses (float): Optional discretionary expenses (default is 0).
    desired_emergency_fund (float): Desired emergency cash amount (default is $250).

    Returns:
    dict: A dictionary containing status and details of emergency fund availability.
    {
        "status": "Success" or "Insufficient Funds",
        "available_fund": float,
        "additional_needed": float
    }
    """
    try:
        # Input validation
        if income < 0 or fixed_expenses < 0 or discretionary_expenses < 0:
            raise ValueError("Income and expenses must be non-negative values.")

        # Calculate disposable income
        disposable_income = income - (fixed_expenses + discretionary_expenses)

        # Determine emergency fund availability
        if disposable_income >= desired_emergency_fund:
            return {
                "status": "Success",
                "available_fund": desired_emergency_fund,
                "additional_needed": 0.0
            }
        else:
            additional_needed = desired_emergency_fund - disposable_income
            return {
                "status": "Insufficient Funds",
                "available_fund": max(disposable_income, 0.0),
                "additional_needed": additional_needed
            }
    except TypeError:
        # Handle incorrect data types
        raise TypeError("Income and expenses must be numeric values.") from None
    except Exception as e:
        # Catch any unexpected errors
        return {
            "status": "Error",
            "message": str(e)
        }


# Example usage:
if __name__ == "__main__":
    try:
        result = calculate_emergency_fund_availability(income=3000, fixed_expenses=2000, discretionary_expenses=500)
        print(result)
    except Exception as e:
        print(f"An error occurred: {e}")
```
