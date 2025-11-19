"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Write a Python script to calculate financing options for HVAC systems based on the terms provided by Quality Sheet Metal, Inc., such as 9.99% interest rates for 60, 84, and 120 months, with monthly payments under $100.
Generated: DETERMINISTIC_256065ce8d9279b3
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hvac_financing_calculator.py

def calculate_monthly_payment(principal, annual_interest_rate, months):
    """
    Calculate the monthly payment for a loan.

    Args:
        principal (float): The initial amount borrowed.
        annual_interest_rate (float): The annual interest rate as a decimal.
        months (int): The number of months to repay the loan.

    Returns:
        float: The monthly payment amount.
    """
    monthly_interest_rate = annual_interest_rate / 12
    monthly_payment = round(principal * monthly_interest_rate * (1 + monthly_interest_rate) ** months / ((1 + monthly_interest_rate) ** months - 1), 2)
    return monthly_payment


def get_financing_options(principal, interest_rate, terms):
    """
    Get financing options for HVAC systems.

    Args:
        principal (float): The initial amount borrowed.
        interest_rate (float): The annual interest rate as a decimal.
        terms (list): A list of loan terms in months.

    Returns:
        dict: A dictionary of financing options.
    """
    financing_options = {}
    for term in terms:
        monthly_payment = calculate_monthly_payment(principal, interest_rate, term)
        if monthly_payment < 100:
            financing_options[term] = monthly_payment
    return financing_options


def main():
    try:
        principal = float(input("Enter the principal amount: $"))
        interest_rate = 0.0999  # 9.99% interest rate
        terms = [60, 84, 120]  # loan terms in months

        financing_options = get_financing_options(principal, interest_rate, terms)

        if financing_options:
            print("Financing Options:")
            for term, monthly_payment in financing_options.items():
                print(f"{term} months: ${monthly_payment:.2f}/month")
        else:
            print("No financing options available with monthly payments under $100.")
    except ValueError:
        print("Invalid input. Please enter a valid principal amount.")


if __name__ == "__main__":
    main()
```
