"""
Generated Code Metadata:
========================
Original URL: https://ahmetiwealth.com
Prompt: Create a function in Python that implements the "Pay Yourself First" financial strategy, inspired by the philosophy discussed on Ahmeti Wealth Management's website.
Generated: DETERMINISTIC_48dd199bc780b525
Batch ID: 20250612_151525
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
def pay_yourself_first(income: float, savings_rate: float, emergency_fund_rate: float, 
                       other_expenses: float) -> dict:
    """
    Implements the 'Pay Yourself First' financial strategy.

    Args:
    income (float): The total monthly income.
    savings_rate (float): The percentage of income to save for long-term goals.
    emergency_fund_rate (float): The percentage of income to save for emergency fund.
    other_expenses (float): The total monthly other expenses.

    Returns:
    dict: A dictionary containing the allocated amounts for savings, emergency fund, and other expenses.

    Raises:
    ValueError: If any of the input rates or expenses are negative.
    """

    # Validate input values
    if income < 0 or savings_rate < 0 or emergency_fund_rate < 0 or other_expenses < 0:
        raise ValueError("Income, savings rate, emergency fund rate, and other expenses must be non-negative.")

    # Calculate savings amount
    savings_amount = income * (savings_rate / 100)
    
    # Calculate emergency fund amount
    emergency_fund_amount = income * (emergency_fund_rate / 100)
    
    # Calculate total savings and emergency fund amount
    total_allocated = savings_amount + emergency_fund_amount
    
    # Check if total allocated amount exceeds income
    if total_allocated > income:
        raise ValueError("Total allocated amount exceeds income.")
    
    # Calculate disposable income after other expenses
    disposable_income = income - other_expenses
    
    # Check if disposable income is sufficient for savings and emergency fund
    if disposable_income < total_allocated:
        raise ValueError("Insufficient disposable income for savings and emergency fund.")
    
    # Calculate remaining income after allocating for savings, emergency fund, and other expenses
    remaining_income = income - total_allocated - other_expenses
    
    # Return allocated amounts
    return {
        "savings": savings_amount,
        "emergency_fund": emergency_fund_amount,
        "other_expenses": other_expenses,
        "remaining_income": remaining_income
    }


def main():
    try:
        income = 5000.0  # Example monthly income
        savings_rate = 10.0  # Example savings rate (10%)
        emergency_fund_rate = 5.0  # Example emergency fund rate (5%)
        other_expenses = 2000.0  # Example other monthly expenses

        allocated_amounts = pay_yourself_first(income, savings_rate, emergency_fund_rate, other_expenses)
        
        print("Allocated Amounts:")
        for category, amount in allocated_amounts.items():
            print(f"{category.capitalize().replace('_', ' ')}: ${amount:.2f}")
    
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
