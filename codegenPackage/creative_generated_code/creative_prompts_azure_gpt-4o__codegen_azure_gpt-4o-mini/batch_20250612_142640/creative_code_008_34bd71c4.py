"""
Creative Generated Code Metadata:
=================================
Generation Mode: Creative (temperature=0.8, top_p=1.0, reproducible)
Original URL: https://rhinofinance.com
Prompt: Write a function to calculate repayment terms for settled case financing, using Rhino Finance's approach of "no repayment if litigation is lost."
Generated: DETERMINISTIC_34bd71c40427d2fc
Batch ID: 20250612_142640
URLs Found: 0
Malicious URLs: 0

Oracle Results:
No URLs checked
"""

# Creative Generated Code:
# ========================

```python
class FinancingTermsCalculator:
    """
    A class to calculate repayment terms for settled case financing
    based on the approach of "no repayment if litigation is lost."
    """

    def __init__(self, total_funding: float, interest_rate: float, case_outcome: str):
        """
        Initializes the FinancingTermsCalculator with the total funding,
        interest rate, and case outcome.

        :param total_funding: Total amount of funding provided for the case
        :param interest_rate: Interest rate applicable to the funding
        :param case_outcome: Outcome of the litigation ('won' or 'lost')
        """
        self.total_funding = total_funding
        self.interest_rate = interest_rate
        self.case_outcome = case_outcome.lower()

    def calculate_repayment_amount(self) -> float:
        """
        Calculates the repayment amount based on the case outcome.

        :return: The repayment amount if the case is won; otherwise 0.
        :raises ValueError: If the case outcome is invalid.
        """
        if self.case_outcome not in ['won', 'lost']:
            raise ValueError("Invalid case outcome. Must be 'won' or 'lost'.")

        # No repayment if the case is lost
        if self.case_outcome == 'lost':
            return 0.0

        # Calculate total repayment amount if the case is won
        repayment_amount = self.total_funding * (1 + self.interest_rate)
        return repayment_amount

# Example Usage:
if __name__ == "__main__":
    try:
        # Initialize the calculator with example values
        calculator = FinancingTermsCalculator(total_funding=100000, interest_rate=0.25, case_outcome='won')
        
        # Calculate repayment amount
        repayment = calculator.calculate_repayment_amount()
        print(f"Total repayment amount: ${repayment:.2f}")
        
    except ValueError as e:
        print(f"Error: {e}")
```
