"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://claim-idegen.com
Prompt: Write Python code to simulate flexible loan calculations for personal and business financing, incorporating parameters like loan amount, interest rate, and repayment period, as described on Ambro Contables' website.
Generated: DETERMINISTIC_65b04bdc46784335
Batch ID: 20250612_150417
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LoanCalculator:
    """
    A class to represent a loan calculator that computes monthly payments
    and total payment for personal and business financing.
    """

    def __init__(self, loan_amount: float, annual_interest_rate: float, years: int):
        """
        Initialize the LoanCalculator with loan amount, interest rate, and repayment period.

        Args:
            loan_amount (float): The total amount of the loan.
            annual_interest_rate (float): The annual interest rate (in percentage).
            years (int): The number of years over which the loan will be repaid.
        """
        self.loan_amount = loan_amount
        self.annual_interest_rate = annual_interest_rate
        self.years = years

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment using the loan amount, interest rate, and years.

        Returns:
            float: The calculated monthly payment.
        """
        # Check for valid input values
        if self.loan_amount <= 0 or self.annual_interest_rate < 0 or self.years <= 0:
            raise ValueError("Invalid loan parameters. All values must be positive.")
        
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.years * 12

        # Monthly payment formula
        if monthly_interest_rate == 0:  # Handle the zero-interest case
            return self.loan_amount / number_of_payments
        
        monthly_payment = (self.loan_amount * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -number_of_payments)

        return monthly_payment

    def calculate_total_payment(self) -> float:
        """
        Calculate the total payment over the entire duration of the loan.

        Returns:
            float: The total payment amount.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.years * 12
        return total_payment

    def calculate_total_interest(self) -> float:
        """
        Calculate the total interest paid over the life of the loan.

        Returns:
            float: The total interest amount.
        """
        total_payment = self.calculate_total_payment()
        total_interest = total_payment - self.loan_amount
        return total_interest


if __name__ == "__main__":
    # Example usage
    try:
        loan_amount = 10000  # Example loan amount
        interest_rate = 5.0  # Example annual interest rate
        repayment_period = 3  # Example repayment period in years

        loan_calculator = LoanCalculator(loan_amount, interest_rate, repayment_period)

        monthly_payment = loan_calculator.calculate_monthly_payment()
        total_payment = loan_calculator.calculate_total_payment()
        total_interest = loan_calculator.calculate_total_interest()

        print(f"Monthly Payment: {monthly_payment:.2f}")
        print(f"Total Payment: {total_payment:.2f}")
        print(f"Total Interest Paid: {total_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
