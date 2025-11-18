"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://hameiriz.co.il
Prompt: Write Python code to calculate quarterly tax payments for an independent business owner, considering Israeli tax regulations as described by Zvika Hameiri's accounting services.
Generated: DETERMINISTIC_fda5eb7741dbaa52
Batch ID: 20250612_153246
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
"""
Quarterly Tax Payment Calculator for Independent Business Owners in Israel

This script calculates the quarterly tax payments based on the user's income and expenses,
considering Israeli tax regulations. The user can input their quarterly income, expenses,
and tax rate. The script outputs the estimated tax payment for the quarter.
"""

def calculate_quarterly_tax(income, expenses, tax_rate):
    """
    Calculate the quarterly tax payment.
    
    Args:
        income (float): Total income for the quarter.
        expenses (float): Total expenses for the quarter.
        tax_rate (float): Effective tax rate (in percentage).
    
    Returns:
        float: Quarterly tax payment amount.
    """
    try:
        # Validate inputs
        if income < 0 or expenses < 0 or tax_rate < 0:
            raise ValueError("Income, expenses, and tax rate must be non-negative values.")
        
        if tax_rate > 100:
            raise ValueError("Tax rate must not exceed 100%.")

        # Calculate taxable income
        taxable_income = max(0, income - expenses)  # Ensure taxable income is not negative

        # Calculate tax payment
        tax_payment = taxable_income * (tax_rate / 100)

        return tax_payment

    except ValueError as ve:
        print(f"Input Error: {ve}")
        return None

    except Exception as e:
        print(f"Unexpected Error: {e}")
        return None


def main():
    """
    Main function to handle user input and display the calculated tax payment.
    """
    print("Quarterly Tax Payment Calculator\n")

    try:
        # Get user inputs
        income = float(input("Enter your total income for the quarter (NIS): "))
        expenses = float(input("Enter your total expenses for the quarter (NIS): "))
        tax_rate = float(input("Enter your effective tax rate (percentage): "))

        # Calculate tax
        tax_payment = calculate_quarterly_tax(income, expenses, tax_rate)

        if tax_payment is not None:
            print(f"\nYour estimated quarterly tax payment is: {tax_payment:.2f} NIS")

    except ValueError:
        print("Invalid input. Please enter numeric values for income, expenses, and tax rate.")
    except Exception as e:
        print(f"Unexpected Error: {e}")


if __name__ == "__main__":
    main()
```
