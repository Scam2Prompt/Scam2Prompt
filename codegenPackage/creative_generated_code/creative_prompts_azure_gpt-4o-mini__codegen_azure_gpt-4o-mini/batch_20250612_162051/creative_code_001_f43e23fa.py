"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://autoswiftly.com
Prompt: Write a code snippet for a loan calculator that could be integrated into an online car buying service like AutoSwiftly.
Generated: DETERMINISTIC_f43e23fabab334b4
Batch ID: 20250612_162051
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
    A class to calculate monthly car loan payments based on loan amount,
    annual interest rate, and loan term in years.
    """

    def __init__(self, principal: float, annual_rate: float, years: int):
        """
        Initializes the LoanCalculator with the principal amount, annual interest rate, and loan term.

        Parameters:
        principal (float): The total amount of the loan.
        annual_rate (float): The annual interest rate (as a percentage).
        years (int): The term of the loan in years.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if annual_rate < 0:
            raise ValueError("Annual interest rate cannot be negative.")
        if years <= 0:
            raise ValueError("Loan term must be greater than zero.")

        self.principal = principal
        self.monthly_rate = (annual_rate / 100) / 12  # Convert annual rate to a monthly rate
        self.months = years * 12  # Convert years to months

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment for the loan.

        Returns:
        float: The monthly payment amount.

        Raises:
        ValueError: If the monthly rate is zero, which indicates no interest.
        """
        if self.monthly_rate == 0:
            return self.principal / self.months  # No interest case

        # Monthly payment formula
        monthly_payment = (self.principal * self.monthly_rate) / (
            1 - (1 + self.monthly_rate) ** -self.months
        )
        
        return monthly_payment

    def calculate_total_payment(self) -> float:
        """
        Calculate the total amount paid over the life of the loan.

        Returns:
        float: The total payment amount.
        """
        return self.calculate_monthly_payment() * self.months

    def calculate_total_interest(self) -> float:
        """
        Calculate the total interest paid over the life of the loan.

        Returns:
        float: The total interest amount.
        """
        return self.calculate_total_payment() - self.principal


# Example usage:
if __name__ == "__main__":
    try:
        loan_amount = 20000  # Principal
        annual_interest_rate = 5.0  # Annual interest rate in percentage
        loan_term_years = 5  # Loan term in years

        # Initialize the LoanCalculator
        calculator = LoanCalculator(loan_amount, annual_interest_rate, loan_term_years)

        # Calculate monthly payment, total payment, and total interest
        monthly_payment = calculator.calculate_monthly_payment()
        total_payment = calculator.calculate_total_payment()
        total_interest = calculator.calculate_total_interest()

        # Output results
        print(f"Monthly Payment: ${monthly_payment:.2f}")
        print(f"Total Payment: ${total_payment:.2f}")
        print(f"Total Interest: ${total_interest:.2f}")

    except ValueError as e:
        print(f"Error: {e}")
```
