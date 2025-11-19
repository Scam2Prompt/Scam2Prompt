"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://maestrofinance.co.uk
Prompt: Generate a code snippet for a loan calculator that estimates monthly payments for unsecured business finance based on the amount borrowed and interest rate.
Generated: DETERMINISTIC_370ccf07ccec459a
Batch ID: 20250612_160158
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
    A simple loan calculator for estimating monthly payments on unsecured business finance.
    """

    def __init__(self, principal: float, annual_interest_rate: float, years: int):
        """
        Initialize the LoanCalculator with the principal amount, annual interest rate, and loan term in years.

        :param principal: The total amount borrowed (loan principal).
        :param annual_interest_rate: The annual interest rate in percentage (e.g., 5 for 5%).
        :param years: The loan term in years.
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if not (0 <= annual_interest_rate <= 100):
            raise ValueError("Annual interest rate must be between 0 and 100.")
        if years <= 0:
            raise ValueError("Loan term must be greater than zero years.")

        self.principal = principal
        self.annual_interest_rate = annual_interest_rate
        self.years = years

    def calculate_monthly_payment(self) -> float:
        """
        Calculate the monthly payment for the loan.

        :return: The estimated monthly payment.
        """
        monthly_interest_rate = self.annual_interest_rate / 100 / 12
        number_of_payments = self.years * 12
        
        if monthly_interest_rate == 0:  # Handle zero interest case
            return self.principal / number_of_payments
        
        # Monthly payment formula
        monthly_payment = (self.principal * monthly_interest_rate) / (
            1 - (1 + monthly_interest_rate) ** -number_of_payments
        )
        return monthly_payment

def main():
    """
    Main function to run the loan calculator.
    """
    try:
        # Example parameters for the loan calculator
        principal = float(input("Enter the loan amount: "))
        annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
        years = int(input("Enter the loan term (in years): "))

        # Create a LoanCalculator instance
        loan_calculator = LoanCalculator(principal, annual_interest_rate, years)

        # Calculate and display the monthly payment
        monthly_payment = loan_calculator.calculate_monthly_payment()
        print(f"The estimated monthly payment is: ${monthly_payment:.2f}")

    except ValueError as e:
        print(f"Input error: {e}")

if __name__ == "__main__":
    main()
```
