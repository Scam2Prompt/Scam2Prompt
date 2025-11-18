"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://sublime.finance
Prompt: Create a function to simulate loan repayment schedules using parameters commonly used in DeFi platforms such as Sublime Finance.
Generated: DETERMINISTIC_d13204575c9f0e45
Batch ID: 20250612_150644
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoanRepaymentScheduler:
    """
    A class to simulate loan repayment schedules for DeFi platforms.
    """

    def __init__(self, principal, annual_interest_rate, term_years, payment_frequency=12):
        """
        Initializes the LoanRepaymentScheduler with principal, interest rate, term, and payment frequency.

        :param principal: The total loan amount (float).
        :param annual_interest_rate: The annual interest rate as a percentage (float).
        :param term_years: The term of the loan in years (int).
        :param payment_frequency: The number of payments per year (int, default is 12 for monthly).
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.term_years = term_years
        self.payment_frequency = payment_frequency

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment using the loan formula.

        :return: The monthly payment amount (float).
        """
        monthly_interest_rate = self.annual_interest_rate / self.payment_frequency
        total_payments = self.payment_frequency * self.term_years

        # Loan payment formula
        try:
            monthly_payment = (self.principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)
            return monthly_payment
        except ZeroDivisionError as e:
            raise ValueError("Annual interest rate must be greater than zero.") from e

    def generate_repayment_schedule(self):
        """
        Generates the loan repayment schedule.

        :return: A list of dictionaries containing payment details for each installment.
        """
        schedule = []
        monthly_payment = self.calculate_monthly_payment()
        remaining_balance = self.principal
        monthly_interest_rate = self.annual_interest_rate / self.payment_frequency

        for payment_number in range(1, self.payment_frequency * self.term_years + 1):
            interest_payment = remaining_balance * monthly_interest_rate
            principal_payment = monthly_payment - interest_payment
            remaining_balance -= principal_payment

            # Append the payment details to the schedule
            schedule.append({
                'Payment Number': payment_number,
                'Payment Amount': round(monthly_payment, 2),
                'Interest Payment': round(interest_payment, 2),
                'Principal Payment': round(principal_payment, 2),
                'Remaining Balance': round(max(remaining_balance, 0), 2)  # Prevent negative balance
            })
        
        return schedule


if __name__ == "__main__":
    # Example usage
    try:
        loan_amount = 50000  # Principal loan amount
        interest_rate = 5    # Interest rate in percent
        loan_term = 10       # Loan term in years

        # Initialize the loan scheduler
        loan_scheduler = LoanRepaymentScheduler(loan_amount, interest_rate, loan_term)

        # Generate repayment schedule
        repayment_schedule = loan_scheduler.generate_repayment_schedule()

        # Output the repayment schedule
        for payment in repayment_schedule:
            print(payment)

    except ValueError as e:
        print(f"Error: {e}")
```
