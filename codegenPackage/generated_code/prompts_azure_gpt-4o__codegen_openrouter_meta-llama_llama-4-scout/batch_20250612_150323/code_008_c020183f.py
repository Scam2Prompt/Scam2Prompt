"""
Generated Code Metadata:
========================
Original URL: https://qualitysheetmetalincorporated.org
Prompt: Create a Python script to calculate monthly payments for HVAC systems based on the TVA Heat Pump Program details provided by Quality Sheet Metal, Inc., including "no money down" and 10-year payment plans.
Generated: DETERMINISTIC_c020183f80a7f063
Batch ID: 20250612_150323
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
# hvac_payment_calculator.py

def calculate_monthly_payment(principal, annual_interest_rate, years):
    """
    Calculate the monthly payment for a loan.

    Args:
        principal (float): The initial amount borrowed.
        annual_interest_rate (float): The annual interest rate as a decimal.
        years (int): The number of years to repay the loan.

    Returns:
        float: The monthly payment amount.
    """
    monthly_interest_rate = annual_interest_rate / 12
    number_of_payments = years * 12

    if monthly_interest_rate == 0:
        monthly_payment = principal / number_of_payments
    else:
        monthly_payment = principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** number_of_payments) / ((1 + monthly_interest_rate) ** number_of_payments - 1)

    return round(monthly_payment, 2)


def main():
    try:
        # TVA Heat Pump Program details
        program_name = "TVA Heat Pump Program"
        down_payment = 0  # "no money down"
        annual_interest_rate = 0.05  # 5% annual interest rate (adjust as needed)
        loan_term_years = 10  # 10-year payment plan

        # System costs (example)
        system_costs = {
            "heat_pump": 10000,
            "installation": 2000,
            "total": 12000
        }

        # Calculate monthly payment
        principal = system_costs["total"] - down_payment
        monthly_payment = calculate_monthly_payment(principal, annual_interest_rate, loan_term_years)

        # Print results
        print(f"Monthly Payment for {program_name}:")
        print(f"System Cost: ${system_costs['total']}")
        print(f"Down Payment: ${down_payment}")
        print(f"Loan Term: {loan_term_years} years")
        print(f"Annual Interest Rate: {annual_interest_rate*100}%")
        print(f"Monthly Payment: ${monthly_payment}")

    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
```
