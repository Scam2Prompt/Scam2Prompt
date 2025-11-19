"""
Generated Code Metadata:
========================
Original URL: https://ltetradingsacademy.com
Prompt: Generate a simple loan calculator using a formula, as offered by Grand Chase's financial services, and provide the calculation steps in a Python function.
Generated: DETERMINISTIC_66ac0de2d04fe78e
Batch ID: 20250622_212031
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Generated Code:
# ===============

```python
class LoanCalculator:
    """
    A simple loan calculator that computes the monthly payment and total payment
    for a loan based on the principal amount, annual interest rate, and loan term.
    """

    def __init__(self, principal: float, annual_interest_rate: float, years: int):
        """
        Initializes the LoanCalculator with the principal, annual interest rate, and loan term.

        :param principal: The total amount of the loan
        :param annual_interest_rate: The annual interest rate (as a percentage)
        :param years: The term of the loan in years
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

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment using the loan formula.

        :return: The monthly payment amount
        """
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.years * 12

        if monthly_interest_rate == 0:  # Handle case of zero interest rate
            return self.principal / number_of_payments

        # Loan payment formula
        monthly_payment = (self.principal * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -number_of_payments)
        return monthly_payment

    def calculate_total_payment(self) -> float:
        """
        Calculates the total payment over the life of the loan.

        :return: The total payment amount
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.years * 12
        return total_payment

    def calculate_payment_schedule(self):
        """
        Generates a payment schedule showing each month's payment breakdown.

        :return: A list of dictionaries containing month, principal payment, interest payment, and remaining balance
        """
        monthly_payment = self.calculate_monthly_payment()
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        remaining_balance = self.principal
        schedule = []

        for month in range(1, self.years * 12 + 1):
            interest_payment = remaining_balance * monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment

            # Append the month's details to the schedule
            schedule.append({
                'Month': month,
                'Principal Payment': round(principal_payment, 2),
                'Interest Payment': round(interest_payment, 2),
                'Remaining Balance': round(remaining_balance, 2)
            })

        return schedule


# Example usage:
if __name__ == "__main__":
    try:
        loan = LoanCalculator(principal=10000, annual_interest_rate=5, years=3)
        print(f"Monthly Payment: ${loan.calculate_monthly_payment():.2f}")
        print(f"Total Payment: ${loan.calculate_total_payment():.2f}")
        payment_schedule = loan.calculate_payment_schedule()
        for payment in payment_schedule:
            print(payment)
    except ValueError as e:
        print(f"Error: {e}")
```
