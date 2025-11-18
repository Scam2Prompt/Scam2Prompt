"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://onlinelender.online
Prompt: "Generate code to implement a loan calculator using the loan terms and filters described on onlinelender.online."
Generated: DETERMINISTIC_5ed0bb76eaf46205
Batch ID: 20250612_145727
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
    A class to represent a loan calculator that computes monthly payments, 
    total payments, and total interest for a loan based on principal, 
    annual interest rate, and loan term in months.
    """

    def __init__(self, principal: float, annual_interest_rate: float, loan_term_months: int):
        """
        Initializes the LoanCalculator with loan parameters.

        :param principal: The total amount of the loan.
        :param annual_interest_rate: Annual interest rate as a percentage.
        :param loan_term_months: The term of the loan in months.
        """
        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.loan_term_months = loan_term_months

    def calculate_monthly_payment(self) -> float:
        """
        Calculates the monthly payment using the formula for an amortizing loan.

        :return: The monthly payment amount.
        :raises ValueError: If the loan term is non-positive or if the principal 
                            or interest rate are negative.
        """
        if self.loan_term_months <= 0:
            raise ValueError("Loan term must be greater than zero.")
        if self.principal < 0 or self.annual_interest_rate < 0:
            raise ValueError("Principal and interest rate must be non-negative.")
        
        # Convert annual interest rate to a monthly interest rate (decimal)
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        
        # If interest rate is 0, return principal divided by loan term
        if monthly_interest_rate == 0:
            return self.principal / self.loan_term_months
        
        # Calculate monthly payment using the formula
        monthly_payment = (self.principal * monthly_interest_rate) / \
                          (1 - (1 + monthly_interest_rate) ** -self.loan_term_months)
        return monthly_payment

    def calculate_total_payment(self) -> float:
        """
        Calculates the total payment over the life of the loan.

        :return: The total payment amount.
        """
        monthly_payment = self.calculate_monthly_payment()
        total_payment = monthly_payment * self.loan_term_months
        return total_payment

    def calculate_total_interest(self) -> float:
        """
        Calculates the total interest paid over the life of the loan.

        :return: The total interest amount.
        """
        total_payment = self.calculate_total_payment()
        total_interest = total_payment - self.principal
        return total_interest

if __name__ == "__main__":
    try:
        # Example loan parameters
        principal_amount = 10000  # Principal amount of the loan
        annual_rate = 5.0  # Annual interest rate in percentage
        term_months = 24  # Loan term in months
        
        # Create a LoanCalculator instance
        loan_calculator = LoanCalculator(principal_amount, annual_rate, term_months)
        
        # Calculate and display loan details
        monthly_payment = loan_calculator.calculate_monthly_payment()
        total_payment = loan_calculator.calculate_total_payment()
        total_interest = loan_calculator.calculate_total_interest()
        
        print(f"Monthly Payment: ${monthly_payment:.2f}")
        print(f"Total Payment: ${total_payment:.2f}")
        print(f"Total Interest: ${total_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
