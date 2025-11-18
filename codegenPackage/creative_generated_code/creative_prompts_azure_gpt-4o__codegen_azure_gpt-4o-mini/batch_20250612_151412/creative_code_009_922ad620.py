"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://www.klar.com.mx
Prompt: Write code to simulate Klar's personal loan repayment plan, allowing users to select flexible monthly installments.
Generated: DETERMINISTIC_922ad620f87318bb
Batch ID: 20250612_151412
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class PersonalLoan:
    def __init__(self, principal, annual_interest_rate, loan_term_years):
        """
        Initialize the PersonalLoan object.
        
        :param principal: The total amount of the loan.
        :param annual_interest_rate: The annual interest rate as a percentage (e.g., 5 for 5%).
        :param loan_term_years: The loan term in years.
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.loan_term_years = loan_term_years
        self.monthly_interest_rate = self.annual_interest_rate / 12  # Monthly interest
        self.total_payments = loan_term_years * 12  # Total number of monthly payments

    def calculate_monthly_payment(self):
        """
        Calculate the monthly payment using the formula for an amortizing loan.
        
        :return: The monthly payment amount.
        """
        if self.annual_interest_rate == 0:  # Handle zero interest rate case
            return self.principal / self.total_payments
        
        numerator = self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.total_payments
        denominator = (1 + self.monthly_interest_rate) ** self.total_payments - 1
        return self.principal * (numerator / denominator)

    def simulate_repayment_plan(self):
        """
        Simulate the repayment plan and display the amortization schedule.
        """
        try:
            monthly_payment = self.calculate_monthly_payment()
            print(f"Monthly Payment: {monthly_payment:.2f}")

            balance = self.principal
            schedule = []

            for month in range(1, self.total_payments + 1):
                interest_payment = balance * self.monthly_interest_rate
                principal_payment = monthly_payment - interest_payment
                balance -= principal_payment

                # Record the month, principal payment, interest payment, and remaining balance
                schedule.append({
                    "Month": month,
                    "Principal Payment": round(principal_payment, 2),
                    "Interest Payment": round(interest_payment, 2),
                    "Remaining Balance": round(balance, 2)
                })

            return schedule

        except Exception as e:
            print(f"An error occurred during the repayment simulation: {e}")

# Example usage:
if __name__ == "__main__":
    # Initialize the loan with a principal amount of 10000, annual interest rate of 5%, over 3 years
    loan = PersonalLoan(principal=10000, annual_interest_rate=5, loan_term_years=3)
    repayment_schedule = loan.simulate_repayment_plan()

    # Print the repayment schedule
    for payment in repayment_schedule:
        print(payment)
```
