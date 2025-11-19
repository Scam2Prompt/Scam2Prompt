"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://cuotaschevrolet.com.ar
Prompt: Write a function that calculates monthly payments for a Chevrolet vehicle based on different financing options.
Generated: DETERMINISTIC_61e2767d3019fdba
Batch ID: 20250612_164321
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ChevroletFinancingCalculator:
    """
    A class to calculate the monthly payments for financing a Chevrolet vehicle.
    """

    def __init__(self, principal, annual_interest_rate, years):
        """
        Initializes the financing calculator with principal, interest rate, and loan term.

        :param principal: The total amount of the loan (vehicle price).
        :param annual_interest_rate: The annual interest rate as a percentage (e.g., 5 for 5%).
        :param years: The number of years to finance the loan.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if years <= 0:
            raise ValueError("Loan term must be greater than zero.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.years = years

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment for the loan using the formula for an amortizing loan.

        :return: The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.years * 12

        # Calculate monthly payment using the formula
        if monthly_interest_rate == 0:  # Handle the case of zero interest rate
            return self.principal / number_of_payments

        monthly_payment = (self.principal * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return monthly_payment

    def display_payment_schedule(self):
        """
        Displays a payment schedule for the loan.

        :return: None
        """
        print("Payment Schedule:")
        monthly_payment = self.calculate_monthly_payment()
        for month in range(1, self.years * 12 + 1):
            print(f"Month {month}: Payment = ${monthly_payment:.2f}")

# Example usage
if __name__ == "__main__":
    try:
        loan_amount = 30000  # Example principal amount for a Chevrolet vehicle
        interest_rate = 5  # Example interest rate
        loan_term = 5  # Example loan term in years

        calculator = ChevroletFinancingCalculator(loan_amount, interest_rate, loan_term)
        monthly_payment = calculator.calculate_monthly_payment()
        print(f"Monthly Payment: ${monthly_payment:.2f}")
        calculator.display_payment_schedule()
    except ValueError as e:
        print(f"Error: {e}")
```
