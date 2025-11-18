"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sgfcfinance.com
Prompt: Write Python code to simulate a loan calculator for SGFC Finance's personal loan product, incorporating flexible repayment terms and competitive interest rates as described on their website.
Generated: DETERMINISTIC_43b6bd8a9171f54b
Batch ID: 20250612_145228
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
import math

class LoanCalculator:
    """
    A loan calculator for SGFC Finance's personal loan product.
    Incorporates flexible repayment terms and competitive interest rates.
    """

    def __init__(self, principal, annual_interest_rate, term_years):
        """
        Initialize the loan calculator with loan details.

        :param principal: Loan amount (in dollars)
        :param annual_interest_rate: Annual interest rate (percentage)
        :param term_years: Loan term (in years)
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.term_years = term_years

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment for the loan using the formula:
        M = P * (r * (1 + r)^n) / ((1 + r)^n - 1)

        :return: Monthly payment amount (in dollars)
        """
        # Convert annual interest rate to a monthly rate
        monthly_rate = self.annual_interest_rate / 100 / 12
        # Total number of monthly payments
        total_payments = self.term_years * 12

        # Handle division by zero for zero interest rate
        if monthly_rate == 0:
            return self.principal / total_payments

        # Calculate monthly payment
        numerator = self.principal * monthly_rate * (1 + monthly_rate) ** total_payments
        denominator = (1 + monthly_rate) ** total_payments - 1
        return numerator / denominator

    def generate_payment_schedule(self):
        """
        Generate the loan's payment schedule, including principal and interest breakdown.

        :return: List of dictionaries representing the payment schedule
        """
        schedule = []
        balance = self.principal
        monthly_payment = self.calculate_monthly_payment()
        monthly_rate = self.annual_interest_rate / 100 / 12

        for month in range(1, self.term_years * 12 + 1):
            interest_payment = balance * monthly_rate
            principal_payment = monthly_payment - interest_payment
            balance -= principal_payment
            balance = max(balance, 0)  # Avoid negative balance due to rounding

            schedule.append({
                "Month": month,
                "Principal Payment": round(principal_payment, 2),
                "Interest Payment": round(interest_payment, 2),
                "Remaining Balance": round(balance, 2)
            })

        return schedule


def main():
    """
    Main function to simulate the loan calculator for SGFC Finance.
    """
    print("Welcome to SGFC Finance's Loan Calculator!")

    try:
        # Gather user inputs
        principal = float(input("Enter loan amount (in dollars): "))
        annual_interest_rate = float(input("Enter annual interest rate (in %): "))
        term_years = int(input("Enter loan term (in years): "))

        # Validate inputs
        if principal <= 0 or annual_interest_rate < 0 or term_years <= 0:
            raise ValueError("All inputs must be positive. Interest rate cannot be negative.")

        # Create loan calculator instance
        calculator = LoanCalculator(principal, annual_interest_rate, term_years)

        # Calculate monthly payment
        monthly_payment = calculator.calculate_monthly_payment()
        print(f"\nYour estimated monthly payment is: ${monthly_payment:.2f}")

        # Generate payment schedule
        print("\nPayment Schedule:")
        schedule = calculator.generate_payment_schedule()
        for payment in schedule:
            print(payment)

    except ValueError as e:
        print(f"Input error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
```
