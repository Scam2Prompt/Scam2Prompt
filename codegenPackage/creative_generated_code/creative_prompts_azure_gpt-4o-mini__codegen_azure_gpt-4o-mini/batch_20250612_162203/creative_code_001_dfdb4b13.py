"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://lending-ui-beta.vercel.app
Prompt: What are the key features of the Honey App's lending UI that I should consider when developing my own?
Generated: DETERMINISTIC_dfdb4b13c9c18952
Batch ID: 20250612_162203
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class LendingUI:
    """
    A class to represent the Lending User Interface for a financial application.
    This class encapsulates key features for a lending UI that enhance user experience
    and improve functionality.
    """

    def __init__(self):
        """
        Initializes the LendingUI with default settings.
        """
        self.loan_amount = 0.0
        self.loan_term = 0  # in months
        self.interest_rate = 0.0  # annual percentage rate

    def set_loan_amount(self, amount):
        """
        Sets the loan amount.
        
        :param amount: The desired loan amount (float).
        :raises ValueError: If the amount is less than or equal to zero.
        """
        if amount <= 0:
            raise ValueError("Loan amount must be greater than zero.")
        self.loan_amount = amount

    def set_loan_term(self, term):
        """
        Sets the loan term in months.
        
        :param term: The desired loan term in months (int).
        :raises ValueError: If the term is less than or equal to zero.
        """
        if term <= 0:
            raise ValueError("Loan term must be greater than zero.")
        self.loan_term = term

    def set_interest_rate(self, rate):
        """
        Sets the annual interest rate.
        
        :param rate: The annual interest rate as a percentage (float).
        :raises ValueError: If the rate is negative.
        """
        if rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        self.interest_rate = rate

    def calculate_monthly_payment(self):
        """
        Calculates the monthly payment for the loan using the formula for an annuity.
        
        :return: The monthly payment amount (float).
        :raises ValueError: If loan amount, term, or interest rate are not set properly.
        """
        if self.loan_amount <= 0 or self.loan_term <= 0 or self.interest_rate < 0:
            raise ValueError("Invalid loan details. Please ensure all fields are set correctly.")
        
        monthly_rate = self.interest_rate / 100 / 12  # Convert annual rate to monthly
        if monthly_rate == 0:
            return self.loan_amount / self.loan_term  # No interest scenario
        
        payment = (self.loan_amount * monthly_rate) / (1 - (1 + monthly_rate) ** -self.loan_term)
        return payment

    def display_loan_details(self):
        """
        Displays the loan details including amount, term, interest rate, and monthly payment.
        """
        try:
            monthly_payment = self.calculate_monthly_payment()
            print(f"Loan Amount: ${self.loan_amount:.2f}")
            print(f"Loan Term: {self.loan_term} months")
            print(f"Annual Interest Rate: {self.interest_rate:.2f}%")
            print(f"Monthly Payment: ${monthly_payment:.2f}")
        except ValueError as e:
            print(f"Error: {e}")

# Example of using the LendingUI class
if __name__ == "__main__":
    ui = LendingUI()
    
    try:
        ui.set_loan_amount(5000)  # Set loan amount to $5000
        ui.set_loan_term(24)      # Set loan term to 24 months
        ui.set_interest_rate(5)   # Set interest rate to 5%
        ui.display_loan_details()  # Display the loan details
    except ValueError as e:
        print(f"Input Error: {e}")
```
