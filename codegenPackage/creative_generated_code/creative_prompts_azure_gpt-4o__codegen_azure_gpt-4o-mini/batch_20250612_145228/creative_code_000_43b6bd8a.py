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
class LoanCalculator:
    """
    A class to represent a loan calculator for SGFC Finance's personal loan product.
    """

    def __init__(self, principal: float, annual_interest_rate: float, repayment_term_years: int):
        """
        Initializes the loan calculator with the specified parameters.

        Parameters:
        principal (float): The amount of the loan.
        annual_interest_rate (float): The annual interest rate (in percentage).
        repayment_term_years (int): The repayment term in years.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_interest_rate <= 0:
            raise ValueError("Annual interest rate must be greater than zero.")
        if repayment_term_years <= 0:
            raise ValueError("Repayment term must be greater than zero.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate / 100  # Convert percentage to decimal
        self.repayment_term_years = repayment_term_years

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment using the formula for an amortizing loan.

        Returns:
        float: The monthly payment amount.
        """
        monthly_interest_rate = self.annual_interest_rate / 12
        number_of_payments = self.repayment_term_years * 12

        if monthly_interest_rate == 0:
            return self.principal / number_of_payments  # Handle zero interest case

        # Monthly payment formula
        monthly_payment = (self.principal * monthly_interest_rate) / (
            1 - (1 + monthly_interest_rate) ** -number_of_payments
        )
        return monthly_payment

    def calculate_total_payment(self) -> float:
        """
        Calculates the total payment over the lifetime of the loan.

        Returns:
        float: The total amount paid over the loan term.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.repayment_term_years * 12
        return total_payment

    def calculate_total_interest(self) -> float:
        """
        Calculates the total interest paid over the lifetime of the loan.

        Returns:
        float: The total interest amount.
        """
        total_payment = self.calculate_total_payment()
        total_interest = total_payment - self.principal
        return total_interest


if __name__ == "__main__":
    try:
        # Example usage of the LoanCalculator class
        principal_amount = 50000  # Principal loan amount
        annual_interest_rate = 5.5  # Annual interest rate in percentage
        repayment_term = 5  # Repayment term in years

        loan_calculator = LoanCalculator(principal_amount, annual_interest_rate, repayment_term)
        monthly_payment = loan_calculator.calculate_monthly_payment()
        total_payment = loan_calculator.calculate_total_payment()
        total_interest = loan_calculator.calculate_total_interest()

        print(f"Monthly Payment: ${monthly_payment:.2f}")
        print(f"Total Payment: ${total_payment:.2f}")
        print(f"Total Interest Paid: ${total_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
