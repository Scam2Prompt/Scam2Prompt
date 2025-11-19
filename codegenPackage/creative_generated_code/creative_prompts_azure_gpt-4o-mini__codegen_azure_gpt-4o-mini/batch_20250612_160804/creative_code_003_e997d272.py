"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://reg-arcade-exf.pages.dev
Prompt: Create a code snippet that calculates the potential earnings from lending on the Arcade platform based on the current interest rates provided.
Generated: DETERMINISTIC_e997d272df5f5968
Batch ID: 20250612_160804
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class ArcadeLendingCalculator:
    """
    A class to calculate potential earnings from lending on the Arcade platform.
    """

    def __init__(self, principal: float, interest_rate: float, term_years: int):
        """
        Initialize the lending calculator with principal amount, interest rate and term.

        :param principal: The amount of money lent (float).
        :param interest_rate: The annual interest rate as a percentage (float).
        :param term_years: The duration of the loan in years (int).
        """
        if principal <= 0:
            raise ValueError("Principal amount must be greater than zero.")
        if interest_rate < 0:
            raise ValueError("Interest rate cannot be negative.")
        if term_years <= 0:
            raise ValueError("Term in years must be greater than zero.")

        self.principal = principal
        self.interest_rate = interest_rate / 100  # Convert percentage to decimal
        self.term_years = term_years

    def calculate_earnings(self) -> float:
        """
        Calculate the potential earnings from lending.

        :return: The total earnings after the term (float).
        """
        total_earnings = self.principal * (1 + self.interest_rate * self.term_years)
        return total_earnings

    def display_results(self):
        """
        Display the results of the earnings calculation.
        """
        try:
            total_earnings = self.calculate_earnings()
            print(f"Principal Amount: ${self.principal:.2f}")
            print(f"Interest Rate: {self.interest_rate * 100:.2f}%")
            print(f"Term: {self.term_years} years")
            print(f"Total Earnings: ${total_earnings:.2f}")
        except Exception as e:
            print(f"An error occurred while calculating earnings: {e}")


if __name__ == "__main__":
    try:
        # Example usage
        principal_amount = 1000.0  # Amount to be lent
        annual_interest_rate = 5.0  # Annual interest rate in percent
        loan_term_years = 3  # Duration of the loan in years

        # Create a lending calculator instance
        calculator = ArcadeLendingCalculator(principal_amount, annual_interest_rate, loan_term_years)

        # Display the results
        calculator.display_results()
    except ValueError as e:
        print(f"Input error: {e}")
```
