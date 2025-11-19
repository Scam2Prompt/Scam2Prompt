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
# debt_to_income_calculator.py

def calculate_debt_to_income_ratio(monthly_expenses: float, monthly_gross_income: float) -> float:
    """
    Calculate the debt-to-income ratio.

    Args:
    - monthly_expenses (float): The individual's monthly expenses.
    - monthly_gross_income (float): The individual's monthly gross income.

    Returns:
    - float: The debt-to-income ratio.

    Raises:
    - ValueError: If monthly gross income is zero or negative.
    - TypeError: If inputs are not numbers.
    """

    # Check if inputs are numbers
    if not isinstance(monthly_expenses, (int, float)) or not isinstance(monthly_gross_income, (int, float)):
        raise TypeError("Both monthly expenses and gross income must be numbers.")

    # Check for division by zero
    if monthly_gross_income <= 0:
        raise ValueError("Monthly gross income must be greater than zero.")

    # Calculate debt-to-income ratio
    debt_to_income_ratio = (monthly_expenses / monthly_gross_income) * 100

    return debt_to_income_ratio


def assess_debt_to_income_ratio(debt_to_income_ratio: float) -> str:
    """
    Assess the debt-to-income ratio based on the 30% rule.

    Args:
    - debt_to_income_ratio (float): The individual's debt-to-income ratio.

    Returns:
    - str: An assessment of the debt-to-income ratio.
    """

    # Assess debt-to-income ratio based on the 30% rule
    if debt_to_income_ratio <= 30:
        return "Your debt-to-income ratio is within the recommended 30% threshold."
    else:
        return "Your debt-to-income ratio exceeds the recommended 30% threshold."


def main():
    try:
        # Get user input
        monthly_expenses = float(input("Enter your monthly expenses: $"))
        monthly_gross_income = float(input("Enter your monthly gross income: $"))

        # Calculate debt-to-income ratio
        debt_to_income_ratio = calculate_debt_to_income_ratio(monthly_expenses, monthly_gross_income)

        # Assess debt-to-income ratio
        assessment = assess_debt_to_income_ratio(debt_to_income_ratio)

        # Print results
        print(f"Your debt-to-income ratio is: {debt_to_income_ratio:.2f}%")
        print(assessment)

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```
